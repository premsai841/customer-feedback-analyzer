# Customer Feedback Analyzer

> A lightweight Customer Experience portfolio project for organizing customer comments, identifying recurring themes, and turning qualitative feedback into structured insight.

## Career context

This project supports my Customer Success direction. It reflects the importance of listening to customers, identifying recurring service or product friction, and translating feedback into improvement opportunities.

## Business problem

Customer feedback is useful only when recurring patterns can be identified and communicated clearly. This project demonstrates a simple, explainable workflow for grouping feedback by sentiment and operational theme.

## Workflow

```text
Customer feedback
    ↓
Text normalization
    ↓
Keyword-based sentiment classification
    ↓
Theme detection
    ↓
Recurring issue summary
    ↓
Customer-experience insight
```

## Themes

The demo identifies themes such as:

- Product usability
- Performance
- Support experience
- Billing
- Feature requests

## Structure

```text
customer-feedback-analyzer/
├── data/feedback.csv
├── src/analyze_feedback.py
├── requirements.txt
└── README.md
```

## Run locally

```bash
pip install -r requirements.txt
python src/analyze_feedback.py
```

## Technical learning

The implementation uses basic Python and Pandas concepts as learning tools. The main focus is the Customer Experience workflow: organizing feedback, finding patterns, and producing a useful summary.

## Important limitation

The classifier is intentionally transparent and uses synthetic feedback. It is a portfolio demonstration, not a production-grade sentiment-analysis system.

## Author

**Prem Sai Bachchala** — Customer Success / Customer Experience / Support portfolio.
