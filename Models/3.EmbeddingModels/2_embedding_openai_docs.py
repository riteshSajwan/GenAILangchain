from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

documents = [
    "Delhi is capital of India",
    "Kolkata is capital of India",
    "Paries is the capital of India",
]

result = embedding.embed_documents(documents)
print(str(result))
