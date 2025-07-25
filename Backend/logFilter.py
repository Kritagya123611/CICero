import re

# Accepts log lines as list[str]
def keyword_filter(log_lines):
    error_lines = []
    for line in log_lines:
        if re.search(r"(ERROR|Exception|FAIL|Traceback)", line, re.IGNORECASE):
            error_lines.append(line.strip())
    return error_lines[:50] or ["No relevant errors found in the log."]

def tail_filter(log_lines, tail_length=50):
    return [line.strip() for line in log_lines[-tail_length:]]

def diff_filter(failed_lines, success_lines):
    failed_set = set(line.strip() for line in failed_lines)
    success_set = set(line.strip() for line in success_lines)
    diff_lines = list(failed_set - success_set)
    return diff_lines[:50] or ["No differences found between failed and successful logs."]
