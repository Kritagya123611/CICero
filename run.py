from Backend.errorExtract import extract_errors
from Backend.LLMsol import get_fix_suggestion

if __name__ == "__main__":
    log_path = "SampleLog/FailedBuild.log"

    print("🔍 Extracting errors...")
    error_text = extract_errors(log_path)
    print("\n--- Extracted Errors ---\n")
    print(error_text)

    print("\n🤖 Generating fix suggestion using Cohere...")
    suggestion = get_fix_suggestion(error_text)
    print("\n--- Suggested Fix ---\n")
    print(suggestion)
