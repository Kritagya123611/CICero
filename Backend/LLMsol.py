import os
import cohere
from dotenv import load_dotenv

load_dotenv()
cohere_api_key = os.getenv("COHERE_API_KEY")
cohere_client = cohere.Client(cohere_api_key)

def get_fix_suggestion(error_log):
    if not error_log.strip():
        return "No errors found in the log."

    prompt = f"""You are an expert DevOps engineer. Analyze the following CI/CD error log:
1. Identify the root cause of failure.
2. Suggest a fix.
3. Recommend how to prevent this in future.

=== LOG START ===
{error_log}
=== LOG END ===
"""

    try:
        response = cohere_client.generate(
            model="command-r-plus",
            prompt=prompt,
            max_tokens=300,
            temperature=0.3,
        )

        if response.generations:
            return response.generations[0].text.strip()
        else:
            return "No response generated from Cohere."

    except Exception as e:
        return f"Error from Cohere API: {str(e)}"
