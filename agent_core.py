from tools import search_web, fetch_page_text
from summarizer import summarize_text, synthesize_report

def research_topic(topic, num_queries=3, results_per_query=3):
    queries = [topic, f"{topic} overview", f"{topic} latest research"]
    all_results = []
    for q in queries:
        try:
            all_results.extend(search_web(q, num=results_per_query))
        except Exception as e:
            print("Search error:", e)
    # dedupe
    seen = set()
    urls = []
    link_map = {}
    for r in all_results:
        link = r.get("link")
        if link and link not in seen:
            seen.add(link)
            urls.append(link)
            link_map[link] = r

    # fetch pages
    fetched = {}
    for u in urls:
        fetched[u] = fetch_page_text(u)

    # summarize
    summaries = []
    for url, text in fetched.items():
        summaries.append({
            "title": link_map[url]["title"],
            "url": url,
            "summary": summarize_text(link_map[url]["title"], url, text)
        })

    # synthesize report
    report = synthesize_report(topic, summaries)
    return {"topic": topic, "report": report, "sources": summaries}
