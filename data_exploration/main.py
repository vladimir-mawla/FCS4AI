# EDA - Exploratory Data Analysis

# Understanding the data

import csv
import pandas as pd

df = pd.read_csv("data_exploration/students.csv")

# Inspecting

# To get the shape of the df

# print(df.shape)
# => (rows, columns)

# print(df.columns)

# print(df.dtypes)

# print(df.head())

# print(df.tail())


# Descriptive Stats

# print(df.describe())

# Value Counts

# age distribution

# print(df["age"].value_counts())

# name distribution

# print(df["name"].value_counts())

# => value_counts() shows us how common each value is


# Detecting Duplicates

# print(df.duplicated().sum)

# print(df.duplicated().sum())

# print(df[df.duplicated()])

# duplicates = df[df.duplicated(subset=["name"])]
# print(duplicates)

# test = df.drop_duplicates()

# print(test)

# Detecting missing Fields

# print(df.isnull().sum())

import matplotlib.pyplot as plt
# import seaborn as sns

# This heatmap shows us exactly which cells are missing

# sns.heatmap(df.isnull())
# plt.show()

# Outliers

# Boxplot => this graph shows us whether some scores are extremelly high/low compared to the rest

# print(df["math"].describe())

# plt.boxplot(df["math"].dropna())
# plt.title("Math Score Outliers")
# plt.show()


# Visualization for EDA (matplotlib) => histogram, scatter, line


# Histogram => Displays the frequency of some column

# df["age"].hist()
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.show()

# Scatter plot

# plt.scatter(df["math"], df["english"])
# plt.title("Math vs English Scores")
# plt.xlabel("Math")
# plt.ylabel("English")
# plt.show()

# Line plot

# df["math"].plot(kind="line")
# plt.title("Math Scores")
# plt.show()

# Model-ready Insights

# df["avg_score"] = df[["math", "english", "science"]].mean(axis=1)

# df["name"] =df["name"].str.lower()

# df["passed"] = df["avg_score"] >= 70

# print(df)

print(df["math"].describe())