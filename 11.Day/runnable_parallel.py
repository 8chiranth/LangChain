from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

llm1 = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash', temperature = 0.7)

parser = StrOutputParser()

prompt = PromptTemplate(
    template = "write a likedin post {topic}",
    input_variables = ['topic']
)

prompt1 = PromptTemplate(
    template = 'write a twiter post about {topic}',
    input_variables = ['topic']
)

parallel_chain = RunnableParallel({
    "tweet" : RunnableSequence(prompt1, llm, parser),
    "linkedin" : RunnableSequence(prompt, llm1, parser)
})

result = parallel_chain.invoke({'topic':'tokenization in LLM'})
print(result)