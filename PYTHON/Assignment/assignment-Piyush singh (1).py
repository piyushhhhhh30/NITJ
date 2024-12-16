# Task 1: Fetch data from a specific URL and print it on screen
import requests

def fetch_data():
    url = "https://example.com"  # Replace with your desired URL
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

# Task 2: Compute the total size of all files in the current directory
import os

def compute_total_size():
    total_size = sum(os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f))
    print(f"Total size of all files: {total_size} bytes")

# Task 3: Copy a file line by line with line numbers
def copy_file_with_line_numbers():
    with open("source.txt", 'r') as src, open("destination.txt", 'w') as dest:
        for i, line in enumerate(src, start=1):
            dest.write(f"{i}: {line}")

# Task 4: Count tabs, spaces, and newlines in a file
def count_characters():
    with open("example.txt", 'r') as file:
        content = file.read()
        print(f"Tabs: {content.count('\\t')}, Spaces: {content.count(' ')}, Newlines: {content.count('\\n')}")

# Task 5: Calculate the percentage of vowels and consonants in a file
def calculate_vowel_consonant_percentage():
    vowels = "aeiouAEIOU"
    with open("example.txt", 'r') as file:
        text = file.read()
        total_chars = len(text)
        vowel_count = sum(1 for char in text if char in vowels)
        consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
        if total_chars > 0:
            print(f"Vowels: {vowel_count / total_chars:.2%}, Consonants: {consonant_count / total_chars:.2%}")
        else:
            print("File is empty.")

# Task 6: File access modes
def list_access_modes():
    print("""
    'r'  - Read mode (default). File must exist.
    'w'  - Write mode. Creates a new file or truncates an existing file.
    'a'  - Append mode. Writes data to the end of the file.
    'rb' - Read mode in binary.
    'wb' - Write mode in binary.
    'ab' - Append mode in binary.
    'r+' - Read and write mode. File must exist.
    'w+' - Write and read mode. Creates a new file or truncates an existing file.
    'a+' - Append and read mode. Writes to the end of the file.
    """)

# Task 7: Format text and save to a file
def format_text():
    text = "this is a test. it has numbers 123."
    formatted = ""
    capitalize = True
    for char in text:
        if char == '.':
            formatted += char
            capitalize = True
        elif char.isdigit():
            formatted += f"({char})"
        elif capitalize and char.isalpha():
            formatted += char.upper()
            capitalize = False
        else:
            formatted += char
    with open("formatted_output.txt", 'w') as file:
        file.write(formatted)
    print("Formatted text saved to formatted_output.txt")

# Task 8: Replace full stops with commas and save to a new file
def replace_full_stops():
    with open("source.txt", 'r') as src, open("destination_with_commas.txt", 'w') as dest:
        for line in src:
            dest.write(line.replace('.', ','))
    print("File copied with full stops replaced by commas.")

# Uncomment the function calls below to test
# fetch_data()
# compute_total_size()
# copy_file_with_line_numbers()
# count_characters()
# calculate_vowel_consonant_percentage()
# list_access_modes()
# format_text()
# replace_full_stops()
