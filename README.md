# research-agent-
Research Agent: Searches Google, summarizes findings, and creates a report.

# 🔎 Research Agent (LangChain + Google/SerpAPI)

A Python-based **AI Research Agent** that:
- Searches Google (via **SerpAPI** or **Google Custom Search**)
- Fetches and extracts text from top result pages
- Summarizes each article using an LLM
- Synthesizes a **final structured research report** (executive summary, aggregated findings, source list)

---

## 📦 Features
- Automated **query expansion** (topic + variants)
- Flexible search backend: **SerpAPI** (default) or **Google CSE**
- Content extraction with `readability` and BeautifulSoup
- Summaries with **OpenAI GPT models**
- Full research report in **Markdown** format
- CLI runner (`run.py`) for easy use

---

## 🛠 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/yourname/research-agent.git
cd research-agent
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
pip install -r requirements.txt

