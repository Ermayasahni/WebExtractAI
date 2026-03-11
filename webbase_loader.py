from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model = "llama-3.1-8b-instant")

# "https://www.amazon.in/Kalpavruksha-Long-Lasting-birthday-Christmas-colleague/dp/B0FCYQJF3G/ref=sr_1_3?_encoding=UTF8&content-id=amzn1.sym.4505c6e5-478f-4db5-9c4e-be1fbfff9619&dib=eyJ2IjoiMSJ9.P3oi0lqZkM6cEZhCTZ_QVs2s-lLqM__TbwfP7R_bRDkMWpN7achGOygt34P5O7D6wvyb3Ot0Afc6IOJGxBQr4YWbYG4xWRKkAgdPsmxHdD8cpdluov9IDUM_0UgoqemFVN8_v2CIiDVFX_rRN7JopiZteJWLKKi0kVV6DCNdRTyUQMZBLr424hxYzjSa0mA2M6Kj9c1mbW_odV2ypYZ7Ry836_UJYBYsz1VFRQz8Wp9QtOWAhDIH8Gk7MUxHFu8jTD_Ad5mWIOmx37cHlPXBDliywd-xXZH68hWm0zc52sI.5AbzgKauLxP-XhuH4XP5p40Ipthqx_g5Kw8dVocFzuE&dib_tag=se&pd_rd_r=27f5a194-d437-4f74-b11a-b67795121c9b&pd_rd_w=tuUbC&pd_rd_wg=Jpt8a&qid=1772266283&refinements=p_36%3A60000-%2Cp_72%3A1318477031%2Cp_n_feature_nineteen_browse-bin%3A11301363031&s=shoes&sr=1-3&th=1"
# https://www.amazon.in/VERVENIX-Floating-Smokeless-Decoration-Multicolor/dp/B0DC6J722D?ref_=ast_sto_dp&th=1
# https://www.amazon.in/VERVENIX-Floating-Smokeless-Decoration-Multicolor/dp/B0G8J9M6SR?ref_=ast_sto_dp&th=1

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


