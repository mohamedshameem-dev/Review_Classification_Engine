# 🤖 Review Classification Engine

Batch-optimized LLM-based automated customer review classification and sentiment detection engine using Ollama + Llama3.

---

## 📌 Problem

Ecommerce platforms receive thousands of customer reviews daily.

Manually reading and categorizing them into:
- Delivery Issues
- Payment Issues
- Product Quality
- Refund Problems

is inefficient and time-consuming.

---

## 🚀 Solution

This project implements a batch-optimized LLM pipeline that:

- Loads customer reviews from CSV
- Processes reviews in batches
- Classifies review category
- Detects sentiment (Positive / Neutral / Negative)
- Returns structured JSON output
- Handles parsing safely
- Includes error handling

---

## 🛠 Tech Stack

- Python
- Pandas
- Ollama
- Llama3
- Batch Prompt Engineering
- JSON Parsing

---

## ⚙️ How It Works

1. Reviews are loaded from CSV
2. Reviews are grouped into batches (default: 10 per call)
3. Llama3 processes multiple reviews in a single API call
4. Output is strictly enforced in JSON format
5. Safe JSON extraction prevents crashes
6. Errors are handled gracefully

---

## 📦 Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Make sure Ollama is installed and running:

```bash
ollama run llama3
```

---

## ▶️ Run the Script

```bash
python llm_review_batch_analyzer.py
```

---

## 📊 Example Output

```json
[
  {"review_number": 1, "category": "Delivery Issue", "sentiment": "Negative"},
  {"review_number": 2, "category": "Payment Issue", "sentiment": "Negative"}
]
```

---

## 🔥 Performance Optimization

Instead of making 1 API call per review:

Old Approach:
30 reviews = 30 API calls ❌

New Batch Approach:
30 reviews = 3 API calls ✅

- Reduced latency
- Reduced token usage
- Scalable architecture

---

## 📌 Future Enhancements

- Negative sentiment alert threshold
- Save output to CSV
- Real-time dashboard integration
- Deploy as REST API

## follow me for more interesting contents
