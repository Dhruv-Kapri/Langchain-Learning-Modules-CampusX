import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# from langchain_openai import ChatOpenAI
# from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

load_dotenv()

# -------------Model Definition-------------
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

# ----------------------------------
# llm = HuggingFacePipeline.from_model_id(
#     model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
#     task='text-generation',
#     pipeline_kwargs=dict(
#         temperature=0.5,
#         max_new_tokens=100,
#     ),
# )
# model = ChatHuggingFace(llm=llm)

# ---------Alternative Model---------
# model = ChatOpenAI(model='gpt-4')

# ----------------------------------


st.header("Reasearch Tool")
user_input = st.text_input("Enter your prompt")
if st.button("Summarize"):
    result = model.invoke(user_input)
    st.write(result.content)
    st.write(result.content)
