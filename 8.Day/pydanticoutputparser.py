from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_community.llms import Cohere  # new import
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the Cohere model (API key taken from .env automatically)
llm = Cohere(model="command", temperature=0.7)


class Person(BaseModel):

    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt = template.invoke({'place':'indian'})
print(prompt)

result = llm.invoke(prompt)
final_result = parser.parse(result)
print(final_result)
# chain = template | llm | parser

# final_result = chain.invoke({'place':'sri lankan'})

# print(final_result)