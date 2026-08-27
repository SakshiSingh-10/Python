import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



data = {
    "District": [
        "East", "North East-I", "North", "North West A",
        "North West B-I", "West A", "West B", "South West A",
        "South West B-I", "South", "New Delhi", "Central",
        "South East", "North East-II", "North West B-II",
        "South West B-II"
    ],

    "Schools": [
        121, 48, 65, 117, 84, 59, 84, 39,
        50, 70, 3, 40, 100, 85, 48, 48
    ],

    "Students": [
        189406, 126931, 77396, 180388,
        142549, 82889, 175104, 47082,
        79706, 110108, 1295, 27641,
        177374, 142510, 67574, 38967
    ],

    "Boys": [
        89786, 59362, 37652, 86906,
        70946, 38918, 84550, 23274,
        39019, 52249, 668, 11920,
        85167, 66679, 33835, 18905
    ],

    "Girls": [
        99620, 67569, 39744, 93482,
        71603, 43971, 90554, 23808,
        40687, 57859, 627, 15721,
        92207, 75831, 33739, 20062
    ],

    "Class_X_Pass": [
        93.09, 89.32, 91.55, 98.32,
        92.61, 96.54, 94.34, 97.55,
        94.80, 95.95, 94.19, 97.30,
        94.01, 92.31, 98.58, 98.25
    ],

    "Class_XII_Pass": [
        95.76, 94.06, 96.74, 98.43,
        97.09, 98.40, 98.30, 98.59,
        99.09, 97.35, 95.09, 95.96,
        96.78, 95.06, 99.23, 99.51
    ]
}

df = pd.DataFrame(data)

print("\n========== DATASET ==========")
print(df)


highest_school = df.loc[df["Schools"].idxmax()]
lowest_school = df.loc[df["Schools"].idxmin()]

print("\nQ1. Highest number of schools:")
print(highest_school["District"], highest_school["Schools"])

print("Lowest number of schools:")
print(lowest_school["District"], lowest_school["Schools"])



highest_students = df.loc[df["Students"].idxmax()]

print("\nQ2. Highest total student enrollment:")
print(
    highest_students["District"],
    highest_students["Students"]
)

df["Gender Difference"] = (
    df["Boys"] - df["Girls"]
).abs()

largest_gender_difference = df.loc[
    df["Gender Difference"].idxmax()
]

print("\nQ3. Largest gender difference:")

print(
    largest_gender_difference["District"]
)

print(
    "Difference:",
    largest_gender_difference["Gender Difference"]
)


highest_class_x = df.loc[
    df["Class_X_Pass"].idxmax()
]

print("\nQ4. Highest Class X pass percentage:")

print(
    highest_class_x["District"],
    highest_class_x["Class_X_Pass"],
    "%"
)

highest_class_xii = df.loc[
    df["Class_XII_Pass"].idxmax()
]

print("\nQ5. Highest Class XII pass percentage:")

print(
    highest_class_xii["District"],
    highest_class_xii["Class_XII_Pass"],
    "%"
)

print("\nQ6. Class X vs Class XII:")

comparison = df[
    ["District", "Class_X_Pass", "Class_XII_Pass"]
]

print(comparison)

print(
    "\nAverage Class X Pass Percentage:",
    round(df["Class_X_Pass"].mean(), 2)
)

print(
    "Average Class XII Pass Percentage:",
    round(df["Class_XII_Pass"].mean(), 2)
)
school_correlation = df["Schools"].corr(
    df["Class_X_Pass"]
)

print("\nQ7. Correlation between schools and Class X pass:")
print(round(school_correlation, 2))

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Schools"],
    df["Class_X_Pass"]
)

plt.xlabel("Number of Schools")
plt.ylabel("Class X Pass Percentage")

plt.title(
    "Schools vs Class X Pass Percentage"
)

plt.grid(True)

plt.show()

student_correlation = df["Students"].corr(
    df["Class_X_Pass"]
)

print("\nQ8. Correlation between students and Class X pass:")
print(round(student_correlation, 2))

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Students"],
    df["Class_X_Pass"]
)

plt.xlabel("Total Students")
plt.ylabel("Class X Pass Percentage")

plt.title(
    "Student Enrollment vs Class X Pass Percentage"
)

plt.grid(True)

plt.show()


df["Students Per School"] = (
    df["Students"] / df["Schools"]
)

highest_students_per_school = df.loc[
    df["Students Per School"].idxmax()
]

print("\nQ9. Highest students per school:")

print(
    highest_students_per_school["District"]
)

print(
    round(
        highest_students_per_school["Students Per School"],
        2
    )
)

# Correlation
students_school_correlation = df[
    "Students Per School"
].corr(
    df["Class_X_Pass"]
)

print(
    "Correlation with Class X performance:",
    round(students_school_correlation, 2)
)

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Students Per School"],
    df["Class_X_Pass"]
)

plt.xlabel("Students Per School")
plt.ylabel("Class X Pass Percentage")

plt.title(
    "Students Per School vs Class X Pass Percentage"
)

plt.grid(True)

plt.show()


print("\nQ10. THREE IMPORTANT OBSERVATIONS")

print(
    "1. Class XII has a higher average pass percentage "
    "than Class X."
)

print(
    "2. The number of schools does not strongly determine "
    "Class X pass percentage."
)

print(
    "3. Higher students per school tends to be associated "
    "with lower Class X pass percentage in this dataset."
)

plt.figure(figsize=(12, 6))

x = np.arange(len(df))

width = 0.35

plt.bar(
    x - width / 2,
    df["Class_X_Pass"],
    width,
    label="Class X"
)

plt.bar(
    x + width / 2,
    df["Class_XII_Pass"],
    width,
    label="Class XII"
)

plt.xlabel("District")

plt.ylabel("Pass Percentage")

plt.title(
    "Class X vs Class XII Pass Percentage"
)

plt.xticks(
    x,
    df["District"],
    rotation=90
)

plt.legend()

plt.tight_layout()

plt.show()