# Email AI Automation Agent

An AI-powered automation agent that reads sample emails, categorizes them, generates reply drafts (optional via OpenAI/local LLM), and produces a daily summary.

## Features
- Read sample emails from JSON
- Simple keyword-based categorization + optional AI refine
- Generate reply drafts (OpenAI or local model optional)
- Output daily summary.json

## Tech Stack
- Python 3.9+
- Optional: OpenAI API (for nicer replies)

## Quick Start
1. Clone the repo.
2. (Optional) Create `.env` with `OPENAI_API_KEY`.
3. Install dependencies:
