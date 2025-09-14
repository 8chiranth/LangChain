from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.llms import Cohere  # new import
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the Cohere model (API key taken from .env automatically)
llm = Cohere(model="command", temperature=0.7)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me the name, age and city of a fictional person \n{format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | llm | parser

result = chain.invoke({})

print(result)

# prompt = template.format()

# result = llm.invoke(prompt)
# final_result = parser.parse(result)
# print(final_result)
# print(type(final_result))
# 