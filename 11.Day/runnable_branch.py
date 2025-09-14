from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough, RunnableBranch
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
    template = "write a detailed report on {topic}",
    input_variables = ['topic']
)

prompt1 = PromptTemplate(
    template = "summarize the following texr \n {text}",
    input_variables = ['text']
)

report_generation = prompt | llm | parser

branch_chain = RunnableBranch(
    (lambda x : len(x.split())>500, RunnableSequence(prompt1, llm, parser)),
    RunnablePassthrough()
)

final_chain = report_generation | branch_chain

print(final_chain.invoke({'topic':'Russia vs Ukraine'}))