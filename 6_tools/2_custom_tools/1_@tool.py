from langchain_core.tools import tool

# # Step 1 - create a function
# def multiply(a, b):
#     """Multiply 2 numbers"""
#     return a*b


# # Step 2 - add type hints
# def multiply(a: int, b: int) -> int:
#     """Multiply 2 numbers"""
#     return a*b


# Step 3 - add tool decorator
@tool
def multiply(a: int, b: int) -> int:
    """Multiply 2 numbers"""
    return a * b


result = multiply.invoke({"a": 3, "b": 10})
print(result)

print("--------------")
print(multiply.name)
print(multiply.description)
print(multiply.args)

print("--------------")
print(multiply.args_schema.model_json_schema())
