import json
from pathlib import Path
from categorize import categorize_email
from ai_response import generate_reply
from summary import write_summary

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "sample_emails.json"

def load_emails(path=DATA_FILE):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def process_emails(emails):
    results = []
    for e in emails:
        category = categorize_email(e)
        reply = generate_reply(e)
        results.append({
            "id": e.get("id"),
            "from": e.get("from"),
            "subject": e.get("subject"),
            "category": category,
            "reply_draft": reply
        })
    return results

def save_results(results, out_path="results.json"):
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to {out_path}")

def main():
    emails = load_emails()
    results = process_emails(emails)
    save_results(results)
    write_summary(results)

if __name__ == "__main__":
    main()
