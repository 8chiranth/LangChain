from langchain_community.llms import Cohere
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

import os




prompt1 = PromptTemplate(
    template = 'Generate the summary one this {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'generate the 5 key points on {text}',
    input_variables = ['text']
)

llm = Cohere(model = "command", temperature = 0.7)

parser = StrOutputParser()



chain = prompt1 | llm | parser | prompt2 | llm | parser
result = chain.invoke({'topic': 'cricker'})

print(result)
chain.get_graph().print_ascii()