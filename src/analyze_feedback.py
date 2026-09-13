from pathlib import Path
import re
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "feedback.csv"

POSITIVE = {"easy", "saves", "quickly", "clearly", "helpful", "easier", "useful"}
NEGATIVE = {"slowly", "freezes", "confusing", "errors", "improvement", "issue"}
THEMES = {
    "Usability": ["easy", "easier", "confusing", "setup"],
    "Performance": ["slow", "slowly", "freezes", "errors"],
    "Support": ["support", "resolved", "helpful", "fix"],
    "Billing": ["billing", "invoice"],
    "Feature Request": ["add", "export", "excel"],
}


def words(text: str) -> set[str]:
    return set(re.findall(r"[a-z]+", text.lower()))


def classify_sentiment(text: str) -> str:
    tokens = words(text)
    score = len(tokens & POSITIVE) - len(tokens & NEGATIVE)
    return "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"


def detect_theme(text: str) -> str:
    lower = text.lower()
    for theme, keywords in THEMES.items():
        if any(keyword in lower for keyword in keywords):
            return theme
    return "Other"


def main() -> None:
    df = pd.read_csv(INPUT)
    df["sentiment"] = df["comment"].map(classify_sentiment)
    df["theme"] = df["comment"].map(detect_theme)

    print("Customer Feedback Summary")
    print("=" * 26)
    print("\nSentiment:")
    print(df["sentiment"].value_counts().to_string())
    print("\nThemes:")
    print(df["theme"].value_counts().to_string())
    print("\nDetailed results:")
    print(df[["feedback_id", "sentiment", "theme", "comment"]].to_string(index=False))


if __name__ == "__main__":
    main()
