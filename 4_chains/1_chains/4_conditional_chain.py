from typing import Literal

from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")


class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Give the sentiment of the feedback"
    )


parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)


# -------- Classifier --------
prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into postive or negative \n feedback: {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser2.get_format_instructions()},
)

classifier_chain = prompt1 | model | parser2

# -------- Response Prompts --------
prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=["feedback"],
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=["feedback"],
)

# -------- Branch --------
branch_chain = RunnableBranch(
    # (condition, chain),
    (lambda x: x["sentiment"] == "positive", prompt2 | model | parser),
    (lambda x: x["sentiment"] == "negative", prompt3 | model | parser),
    RunnableLambda(lambda _: "Could not find sentiment"),
)

# -------- Glue sentiment + original input --------
#                               ┌─ sentiment==postive → prompt2 -> model
# feedback -> classifier_chain ─┤
#                               └─ sentiment==negative → prompt3 -> model
chain = (
    RunnableLambda(
        lambda inputs: {"feedback": inputs["feeldback"], "sentiment": classifier_chain}
    )
    | branch_chain
)

result = chain.invoke({"feedback": "This is a beautiful phone"})
print(result)

chain.get_graph().print_ascii()
