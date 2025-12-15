from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)


prompt1 = PromptTemplate(
    template='Write a joke on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the joke on {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)

print(chain.invoke({'topic':'AI'}))


