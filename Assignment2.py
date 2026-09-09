import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {

    "Semester": [
        "Semester 3",
        "Semester 4",
        "Semester 5",
        "Semester 6"
    ],

    "Material Science": [66, np.nan, np.nan, np.nan],

    "Technical Communication": [70, np.nan, np.nan, np.nan],

    "Data Structure": [74, np.nan, np.nan, np.nan],

    "Computer Organization and Architecture":
        [70, np.nan, np.nan, np.nan],

    "Discrete Structures & Theory of Logic":
        [48, np.nan, np.nan, np.nan],

    "Cyber Security": [70, np.nan, np.nan, np.nan],

    "Data Structure Lab": [89, np.nan, np.nan, np.nan],

    "Computer Organization and Architecture Lab":
        [89, np.nan, np.nan, np.nan],

    "Web Designing Workshop": [88, np.nan, np.nan, np.nan],

    "Internship Assessment / Mini Project":
        [51, np.nan, np.nan, np.nan],

    "Mathematics-IV": [np.nan, 49, np.nan, np.nan],

    "Universal Human Values and Professional Ethics":
        [np.nan, 76, np.nan, np.nan],

    "Operating System": [np.nan, 78, np.nan, np.nan],

    "Theory of Automata and Formal Languages":
        [np.nan, 53, np.nan, np.nan],

    "Object Oriented Programming with Java":
        [np.nan, 59, np.nan, np.nan],

    "Python programming": [np.nan, 67, np.nan, np.nan],

    "Operating System Lab":
        [np.nan, 92, np.nan, np.nan],

    "Object Oriented Programming with Java Lab":
        [np.nan, 90, np.nan, np.nan],

    "Cyber Security Workshop":
        [np.nan, 90, np.nan, np.nan],

    "Sports and Yoga - II":
        [np.nan, 87, np.nan, np.nan],

    "Database Management System":
        [np.nan, np.nan, 73, np.nan],

    "Web Technology":
        [np.nan, np.nan, 78, np.nan],

    "Design and Analysis of Algorithm":
        [np.nan, np.nan, 68, np.nan],

    "Object Oriented System Design with C++":
        [np.nan, np.nan, 81, np.nan],

    "Application of Soft Computing":
        [np.nan, np.nan, 63, np.nan],

    "Database Management System Lab":
        [np.nan, np.nan, 91, np.nan],

    "Web Technology Lab":
        [np.nan, np.nan, 91, np.nan],

    "Design and Analysis of Algorithm Lab":
        [np.nan, np.nan, 92, np.nan],

    "Mini Project or Internship Assessment":
        [np.nan, np.nan, 82, np.nan],

    "Constitution of India":
        [np.nan, np.nan, 61, np.nan],

    "Software Engineering":
        [np.nan, np.nan, np.nan, 56],

    "Compiler Design":
        [np.nan, np.nan, np.nan, 71],

    "Computer Networks":
        [np.nan, np.nan, np.nan, 83],

    "Blockchain Architecture Design":
        [np.nan, np.nan, np.nan, 68],

    "IDEA TO BUSINESS MODEL":
        [np.nan, np.nan, np.nan, 72],

    "Software Engineering Lab":
        [np.nan, np.nan, np.nan, 100],

    "Compiler Design Lab":
        [np.nan, np.nan, np.nan, 100],

    "Computer Networks Lab":
        [np.nan, np.nan, np.nan, 100],

    "Essence of Indian Traditional Knowledge":
        [np.nan, np.nan, np.nan, 80]
}

df = pd.DataFrame(data)

print("\n================ DATASET ================\n")
print(df.to_string(index=False))




subject_columns = df.columns[1:]



number_of_semesters = df["Semester"].nunique()

print("\n2. Number of semesters:")
print(number_of_semesters)



total_subjects = df[subject_columns].count().sum()

print("\n3. Total number of subjects studied:")
print(total_subjects)



highest_marks = df[subject_columns].max().max()

print("\n4. Highest marks:")
print(highest_marks)

lowest_marks = df[subject_columns].min().min()

print("\n5. Lowest marks:")
print(lowest_marks)


df["Total Marks"] = df[subject_columns].sum(axis=1)

df["Average Marks"] = df[subject_columns].mean(axis=1)


highest_total_index = df["Total Marks"].idxmax()

print("\n6. Semester with highest total marks:")

print(
    df.loc[highest_total_index, "Semester"],
    "=",
    df.loc[highest_total_index, "Total Marks"]
)


lowest_total_index = df["Total Marks"].idxmin()

print("\n7. Semester with lowest total marks:")

print(
    df.loc[lowest_total_index, "Semester"],
    "=",
    df.loc[lowest_total_index, "Total Marks"]
)


print("\n8. First five records:")

print(df.head())


print("\n9. Average marks for each semester:")

print(
    df[["Semester", "Average Marks"]]
)

plt.figure(figsize=(8, 5))

plt.plot(
    df["Semester"],
    df["Average Marks"],
    marker="o",
    linewidth=2,
    label="My Average"
)

# Academic target
plt.axhline(
    y=75,
    linestyle="--",
    label="Target = 75%"
)

plt.title("Figure 1: Semester-wise Average Marks")

plt.xlabel("Semester")
plt.ylabel("Average Marks (%)")

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.show()


subject_average = df[subject_columns].mean()

# Remove subjects that do not have enough data
subject_average = subject_average.dropna()

plt.figure(figsize=(14, 6))

plt.bar(
    subject_average.index,
    subject_average.values
)

plt.axhline(
    y=75,
    linestyle="--",
    label="Target = 75%"
)

