import re

def extract_errors(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        error_lines = []
        for line in lines:
            if re.search(r"(ERROR|Exception|FAIL|Traceback)", line, re.IGNORECASE):
                error_lines.append(line.strip())

        print(f"Extracted {len(error_lines)} error lines from the log.")
        return "\n".join(error_lines[:50]) or "No relevant errors found in the log."

    except FileNotFoundError:
        return f"Log file not found: {file_path}"
