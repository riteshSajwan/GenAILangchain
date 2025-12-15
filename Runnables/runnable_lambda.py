# for preprocessing


from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

def word_count(text):
    return len(text.split())

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

llm1 = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
)

model1 = ChatHuggingFace(llm=llm1)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model1, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    # 'word_count': RunnableLambda(word_count)
    'word_count': RunnableLambda(lambda x:len(x.split())),
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic':'AI'})

final_result = """{} \n word count -> {}""".format(result['joke'], result['word_count'])

print(final_result)