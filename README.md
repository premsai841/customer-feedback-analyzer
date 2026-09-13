# Customer Feedback Analyzer

> A lightweight feedback-processing workflow for categorizing customer comments, detecting sentiment, and surfacing recurring themes.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)

## Purpose

Customer feedback is valuable only when recurring patterns can be turned into action. This project demonstrates a simple, explainable approach to organizing qualitative feedback into sentiment groups and operational themes.

## Workflow

```text
Feedback CSV
    ↓
Text normalization
    ↓
Keyword-based sentiment classification
    ↓
Theme detection
    ↓
Summary of recurring customer issues
```

## Themes

The demo identifies common themes such as:

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

## Run

```bash
pip install -r requirements.txt
python src/analyze_feedback.py
```

## Scope

The classifier is intentionally transparent and uses synthetic feedback. It is a portfolio demonstration, not a production sentiment model.

## Author

**Prem Sai Bachchala** — Customer Success / Customer Experience analytics portfolio project.
