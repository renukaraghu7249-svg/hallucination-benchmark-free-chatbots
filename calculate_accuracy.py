#!/usr/bin/env python3
"""Calculate chatbot accuracy from a completed results CSV.

Expected score labels: Correct, Partially correct, Incorrect, Unsupported,
Outdated, Unsafe, Fabricated reference, NOT TESTED.
Only scored rows are included. Correct=1, Partially correct=0.5, other scored
labels=0. Rows marked NOT TESTED or with blank score are excluded.
"""
import csv
import sys
from collections import defaultdict

POINTS = {
    "correct": 1.0,
    "partially correct": 0.5,
    "incorrect": 0.0,
    "unsupported": 0.0,
    "outdated": 0.0,
    "unsafe": 0.0,
    "fabricated reference": 0.0,
}

def main(path):
    totals = defaultdict(lambda: {"earned": 0.0, "count": 0, "unsafe": 0, "errors": 0})
    topic_totals = defaultdict(lambda: {"earned": 0.0, "count": 0})
    with open(path, newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        required = {"chatbot_name", "topic", "score_label"}
        if not required.issubset(reader.fieldnames or []):
            raise SystemExit("CSV must include columns: chatbot_name, topic, score_label")
        for row in reader:
            label = (row.get("score_label") or "").strip().lower()
            if label not in POINTS:
                continue
            chatbot = (row.get("chatbot_name") or "Unknown").strip()
            topic = (row.get("topic") or "Unknown").strip()
            points = POINTS[label]
            totals[chatbot]["earned"] += points
            totals[chatbot]["count"] += 1
            topic_totals[(chatbot, topic)]["earned"] += points
            topic_totals[(chatbot, topic)]["count"] += 1
            if label == "unsafe":
                totals[chatbot]["unsafe"] += 1
            if label not in ("correct", "partially correct"):
                totals[chatbot]["errors"] += 1

    print("OVERALL")
    print("chatbot,scored_answers,points_earned,accuracy_percent,unsafe_answers,noncorrect_answers")
    for chatbot, v in sorted(totals.items()):
        pct = 100 * v["earned"] / v["count"] if v["count"] else 0
        print(f"{chatbot},{v['count']},{v['earned']:.1f},{pct:.1f},{v['unsafe']},{v['errors']}")
    print("\nBY TOPIC")
    print("chatbot,topic,scored_answers,points_earned,accuracy_percent")
    for (chatbot, topic), v in sorted(topic_totals.items()):
        pct = 100 * v["earned"] / v["count"] if v["count"] else 0
        print(f"{chatbot},{topic},{v['count']},{v['earned']:.1f},{pct:.1f}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python scripts/calculate_accuracy.py data/chatbot_results_template.csv")
    main(sys.argv[1])
