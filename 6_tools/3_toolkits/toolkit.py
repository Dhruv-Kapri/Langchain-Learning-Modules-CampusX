from langchain_core.tools import tool


# Custom tools
@tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


# Toolkit
class MathToolkit:
    def get_tools(self):
        return [add, multiply]


# Application
toolkit = MathToolkit()
tools = toolkit.get_tools()

for it in tools:
    print(it.name, "=>", it.description)
