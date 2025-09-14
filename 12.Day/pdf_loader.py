from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader('ABC-merged.pdf')
docs = loader.load()
print(docs[0])