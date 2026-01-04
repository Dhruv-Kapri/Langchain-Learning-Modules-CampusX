from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableSequence,
)
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
parser = StrOutputParser()


prompt1 = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Explain the following joke - {text}", input_variables=["text"]
)


joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "explanation": RunnableSequence(prompt2, model, parser),
    }
)

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = parallel_chain.invoke({"topic": "AI"})

print(result["tweet"])
print(result["linkedin"])
print(result["linkedin"])
