import os
import requests
from bs4 import BeautifulSoup
from readability import Document
from dotenv import load_dotenv

load_dotenv()

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
SEARCH_BACKEND = os.getenv("SEARCH_BACKEND", "serpapi").lower()

def search_web(query, num=5):
    if SEARCH_BACKEND == "serpapi":
        from serpapi import GoogleSearch
        params = {"q": query, "engine": "google", "num": num, "api_key": SERPAPI_API_KEY}
        search = GoogleSearch(params)
        res = search.get_dict()
        return [{"title": r.get("title"), "link": r.get("link"), "snippet": r.get("snippet")} 
                for r in res.get("organic_results", [])[:num]]
    else:
        raise NotImplementedError("Only SerpAPI backend implemented")

def fetch_page_text(url, timeout=10):
    try:
        r = requests.get(url, timeout=timeout, headers={"User-Agent":"Mozilla/5.0"})
        doc = Document(r.text)
        soup = BeautifulSoup(doc.summary(), "html.parser")
        text = soup.get_text(separator="\n").strip()
        return text if len(text) > 200 else BeautifulSoup(r.text, "html.parser").get_text(separator="\n").strip()
    except Exception as e:
        return f"[fetch_error] {e}"
