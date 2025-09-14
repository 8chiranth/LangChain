from langchain_huggingface import HuggingFacePipeline
import os
import streamlit as st

# Set cache path for HuggingFace
os.environ['HF_HOME'] = 'D:/huggingface_cache'

# UI header
st.header('🧠 Research Tool')

# Load HuggingFace model using pipeline
llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

# User input
user_input = st.text_input("Enter your prompt:")

# Handle button click
if st.button("Submit") and user_input:
    response = llm.invoke(user_input)
    st.subheader("Response:")
    st.write(response)
