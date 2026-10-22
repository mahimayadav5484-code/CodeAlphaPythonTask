import re
import os
input_file = "sample_text.txt"
output_file = "extracted_emails.txt"
if not os.path.exists(input_file):
    with open(input_file, "w") as f:
        f.write("Hello team,\n")
        f.write("Please contact john.doe@gmail.com or jane_smith@yahoo.com for details.\n")
        f.write("You can also write to services@codealpha.tech.\n")
        f.write("Duplicate: john.doe@gmail.com\n")
    print("Sample file created:", input_file)
try:
    with open(input_file, "r") as file:
        text = file.read()
except FileNotFoundError:
    print("Error: input file not found.")
    exit()
pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
emails = re.findall(pattern, text)
unique_emails = []
for email in emails:
    if email not in unique_emails:
        unique_emails.append(email)
with open(output_file, "w") as file:
    for email in unique_emails:
        file.write(email + "\n")
print("Found", len(unique_emails), "unique email address(es):")
for email in unique_emails:
    print(" -", email)
print("Saved to", output_file)