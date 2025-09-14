from langchain_community.llms import Cohere
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
load_dotenv()

import os 

llm = Cohere(model="command", temperature=0.7)

# 1st prompt -> detaield report

template1 = PromptTemplate(
    template = 'write a detailed report on {topic}',
    input_variables = ['topic']
)
#   2nd prompt -> summary
template2 = PromptTemplate(
    template = 'write a 5 line summary on the following text. /n {text}',
    input_variables = {'text'}
)

prompt1 = template1.invoke({'topic': 'AI'})
result = llm.invoke(prompt1)

prompt2 = template2.invoke({'text': result})
result2 = llm.invoke(prompt2)

print(result2)