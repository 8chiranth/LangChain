from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

parser = StrOutputParser()

prompt = PromptTemplate(
    template = "write a joke about {topic}",
    input_variables = ['topic']
)

prompt1 = PromptTemplate(
    template = "explain the following joke {text}",
    input_cariables = {'text'}
)

joke_gen_chain = RunnableSequence(prompt, llm, parser)

parallel_chain = RunnableParallel({
    "question" : RunnablePassthrough(), 
    "meaning" : RunnableSequence(prompt1, llm, parser)
})

final_chain = joke_gen_chain | parallel_chain

result = final_chain.invoke({'topic':'AI'})