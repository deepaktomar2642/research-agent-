import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1, api_key=OPENAI_API_KEY)

def summarize_text(title, url, text):
    system = SystemMessage(content="You are a research assistant. Summarize this article concisely.")
    human = HumanMessage(content=f"Title: {title}\nURL: {url}\n{text}")
    resp = llm([system, human])
    return resp.content

def synthesize_report(topic, summaries):
    system = SystemMessage(content="You are a senior analyst. Produce a well-structured research report.")
    sources_text = "\n\n".join([f"Title: {s['title']}\nURL: {s['url']}\nSummary:\n{s['summary']}" for s in summaries])
    human = HumanMessage(content=f"Write a research report on: {topic}\nUse the following sources:\n{sources_text}")
    resp = llm([system, human], max_tokens=1000)
    return resp.content
