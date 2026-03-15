import subprocess
from pathlib import Path

input = Path("sample_input.txt")
ans = Path("sample_output.txt") 
output = Path("my_answer.txt")
code = Path("sol.py")

result = subprocess.run(
    ["python", str(code)], # python sol.py
    stdin = open(input, "r"), # < sample_input.txt
    stdout = subprocess.PIPE, # > sample_output.txt
    text = True # in string format
)

output.write_text(result.stdout.strip() + "\n")

expected = ans.read_text().strip()
actual = result.stdout.strip()

if expected == actual:
    print("TRUE")
else:
    print("FALSE\n")
    print("expected:\n", expected)
    print("\nactual:\n", actual)