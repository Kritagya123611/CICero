from Backend.logFilter import keyword_filter, tail_filter, diff_filter

with open("SampleLog/FailedBuild.log", "r", encoding="utf-8") as f:
    failed_log = f.readlines()

try:
    with open("SampleLog/SuccessBuild.log", "r", encoding="utf-8") as f:
        success_log = f.readlines()
except FileNotFoundError:
    success_log = []

# Apply log filtering
k_errors = keyword_filter(failed_log)
tail_errors = tail_filter(failed_log)
diff_errors = diff_filter(failed_log, success_log) if success_log else []

# Combine all results
final_log = "\n".join(k_errors + tail_errors + diff_errors)

print("\n--- Filtered Error Log ---\n")
print(final_log)
