from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


# tool create
@tool
def multiply(a: int, b: int) -> int:
    """Given 2 numbers a and b this tool returns their product"""
    return a * b


# Tool Binding
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
llm_with_tools = llm.bind_tools([multiply])


query = HumanMessage("can you multiply 3 with 1000")
messages: list = [query]
result = llm_with_tools.invoke(messages)
messages.append(result)


print("tool_calls => ", result.tool_calls)
print("--------------")

tool_result = multiply.invoke(result.tool_calls[0])
messages.append(tool_result)

print("messages => ", messages)
print("--------------")

final_result = llm_with_tools.invoke(messages).content
print("final result => ", final_result)
