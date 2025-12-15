from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()


llm1 = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

llm2  = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-Instruct",
    task="text-generation"
)


model1 = ChatHuggingFace(llm=llm1)
model2 = ChatHuggingFace(llm=llm2)


prompt1 = PromptTemplate(
    template='Give a joke on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the text on {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

joke_generator_chain = RunnableSequence(prompt1,model1,parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'explain':RunnableSequence(prompt2,model2,parser)
})

final_chain = RunnableSequence(joke_generator_chain,parallel_chain)

result = final_chain.invoke({'topic':'AI'})
print(result)



