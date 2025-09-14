#++++++++++++++++++++++++++++>>>this is the code to run the chatbot without memory<<<+++++++++++++++++++++++++++++++
# from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
# import os


# os.environ['HF_HOME'] = 'D:/huggingface_cache' 


# llm = HuggingFacePipeline.from_model_id(
#     model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
#     task='text-generation',  # use 'text-generation' for chat models like TinyLlama
#     pipeline_kwargs=dict(
#         temperature=0.5,
#         max_new_tokens=100
#     ),
#     model_kwargs={"local_files_only": True}  #  avoid downloading again
# )

# model = ChatHuggingFace(llm=llm)

# chat_history = []

# # Chat loop
# while True:
#     user_input = input('You: ').lower()
#     chat_history.append(user_input)
#     if user_input.lower() == 'exit':
#         break
    
#     #storing the question history 
#     result = model.invoke(chat_history)
    

#     # Clean special tokens from the response
#     response = result.content.replace('<|user|>', '').replace('<|assistant|>', '').replace('</s>', '').strip()

#     #storing the response
#     chat_history.append(result.content)
    
#     print("AI:", response)

#+++++++++++++++++++++++>>>this is the code to run the chatbot with memory<<<+++++++++++++++++++++++++++++++

# from langchain_community.llms import Cohere
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage  
# from dotenv import load_dotenv

# import os 

# load_dotenv()

# import os


# llm = Cohere(model="command", 
#              temperature=0.7)



# chat_history = [
#     SystemMessage(content="You are a helpful assistant.")
# ]

# # Chat loop
# while True:
#     user_input = input('You: ')
#     if user_input.lower() == 'exit':
#         break
    
#     # Add user message
#     chat_history.append(HumanMessage(content=user_input))

#     # Generate assistant reply using message list (no need to build prompt manually!)
#     result = llm.invoke(chat_history)

#     # Clean response
#     response = result.replace('<|user|>', '').replace('<|assistant|>', '').replace('</s>', '').strip()

#     # Add assistant message to history
#     chat_history.append(AIMessage(content=response))

#     print("AI:", response)


from langchain_community.llms import Cohere
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage  
from dotenv import load_dotenv
import os

load_dotenv()

llm = Cohere(model="command", temperature=0.7)

chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]


while True:
    user_input = input('You: ')
    if user_input.lower() == "exit":
        print("See you later!")
        break

    chat_history.append(HumanMessage(content=user_input))

    # Build prompt from message history
    prompt = "\n".join([msg.content for msg in chat_history])
    result = llm.invoke(prompt)

    response = result.replace('<|user|>', '').replace('<|assistant|>', '').replace('</s>', '').strip()  
    chat_history.append(AIMessage(content=response))

    print("AI:", response)