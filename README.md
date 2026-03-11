🌐 WebExtractAI

WebExtractAI is a web content extraction tool that parses e-commerce webpages using BeautifulSoup (bs4) to extract product prices.
It optionally leverages LangChain and Groq Llama-3.1-8B for AI-powered extraction, providing fast, structured price information through a Streamlit frontend and FastAPI backend.

🚀 Features

        🌐 Webpage Content Loader – Load product pages from URLs
        
        🧹 BeautifulSoup (bs4) – Parse and clean HTML content
        
        💰 Price Extraction – Extract product prices accurately
        
        ⚡ FastAPI Backend – Efficient API for processing requests
        
        🖥️ Streamlit Frontend – Interactive, user-friendly interface
        
        🤖 Optional AI Assistance – LangChain + Groq LLM for complex extraction

🛠️ Tech Stack
    Technology	Usage

        Python	Core programming language
        
        Streamlit	Frontend web interface
        
        FastAPI	Backend API
        
        BeautifulSoup (bs4)	HTML parsing and cleaning
        
        LangChain	LLM orchestration (optional)
        
        Groq Llama-3.1-8B	AI-based price extraction (optional)
        
        Requests	API communication
        
        dotenv	Environment variable management
        
📂 Project Structure

        WebExtractAI/
        │
        ├── app.py              # Streamlit frontend
        
        ├── api.py              # FastAPI backend
        
        ├── extractor.py        # Web scraping & AI extraction logic
        
        ├── requirements.txt    # Dependencies
        
        ├── .env                # API keys (optional for Groq)
        
        └── README.md           # Documentation

🔄 Processing Pipeline

Product URL
     │
     ▼
WebBaseLoader
(load webpage)
     │
     ▼
BeautifulSoup
(clean HTML)
     │
     ▼
PromptTemplate (optional)
(format AI instructions)
     │
     ▼
ChatGroq (optional LLM)
(extract price)
     │
     ▼
StrOutputParser (optional)
(clean output)
     │
     ▼
Extracted Product Price

🔗 API Endpoint


Endpoint	Method	Description


/extract-price	POST	Extracts product price from a URL

Example Request
{
 "url": "https://www.amazon.in/product-url"
}

Example Response
{
 "price": "₹1,299"
}
