# Sample dataset: Sentences from an AI Voice Log
data_logs = [
    "Artificial intelligence is transforming software engineering",
    "Python is the best language for data science tools",
    "Machine learning models require clean data pipelines",
    "I am learning python code to build an ai plotter project"
]

print("--- AI DATA LOG REPORT ---")
print(f"Total entries analyzed: {len(data_logs)}")

# Task: Count how many times keyword 'python' or 'ai' appears
ai_count = 0
python_count = 0

for log in data_logs:
    lower_log = log.lower()
    if "ai" in lower_log or "artificial" in lower_log:
        ai_count += 1
    if "python" in lower_log:
        python_count += 1

print(f"Entries mentioning AI: {ai_count}")
print(f"Entries mentioning Python: {python_count}")
