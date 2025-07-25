import os
import cohere
from dotenv import load_dotenv
from Backend.ragEngine import search_similar

load_dotenv()
cohere_api_key = os.getenv("COHERE_API_KEY")
cohere_client = cohere.Client(cohere_api_key)

def extract_errors(error_log):
    if not error_log.strip():
        return "No errors found in the log."

    # Search similar past logs
    similar_examples = search_similar(error_log)
    similar_logs = "\n".join([
        f"[Similar Case #{i+1}]\nLog: {ex['log']}\nFix: {ex['fix']}"
        for i, ex in enumerate(similar_examples)
    ])

    prompt = f"""
    You are an expert DevOps engineer.
    Analyze this error log and suggest a fix.

    [Current Log]
    {error_log}

    [Similar Past Logs]
    {similar_logs}

    Explain:
    1. Root Cause
    2. Suggested Fix
    3. How to avoid it in the future
    """

    response = cohere_client.generate(
        model="command-r-plus",
        prompt=prompt,
        max_tokens=350,
        temperature=0.3,
    )
    return response.generations[0].text.strip() if response.generations else "No suggestion generated."
