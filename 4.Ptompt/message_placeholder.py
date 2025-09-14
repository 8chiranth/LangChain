from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import os 

os.environ['HF_HOME'] = 'D:/huggingface_cache' 

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    ),
    model_kwargs={"local_files_only": True}
)

#chat template

chat_template = ChatPromptTemplate([
    ('system', "you are a helpful customer support agent."),
    MessagesPlaceholder(variable_name = 'chat_history'),
    ('human', '{query}')
])
#load chat history
chat_history = []

with open('4.Ptompt\chat_history.txt') as f:
    chat_history.extend(f.readlines())
print(chat_history)
#create prompt
prompt = chat_template.invoke({'chat_history': chat_history, 'query' : 'wher is my refund?'})

print(prompt)