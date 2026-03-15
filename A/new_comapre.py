import subprocess
from pathlib import Path
import difflib
import time

# Files
input_file = Path("sample_input.txt")
expected_file = Path("sample_output.txt")
output_file = Path("my_answer.txt")
code = Path("sol.py")

# Colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Run solution
start = time.time()

result = subprocess.run(
    ["python", str(code)],
    stdin=open(input_file, "r"),
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

end = time.time()
runtime = end - start

actual_output = result.stdout.strip()
expected_output = expected_file.read_text().strip()

# Save program output
output_file.write_text(actual_output + "\n")

expected_lines = expected_output.splitlines()
actual_lines = actual_output.splitlines()

print("\n================ RESULT ================\n")

if expected_output == actual_output:
    print(f"{GREEN}✔ Output matches expected output{RESET}")
else:
    print(f"{RED}✘ Output does NOT match expected output{RESET}\n")

    # Check line by line
    max_len = max(len(expected_lines), len(actual_lines))

    for i in range(max_len):
        e = expected_lines[i] if i < len(expected_lines) else "<NO LINE>"
        a = actual_lines[i] if i < len(actual_lines) else "<NO LINE>"

        if e != a:
            print(f"{YELLOW}First mismatch at line {i+1}:{RESET}")
            print(f"{GREEN}Expected:{RESET} {e}")
            print(f"{RED}Actual  :{RESET} {a}\n")
            break

    # Show full diff
    print("------- Diff (expected vs actual) -------\n")

    diff = difflib.ndiff(expected_lines, actual_lines)

    for line in diff:
        if line.startswith("- "):
            print(f"{GREEN}{line}{RESET}")
        elif line.startswith("+ "):
            print(f"{RED}{line}{RESET}")

# Line count check
if len(expected_lines) != len(actual_lines):
    print(f"\n{YELLOW}Line count mismatch:{RESET}")
    print(f"Expected lines: {len(expected_lines)}")
    print(f"Actual lines  : {len(actual_lines)}")

# Execution time
print(f"\nExecution time: {runtime:.4f} seconds")

print("\n========================================\n")