from typing import Type

from langchain.tools import BaseTool
from pydantic import BaseModel, Field


# arg schema using pydantic
class MultiplyInput(BaseModel):
    a: int = Field(description="The first number to add")
    b: int = Field(description="The second number to add")


class MultiplyTool(BaseTool):
    name: str = "Multiply"
    description: str = "Multiply 3 numbers"

    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a * b


multiply_tool = MultiplyTool()


result = multiply_tool.invoke({"a": 3, "b": 3})
print(result)

print("--------------")
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)
