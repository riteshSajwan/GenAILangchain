# import os
# folder = r"D:\Gen AI\documentLoader"
# print(os.listdir(folder))  #to verify files

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r'D:\Gen AI\documentLoader\curriculum.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)

# can use other doc loader