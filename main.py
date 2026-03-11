from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from .webbase_loader import extractprice_url

app = FastAPI(title="Product Price Extractor API")


class URLRequest(BaseModel):
    url: HttpUrl


class PriceResponse(BaseModel):
    price: str


@app.get("/")
def root():
    return {"message": "API working"}

@app.post("/extract-price")
def extract_price(request: URLRequest):
        price = extractprice_url(str(request.url))
        return PriceResponse(price=price)

