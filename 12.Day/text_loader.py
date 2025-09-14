from langchain_community.document_loaders import TextLoader

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()

parser = StrOutputParser()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

prompt = PromptTemplate(
    template = 'write a smmary for the following poem - \n {poem}',
    input_variables = ['poem']
)

loader = TextLoader('12.Day/cricket.txt', encoding = 'utf-8')

docs = loader.load()
chain = prompt | llm | parser

print(chain.invoke({'poem': docs[0].page_content}))



print(len(docs))
print(docs)