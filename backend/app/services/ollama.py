import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def parse_task(text: str):
    prompt = f"""
Extract task details and return JSON with:
- title
- due_date (ISO or null)
- priority (Low, Medium, High)

Input:
{text}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]
