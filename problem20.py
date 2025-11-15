
import string

# Read number of lines
n = int(input())

# List of filler words to remove
filler_words = ["very", "really", "quite", "extremely", "actually"]

# Initialize an empty string to store the final filtered text
filtered_text = ""

# Loop through each line of input
for _ in range(n):
    line = input()  # Read one line of review
    words = line.split()  # Split the line into words
    for word in words:
        # Remove punctuation from the word for comparison
        clean_word = word.strip(string.punctuation).lower()
        if clean_word not in filler_words:
            filtered_text += word + " "  # Add the word to the result if it's not a filler

# Remove extra space at the end and capitalize the first character
filtered_text = filtered_text.strip()
if filtered_text:
    filtered_text = filtered_text[0].upper() + filtered_text[1:]

# Print the cleaned-up review text
print(filtered_text)

# Count total words in the filtered text
total_words = filtered_text.split()
print(len(total_words))

# Count unique words (case-insensitive, punctuation removed)
unique_words = set()
for word in total_words:
    clean = word.strip(string.punctuation).lower()
    unique_words.add(clean)

print(len(unique_words))
