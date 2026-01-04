import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

prompt_template = PromptTemplate(
    template="""
    Please summarize the research paper titled "{paper_input}" with the following specifications:
    Explanation Style: {style_input}  
    Explanation Length: {length_input}  
    1. Mathematical Details:  
    - Include relevant mathematical equations if present in the paper.  
    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
    2. Analogies:  
    - Use relatable analogies to simplify complex ideas.  
    If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
    Ensure the summary is clear, accurate, and aligned with the provided style and length.
    """,
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True,
)

# -------------------------------

st.header("Reasearch Tool")
paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis",
    ],
)
style_input = st.selectbox(
    "Select Explaination Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"],
)
length_input = st.selectbox(
    "Select Explaination Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)",
    ],
)


if st.button("Summarize"):
    prompt = prompt_template.invoke(
        {
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input,
        }
    )
    result = model.invoke(prompt)
    st.write(result.content)
