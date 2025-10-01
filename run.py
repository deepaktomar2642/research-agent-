import argparse
from agent_core import research_topic

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", "-t", required=True, help="Research topic")
    args = parser.parse_args()

    out = research_topic(args.topic)
    print("\n\n===== RESEARCH REPORT =====\n")
    print(out["report"])
    print("\n\n===== SOURCES =====")
    for s in out["sources"]:
        print("-", s["title"], s["url"])

