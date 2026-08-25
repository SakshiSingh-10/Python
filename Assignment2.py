import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Semester": [
        "Semester 1",
        "Semester 2",
        "Semester 3",
        "Semester 4",
        "Semester 5",
        "Semester 6"
    ],

    "Python": [72, 75, 78, 80, 84, 88],
    "Java": [68, 72, 75, 78, 82, 85],
    "DBMS": [70, 74, 79, 81, 85, 89],
    "Data Structures": [65, 70, 76, 79, 83, 87],
    "Computer Networks": [60, 68, 72, 77, 81, 86]
}

df = pd.DataFrame(data)

print("DATASET")
print(df)
number_of_semesters = df["Semester"].nunique()

print("\n2. Number of semesters:", number_of_semesters)
subjects = df.columns[1:]
number_of_subjects = len(subjects)

print("\n3. Total number of subjects:", number_of_subjects)
highest_marks = df[subjects].max().max()

print("\n4. Highest marks:", highest_marks)
lowest_marks = df[subjects].min().min()

print("\n5. Lowest marks:", lowest_marks)

semester_total = df[subjects].sum(axis=1)

highest_total_index = semester_total.idxmax()

print("\n6. Semester with highest total marks:",
      df.loc[highest_total_index, "Semester"])

print("Highest total marks:", semester_total.max())
lowest_total_index = semester_total.idxmin()

print("\n7. Semester with lowest total marks:",
      df.loc[lowest_total_index, "Semester"])

print("Lowest total marks:", semester_total.min())
print("\n8. First five records:")
print(df.head())
semester_average = df[subjects].mean(axis=1)

print("\n9. Average marks for each semester:")

for i in range(len(df)):
    print(df.loc[i, "Semester"], ":", semester_average[i])

plt.figure(figsize=(8, 5))

plt.plot(
    df["Semester"],
    semester_average,
    marker="o"
)

plt.title("Semester-wise Average Marks")
plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.axhline(y=75, linestyle="--", label="Target = 75%")
plt.legend()
plt.grid(True)

plt.show()
subject_average = df[subjects].mean()

print("\n11. Subject-wise average marks:")
print(subject_average)

plt.figure(figsize=(9, 5))

plt.bar(
    subject_average.index,
    subject_average.values
)

plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.xticks(rotation=30)
plt.axhline(y=75, linestyle="--", label="Target = 75%")
plt.legend()

plt.show()

highest_subject = subject_average.idxmax()
highest_subject_marks = subject_average.max()

print("\n12. Highest-performing subject:",
      highest_subject)

print("Average marks:",
      highest_subject_marks)
lowest_subject = subject_average.idxmin()
lowest_subject_marks = subject_average.min()

print("\n13. Lowest-performing subject:",
      lowest_subject)

print("Average marks:",
      lowest_subject_marks)

best_semester = df.loc[semester_average.idxmax(), "Semester"]
worst_semester = df.loc[semester_average.idxmin(), "Semester"]

print("\n14. Best semester:", best_semester)
print("Worst semester:", worst_semester)


semester_1_average = semester_average.iloc[0]
semester_6_average = semester_average.iloc[-1]

improvement = semester_6_average - semester_1_average

print("\n15. Improvement between Semester 1 and Semester 6:",
      improvement, "marks")


# Improvement percentage
improvement_percentage = (
    improvement / semester_1_average
) * 100

print("Improvement percentage:",
      round(improvement_percentage, 2), "%")
all_marks = df[subjects].values.flatten()

mean = np.mean(all_marks)
median = np.median(all_marks)
maximum = np.max(all_marks)
minimum = np.min(all_marks)
standard_deviation = np.std(all_marks)

print("\n16. NumPy Statistics")

print("Mean:", round(mean, 2))
print("Median:", median)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Standard Deviation:", round(standard_deviation, 2))
plt.figure(figsize=(10, 6))

for subject in subjects:
    plt.plot(
        df["Semester"],
        df[subject],
        marker="o",
        label=subject
    )

plt.title("Subject Performance Across Six Semesters")
plt.xlabel("Semester")
plt.ylabel("Marks")
plt.axhline(
    y=75,
    linestyle="--",
    label="Target = 75%"
)

plt.legend()
plt.grid(True)

plt.show()
plt.figure(figsize=(9, 5))

plt.plot(
    df["Semester"],
    semester_average,
    marker="o",
    label="My Average"
)

plt.axhline(
    y=75,
    linestyle="--",
    label="Academic Target = 75%"
)

plt.title("My Performance vs Academic Target")
plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.legend()
plt.grid(True)

plt.show()
class_average = [70, 72, 74, 76, 78, 80]

print("\n19. My Average vs Class Average")

comparison = pd.DataFrame({
    "Semester": df["Semester"],
    "My Average": semester_average,
    "Class Average": class_average
})

print(comparison)

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

axes[0, 0].plot(
    df["Semester"],
    semester_average,
    marker="o"
)

axes[0, 0].axhline(
    y=75,
    linestyle="--",
    label="Target = 75%"
)

axes[0, 0].set_title("Figure 1: Semester-wise Average")
axes[0, 0].set_xlabel("Semester")
axes[0, 0].set_ylabel("Average Marks")
axes[0, 0].legend()
axes[0, 0].grid(True)

axes[0, 1].bar(
    subject_average.index,
    subject_average.values
)

axes[0, 1].axhline(
    y=75,
    linestyle="--",
    label="Target = 75%"
)

axes[0, 1].set_title("Figure 2: Subject-wise Average")
axes[0, 1].set_xlabel("Subject")
axes[0, 1].set_ylabel("Average Marks")
axes[0, 1].tick_params(axis="x", rotation=30)
axes[0, 1].legend()

axes[1, 0].bar(
    df["Semester"],
    semester_total
)

axes[1, 0].set_title("Figure 3: Semester-wise Total")
axes[1, 0].set_xlabel("Semester")
axes[1, 0].set_ylabel("Total Marks")


axes[1, 1].plot(
    df["Semester"],
    semester_average,
    marker="o",
    label="My Average"
)

axes[1, 1].plot(
    df["Semester"],
    class_average,
    marker="o",
    label="Class Average"
)

axes[1, 1].set_title("Figure 4: My Performance vs Class Average")
axes[1, 1].set_xlabel("Semester")
axes[1, 1].set_ylabel("Average Marks")
axes[1, 1].legend()
axes[1, 1].grid(True)

plt.tight_layout()
plt.show()

print("\n21. FIVE OBSERVATIONS")

print("1. My average marks generally increased from Semester 1 to Semester 6.")

print("2. Semester 6 is my best-performing semester based on average marks.")

print("3. Python is my highest-performing subject based on overall average marks.")

print("4. Computer Networks has the lowest overall average among the subjects.")

print("5. My performance in the later semesters is higher than my performance in the earlier semesters.")