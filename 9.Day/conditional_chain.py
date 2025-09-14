from langchain_community.llms import Cohere
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

import os

llm = Cohere(model = 'command', temperature = 0.7)

parser = StrOutputParser( )

class Feedback(BaseModel):
    sentiment : Literal['positive', 'negative'] = Field(description = ' Give the sentiment of the feedbac')


parser2 = PydanticOutputParser( pydantic_object = Feedback)
prompt1 = PromptTemplate(
    template=(
        "Classify the sentiment of the following feedback text into 'positive' or 'negative'.\n"
        "Feedback: {feedback}\n"
        "Respond ONLY in valid JSON matching this schema:\n"
        "{format_instruction}"
    ),
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)



classifier_chain = prompt1 | llm | parser2

result = classifier_chain.invoke({'feedback':"this phone is a terrible product"}).sentiment
print(result)

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | llm | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | llm| parser),
    RunnableLambda(lambda x: "could not find sentiment")
)


chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a beautiful phone'}))

chain.get_graph().print_ascii()