from typing import Annotated, Literal, Optional, TypedDict

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")


# TypedDict Schema -1
class Review(TypedDict):
    # -------v1----------
    # summary: str
    # sentiment: str

    # -------v2----------
    summary: Annotated[str, "A breif sumary of the review"]
    sentiment: Annotated[
        str, "Return sentiment of the Review either negative, positive, neutral"
    ]


structured_model = model.with_structured_output(Review)
result = structured_model.invoke(
    """
    The hardware is great, but the software feels bloated. There are way too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.
    """
)

# ----------------------------------------------------------
# TypedDict Schema -2


class Review(TypedDict):
    key_themes: Annotated[
        list[str], "Write down all the key themes discussed int the review in a list"
    ]
    summary: Annotated[str, "A breif sumary of the review"]
    sentiment: Annotated[
        Literal["pos", "neg"],
        "Return sentiment of the Review either negative, positive",
    ]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[str, "Write the name of the reviewer"]


structured_model = model.with_structured_output(Review)
result = structured_model.invoke(
    """
    I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

    The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

    However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

    Pros:
    Insanely powerful processor (great for gaming and productivity)
    Stunning 200MP camera with incredible zoom capabilities
    Long battery life with fast charging
    S-Pen support is unique and useful
                                    
    Review by Aman
    """
)

# ----------------------------------------------------------

print(result)
print(type(result))
print(result["summary"])
print(result["summary"])
