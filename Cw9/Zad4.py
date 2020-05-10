import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df = pd.read_csv("iris.data", sep=",", names=["Sepal length", "Sepal width", "Petal length", "Petal width", "Class"])

se = df[df["Class"] == "Iris-setosa"]
ve = df[df["Class"] == "Iris-versicolor"]
vi = df[df["Class"] == "Iris-virginica"]

setosa = plt.scatter(se["Petal length"], se["Petal width"], color="r")
versicolor = plt.scatter(ve["Petal length"], ve["Petal width"], color="b")
virginica = plt.scatter(vi["Petal length"], vi["Petal width"], color="y")

plt.ylabel("Petal length")
plt.xlabel("Petal width")
plt.legend((setosa, versicolor, virginica), ("Iris-setosa", "Iris-versicolor", "Iris-virginica"), title="Classes")

plt.show()