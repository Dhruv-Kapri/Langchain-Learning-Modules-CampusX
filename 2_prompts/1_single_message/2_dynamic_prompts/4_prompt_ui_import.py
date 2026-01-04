from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

project_root = Path(__file__).parents[3]
curr_path = project_root / "prompts" / "1_single_message" / "2_dynamic_prompts"


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
prompt_template = load_prompt(curr_path / "3_prompt_template.json")

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
    # -------Option 1--------------
    prompt = prompt_template.invoke(
        {
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input,
        }
    )
    st.write(prompt)
    result = model.invoke(prompt)

    # -----------Option 2--------
    chain = prompt_template | model
    result_1 = chain.invoke(
        {
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input,
        }
    )

    # ---------------------------

    st.write(result.content)
    st.write(result.content)
