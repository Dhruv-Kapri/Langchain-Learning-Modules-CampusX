from pathlib import Path

from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template
chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful customer support agent"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{querry}"),
    ]
)


# load chat history
project_root = Path(__file__).parents[3]
curr_path = project_root / "2_prompts" / "2_multi_message" / "2_dynamic_prompts"

chat_history = []
with open(curr_path / "chat_history.txt") as f:
    chat_history.append(f.readlines())

print(chat_history)


# create prompt
prompt = chat_template.invoke(
    {"chat_history": chat_history, "querry": HumanMessage(content="")}
)

print(prompt)
print(prompt)
