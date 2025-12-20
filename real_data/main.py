# collect -> clean -> chunk -> store -> retrieve

# Part A - Working with Real Data

# 1. HTTP Request - JSONPlaceholder

import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
# print("Status code:", response.status_code)

data = response.json() # The API sends JSON. Python converts it into a list of dictionaries
# print("Type:", type(data))
# print("First item:", data[0])


# 2. Parse JSON into a DataFrame

import pandas as pd

df = pd.DataFrame(data)
# print(df.head())
# print(df.shape)
# print(df.columns)

# 3. Convert Rows into Documents for AI

documents = []

# df.iterrows() => is a Pandas method, that iterates DF one row at a time, and returns 2 values (index, row)
# (0, row_data)
# (1, row_data)
# (2, row_data)

for _, row in df.iterrows():
    doc = f"Post #{row['id']} (user {row['userId']}: {row['title']}. {row['body']})"
    documents.append(doc)

# 4. Basic Web Scraping When No API Exists

# import requests
# from bs4 import BeautifulSoup

# url = "https://sefactory.io"
# html = requests.get(url).text

# soup = BeautifulSoup(html, "html.parser")
# title = soup.find("h1").get_text(strip=True)

# print("Scraped title:", title)



# Part B - Chunking

# 1. Normalization, Tokenization, Stopwords

import re

def normalize(text):
    text = text.lower()
    text = text.strip()
    text = re.sub(r"[^a-z\d\s]", "", text)
    return text

def tokenize(text):
    return text.split()

stopwards = ["the", "a", "an", "my", "is", "i", "and", "am", "are", "was", "were", "of", "in", "on", "he", "who"]

def remove_stopwords(tokens):
    filtered = []
    for t in tokens:
        if t not in stopwards:
            filtered.append(t)
    return filtered


raw_text = """
John is a student who loves Python and AI.
He is taking an FCS4AI course.

Joe is interested in data science
He uses Pandas and Matplotlib

Alaa wants to focus on backend
"""

clean = normalize(raw_text)
tokens = tokenize(clean)
filtered_tokens = remove_stopwords(tokens)

# print("Clean text:", clean)
# print("Tokens:", tokens)
# print("Filtered Tokens:", filtered_tokens)

# 2. Chunking => splitting large text/documents into smaller pieces (which ai models can work with more effectively)

def chunk_words(tokens, chunk_size=8):
    chunks = []
    current = []

    for t in tokens:
        current.append(t)
        if len(current) == chunk_size:
            chunks.append(current)
            current = []

    if len(current) > 0:
        chunks.append(current)

    return chunks
    

chunks = chunk_words(filtered_tokens, chunk_size=8)
# print(filtered_tokens)
# for i in range(len(chunks)):
#     print("Chunk", i + 1, ":", chunks[i])

# 3. Apply the Pipeline to Real API Data

all_chunks = []

for doc_id in range(len(documents)):
    clean_doc = normalize(documents[doc_id])
    tokens = tokenize(clean_doc)
    filtered = remove_stopwords(tokens)

    chunks = chunk_words(filtered, chunk_size=40)

    for c in chunks:
        all_chunks.append({
            "source": "jsonplaceholder_posts",
            "doc_id": doc_id + 1,
            "chunk_text": " ".join(c)
        })

# print(all_chunks)


# C - Prompt Engineering -> clarity

# elements: role, task, constraints, context, output format

context = all_chunks[0]["chunk_text"]

bad_prompt = f"Summarize this: {context}"

good_prompt = f"""
You are an assistant

Task: Summarize the text in 2 bullet points.

Rules:
- Use simple words.
- Do not invent details

Text: {context}
"""


# D - Databases (SQLite)


import sqlite3

conn = sqlite3.connect("chunks.db")

cursor = conn.cursor()

cursor.execute("""
              CREATE TABLE IF NOT EXISTS chunks (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               source TEXT,
               doc_id INTEGER,
               chunk_text TEXT
               )
               """)

conn.commit()
print("Database and table ready")

# insert chunks into the db table

for item in all_chunks:
    cursor.execute(
        "INSERT INTO CHUNKS (source, doc_id, chunk_text) VALUES (?, ?, ?)",
        (item["source"], item["doc_id"], item["chunk_text"])
    )

conn.commit()
# print("Inserted chunks:", len(all_chunks))

# select from db table (search)

keyword = "blanditiis"

cursor.execute(

    "SELECT * FROM chunks WHERE chunk_text LIKE ? LIMIT 5",
    (f"%{keyword}%",)
)

results = cursor.fetchall()
# print(results)
# print("Search results:")

# for result in results:
#     print("Chunk ID:", result[0], " | Doc:", result[2])
#     print(result[3])
#     print("----------")

# Update and Delete

cursor.execute(

    "UPDATE chunks SET source = ? WHERE source = ?",
    ("posts_v2", "posts")
)

conn.commit()

# cursor.execute(

#     "SELECT * FROM chunks LIMIT 1"
# )
# results = cursor.fetchall()
print("Updated source names")
# print(results)

# Delete

cursor.execute(

    "DELETE FROM chunks WHERE id = ?",
    (3,)
)
conn.commit()
print("Deleted chunk with id = 1")

cursor.execute(

    "SELECT * FROM chunks WHERE id = 3"
)
results = cursor.fetchone()
print(results)

conn.close()


user_input = "1=1"
sql = "DELETE FROM chunks WHERE id = ?", (user_input)