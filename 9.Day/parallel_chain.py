from langchain_community.llms import Cohere
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

import os

llm = Cohere(model = 'command', temperature = 0.7)

llm1 = Cohere(model = 'command', temperature = 0.7)

prompt1 = PromptTemplate(
    template = "generate short and simple notes from the following text \n {text}", 
    input_varibales = ['text']
)

prompt2 = PromptTemplate(
    template = "generate 5 short question answers for the following text \n {text}",
    input_variables = ['text']
)

prompt3 = PromptTemplate(
    template = "merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz} ",
    input_variables = ['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes' : prompt1 | llm | parser, 
    'quiz' : prompt2 | llm1 | parser
})

merge_chain = prompt3 | llm1 | parser

chain = parallel_chain | merge_chain

text = " gen ai langchain "

result = chain.invoke({'text':text})
print(result)

chain.get_graph().print_ascii()
