from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

llm1 = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash', temperature = 0.7)

def word_count(text):
    return len(text.split())

parser = StrOutputParser()

prompt = PromptTemplate(
    template = "write a likedin post {topic}",
    input_variables = ['topic']
)

joke_gen = prompt | llm | parser

parallel_chain = RunnableParallel({
    "joke" : RunnablePassthrough(),
    "word_count" : RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen, parallel_chain)
result = final_chain.invoke({'topic':'AI'})
print(result)