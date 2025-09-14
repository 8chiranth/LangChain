from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.llms import Cohere  # new import
from dotenv import load_dotenv
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
import os

# Load environment variables
load_dotenv()

# Initialize the Cohere model (API key taken from .env automatically)
llm = Cohere(model="command", temperature=0.7)

schema = [
    ResponseSchema(name = "fact_1", description = 'fact 1 about the topic'),
    ResponseSchema(name = "fact_2", description = 'fact 2 about the topic'),
    ResponseSchema(name = "fact_3", description = 'fact 3 about the topic')

]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'give 3 facts about {topic} \n {format_instruction}',
    input_variables = ['topic'],
    partial_variables = {'format_instruction' : parser.get_format_instructions()}
)


prompt = template.invoke({'topic':'black hole'})

result = llm.invoke(prompt)

final_result = parser.parse(result)

print(final_result)