from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()


template = PromptTemplate(

    # template="Give me the name,age and city of a frictional person \n {format_instruction}",
    template="Give me 5 fact about {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# method 1
# prompt = template.format()
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
# print(final_result)

# method 2
chain = template | model | parser
result2 = chain.invoke({'topic':'black hole'})
print(result2)


# flaws is it does not enforce any proper schema