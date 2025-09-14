from langchain_community.llms import Cohere
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

import os


prompt = PromptTemplate(
    template = 'Generate 5 interesting facts about {topic}',
    input_variables = ['topic']
)

llm = Cohere(model="command", temperature = 0.7)

parser = StrOutputParser()


chain = prompt | llm | parser

result = chain.invoke({"topic": "cricker"})
print(result)

chain.get_graph().print_ascii()