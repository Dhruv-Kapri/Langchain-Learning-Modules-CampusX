from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

# xxxxxxxxxxxxxxxx--This dosen't work, langchain schenanigans--xxxxxxxxxxxxx
# chat_template = ChatPromptTemplate([
#     SystemMessage(content='You are a helpful {domain} expert'),
#     HumanMessage(content='Explain in simple terms, what is {topic}')
# ])

chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful {domain} expert"),
        ("human", "Explain in simple terms, what is {topic}"),
    ]
)

domain = "cricket"
topic = "Dusra"

prompt = chat_template.invoke({"domain": domain, "topic": topic})
print(prompt)


result = model.invoke(prompt)
print(result.content)
