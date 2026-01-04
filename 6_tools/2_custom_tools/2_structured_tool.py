from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


class MultiplyInput(BaseModel):
    a: int = Field(description="The first number to multiply")
    b: int = Field(description="The second number to multiply")


def multiply_func(a: int, b: int) -> int:
    return a * b


multiply_tool = StructuredTool.from_function(
    func=multiply_func,
    name="multiply",
    description="Multiply two numbers",
    args_schema=MultiplyInput,
)


result = multiply_tool.invoke({"a": 3, "b": 10})
print(result)

print("--------------")
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)

print("--------------")
print(multiply_tool.args_schema.model_json_schema())
