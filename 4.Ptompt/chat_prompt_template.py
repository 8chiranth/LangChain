from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate



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

model = ChatHuggingFace(llm=llm)

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} assistant."),
    ("human", "Explain in simple terms, what is {topic}")
])

prompt = chat_template.format_prompt(domain="math", topic="calculus")
response = model.invoke(prompt.messages)
print(response.content)
