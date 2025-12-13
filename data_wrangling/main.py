# # Loading real-world data -> inspect -> clean it -> fix it -> select the needed fields -> preparing it for our AI model

# # Pandas & DataFrame

# # Pandas is a Pythoin library for working with structured data
# # DataFrame is the main object in Pandas; it has columns & rows -> just like excel & SQL Table

# # DataFrame Advantages:
#     # 1. Filtering
#     # 2. Grouping
#     # 3. Cleaning
#     # 4. Statistics
#     # 5. Joining tables


# import pandas as pd

# df = pd.read_csv("data_wrangling/data/students.csv")
# # print(df)

# # Before cleaning, we need to inspect the file
# # print(df.head())
# # print(df.tail())
# # print(df.info())
# # print(df.describe())

# # This step (inspecting) tells us if the data is usable or broken

# # Cleaning Missing Values

# # Check for missing values
# # print(df.isnull())
# # print(df.isnull().sum())

# # df.fillna(0, inplace=True)
# # print(df.isnull().sum())
# df["math"].fillna(df["math"].mean(), inplace=True)
# df["english"].fillna(df["english"].mean(), inplace=True)
# # df.dropna(inplace=True)
# # print(df.head())
# # df.to_csv('students.csv')   # to export the last version of df

# # Cleaning messy text data

# df["name"] = df["name"].str.strip()
# df["name"] = df["name"].str.lower()
# # print(df.head())


# # Filtering Data

# math_high_scores = df[df["math"] > 70]
# english_high_scores = df[df["english"] > 80]
# # print(math_high_scores)
# # print(english_high_scores)

# filtered = df[(df["math"] > 70) & (df["english"] > 80)]
# print(filtered)

# # filtered = df["math"] > 70
# # print(df[filtered])

# # filtered = df[df["math"] > 70]
# # print(filtered)


# # Joining DataFrames (Merging)


import pandas as pd

students = pd.read_csv("data_wrangling/data/students.csv")
scores = pd.read_csv("data_wrangling/data/scores.csv")

merged = students.merge(scores, left_on="id", right_on="student_id")
# merged = pd.merge(students, scores, left_on="id", right_on="student_id")
print(merged)
