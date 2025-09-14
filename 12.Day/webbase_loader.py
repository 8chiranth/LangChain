from langchain_community.document_loaders import WebBaseLoader

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

import os
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-1.5-flash", temperature = 0.7
)

parser = StrOutputParser()

prompt = PromptTemplate(
    template = "answer the following question - \n{question} from the following text - \n {text}",
    input_variavles = ['question', 'text']
)

url = 'https://www.forbes.com/lists/india-billionaires/'

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | llm | parser

print(chain.invoke({'question':'what is the networth of ambani', 'text':docs[0].page_content}))
