import json
from datetime import datetime

def write_summary(results, out_path="summary.json"):
    summary = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "total_emails": len(results),
        "by_category": {}
    }
    for r in results:
        cat = r.get("category")
        summary["by_category"].setdefault(cat, 0)
        summary["by_category"][cat] += 1
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(f"Summary written to {out_path}")
