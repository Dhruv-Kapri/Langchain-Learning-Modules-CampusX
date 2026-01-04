from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
    RunnableSequence,
)
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def word_count(text):
    return len(text.split())


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
parser = StrOutputParser()


prompt = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)


joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel(
    {"joke": RunnablePassthrough(), "word_count": RunnableLambda(word_count)}
)

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = parallel_chain.invoke({"topic": "AI"})
final_result = f"Joke: {result['joke']} \n Word count: {result['word_count']}"

print(final_result)
