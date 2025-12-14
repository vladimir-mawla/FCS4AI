# Text Processing

# Tokenization => means taking a long string of text and breaking
# it into smaller units called tokens

text = "     Hello, my name   is John Doe, and I am learning Python since 2 years"
# tokens = text.split()

# print(tokens)

# Output: ['Hello,', 'my', 'name', 'is', 'John', 'Doe,', 'and', 'I', 'am', 'learning', 'Python']

# Normalization

import re

text = text.lower()

# remove trailing/leading spaces
text = text.strip()

# print(text)

# Regular Expressions (Regex) for text cleaning.
# regex, are patterns that let us search or replace text in a flexible way
# instead of saying "replace this exact word", we can say "replace any sequence that looks like an email"

# \s => whitespace (opposite) \S
# \d => digits
# \w => letter, digit or underscore
# [^...] => NOT these chars
# + => one and more occurence
# * => zero and more occurences
# ? => optional



text = re.sub(r"[^a-z\d\s]", "", text) # => remove anything that isn't a letter, number or space
# print(text)

# text = re.sub()

# text = "ID: 1023, Code: 0, Ref: 7"
# result = re.findall(r"\d+", text)
# print(result)

# text = "color colour colouur colouuur colr"
# result = re.findall(r"colou*r", text)
# print(result)

# Remove URLs

# text = "check this out: https://example.com and http://test.com"

# result = re.sub(r"https?://\S+", "", text)
# token = text.split()

# print(text)

# stopwords

stopwards = ["the", "a", "an", "my", "is", "i", "and", "am"]

filtered_tokens = []

# for t in token:
#     if t not in stopwards:
#         filtered_tokens.append(t)

# print(filtered_tokens)

# print(text)
# text = re.sub(r"\s+", " ", text)
# print(text)


# Chunking => means splitting a long document into smaller pieces


doc = """
John is a student who loves Python and AI.
He is taking an FCS4AI course.

Joe is interested in data science
He uses Pandas and Matplotlib

Alaa wants to focus on backend
"""

# paragraph-based chunking

raw_paragraphs = doc.split("\n\n")
# print(raw_paragraphs)

paragraphs = []

for p in raw_paragraphs:
    cleaned = p.strip()
    if cleaned != "":
        paragraphs.append(cleaned)

count = 1
# for p in paragraphs:
#     print("Chunk", count)
#     print(p)
#     print("-------------------")
#     count += 1


# word-based chunking

def chunk_by_words(text, max_words=40):
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_words):
        chunk_words = words[i:i+max_words]
        chunks.append(" ".join(chunk_words))
    return chunks

print(chunk_by_words(doc, 7))


# overlapping chunks

def sliding_window_chunks(text, window_size=50, overlap=10):
    words = text.split()
    chunks = []
    step = window_size - overlap
    for i in range(0, len(words), step):
        chunk_words = words[i:i+window_size]
        chunks.append(" ".join(chunk_words))
        if i + window_size >= len(words):
            break
    return chunks

print(sliding_window_chunks(doc, 7, 2))