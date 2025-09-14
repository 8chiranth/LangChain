from langchain_core.messages import SystemMessage, HumanMessage, AIMessage  
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os 

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache' 


llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',  # use 'text-generation' for chat models like TinyLlama
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    ),
    model_kwargs={"local_files_only": True}  #  avoid downloading again
)

model = ChatHuggingFace(llm=llm)

user_input = input("User: ")

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content=user_input),

]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages) 