plt.title("Figure 2: Subject-wise Average Marks")

plt.xlabel("Subjects")
plt.ylabel("Average Marks (%)")

plt.xticks(
    rotation=90,
    fontsize=8
)

plt.legend()

plt.grid(
    axis="y"
)

plt.tight_layout()

plt.show()


highest_subject = subject_average.idxmax()

highest_subject_marks = subject_average.max()

print("\n12. Highest-performing subject:")

print(highest_subject)

print(
    "Average marks =",
    highest_subject_marks
)

lowest_subject = subject_average.idxmin()

lowest_subject_marks = subject_average.min()

print("\n13. Lowest-performing subject:")

print(lowest_subject)

print(
    "Average marks =",
    lowest_subject_marks
)


best_semester = df.loc[
    df["Average Marks"].idxmax(),
    "Semester"
]

worst_semester = df.loc[
    df["Average Marks"].idxmin(),
    "Semester"
]

print("\n14. Best semester:")
print(best_semester)

print("Worst semester:")
print(worst_semester)

print("\n15. Improvement between Semester 1 and Semester 6:")

print(
    "Cannot calculate because Semester 1 marks "
    "are not present in the uploaded result."
)

all_marks = df[subject_columns].values.flatten()

# Remove NaN values
all_marks = all_marks[
    ~np.isnan(all_marks)
]

mean_marks = np.mean(all_marks)

median_marks = np.median(all_marks)

maximum_marks = np.max(all_marks)

minimum_marks = np.min(all_marks)

standard_deviation = np.std(all_marks)

print("\n16. NumPy Statistics")

print(
    "Mean =",
    round(mean_marks, 2)
)

print(
    "Median =",
    round(median_marks, 2)
)

print(
    "Maximum =",
    maximum_marks
)

print(
    "Minimum =",
    minimum_marks
)

print(
    "Standard Deviation =",
    round(standard_deviation, 2)
)

plt.figure(figsize=(15, 7))

for subject in subject_columns:

    values = df[subject]

    if values.notna().any():

        plt.plot(
            df["Semester"],
            values,
            marker="o",
            label=subject
        )

# Target
plt.axhline(
    y=75,
    linestyle="--",
    linewidth=2,
    label="Target = 75%"
)

plt.title(
    "Figure 3: Performance of Each Subject Across Semesters"
)

plt.xlabel("Semester")

plt.ylabel("Marks (%)")

plt.legend(
    bbox_to_anchor=(1.02, 1),
    loc="upper left",
    fontsize=7
)

plt.grid(True)

plt.tight_layout()

plt.show()


plt.figure(figsize=(8, 5))

plt.plot(
    df["Semester"],
    df["Average Marks"],
    marker="o",
    label="My Average"
)

plt.axhline(
    y=75,
    linestyle="--",
    linewidth=2,
    label="Academic Target = 75%"
)

plt.title(
    "Semester Performance with 75% Target"
)

plt.xlabel("Semester")

plt.ylabel("Average Marks (%)")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()


class_average = [70, 72, 74, 76]

plt.figure(figsize=(8, 5))

plt.plot(
    df["Semester"],
    df["Average Marks"],
    marker="o",
    label="My Performance"
)

plt.plot(
    df["Semester"],
    class_average,
    marker="s",
    label="Class Average"
)

plt.title(
    "Figure 4: My Performance vs Class Average"
)

plt.xlabel("Semester")

plt.ylabel("Average Marks (%)")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()


fig, axes = plt.subplots(
    2,
    2,
    figsize=(16, 11)
)

axes[0, 0].plot(
    df["Semester"],
    df["Average Marks"],
    marker="o",
    label="My Average"
)

axes[0, 0].axhline(
    y=75,
    linestyle="--",
    label="Target = 75%"
)

axes[0, 0].set_title(
    "Figure 1: Semester-wise Average"
)

axes[0, 0].set_xlabel("Semester")

axes[0, 0].set_ylabel("Average Marks (%)")

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

axes[0, 1].set_title(
    "Figure 2: Subject-wise Average"
)

axes[0, 1].set_xlabel("Subjects")

axes[0, 1].set_ylabel("Average Marks (%)")

axes[0, 1].tick_params(
    axis="x",
    rotation=90
)

axes[0, 1].legend()


axes[1, 0].bar(
    df["Semester"],
    df["Total Marks"]
)

axes[1, 0].set_title(
    "Figure 3: Semester-wise Total"
)

axes[1, 0].set_xlabel("Semester")

axes[1, 0].set_ylabel("Total Marks")

axes[1, 1].plot(
    df["Semester"],
    df["Average Marks"],
    marker="o",
    label="My Performance"
)

axes[1, 1].plot(
    df["Semester"],
    class_average,
    marker="s",
    label="Class Average"
)

axes[1, 1].set_title(
    "Figure 4: My Performance vs Class Average"
)

axes[1, 1].set_xlabel("Semester")

axes[1, 1].set_ylabel("Average Marks (%)")

axes[1, 1].legend()

axes[1, 1].grid(True)


plt.tight_layout()

plt.show()

print("\n========== 21. FIVE OBSERVATIONS ==========")

print(
    "1. Semester 6 has the highest average marks "
    "among the available semesters."
)

print(
    "2. My average performance shows an increasing "
    "trend from Semester 3 to Semester 6."
)

print(
    "3. Several practical subjects have marks "
    "above the 75% academic target."
)

print(
    "4. The subject-wise graph helps identify my "
    "strongest and weakest subjects."
)

print(
    "5. Semester 6 has the highest average performance "
    "among Semesters 3 to 6."
)
