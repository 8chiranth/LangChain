from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)


prompt = PromptTemplate(
    template = "write a joke about {topic}",
    input_variables = ['topic']
)

prompt1 = PromptTemplate(
    template = "explain the following joke {text}",
    input_cariables = {'text'}
)
parser = StrOutputParser()

chain = RunnableSequence(prompt, llm, parser, prompt1, llm, parser)

print(chain.invoke({'topic':'AI'}))
