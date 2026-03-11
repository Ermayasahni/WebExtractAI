from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model = "llama-3.1-8b-instant")

prompt = PromptTemplate(
                        template="Extract the product price from the following webpage content Kalpavruksha-Long-Lasting-birthday-Christmas-colleague:\n\n{input}",
                        input_variables=["input"]
                        )

parser = StrOutputParser()                                                                                          

chains = prompt | model | parser


def extractprice_url(url: str) -> str:
    loader = WebBaseLoader(url)
    docs = loader.load()
    page_content = docs[0].page_content

    result = chains.invoke({"input": page_content})
    return result



