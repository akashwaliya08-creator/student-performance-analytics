import pandas as pd
import numpy as np


def load_data(file_name):
    try:
        data = pd.read_csv(file_name)
        return data
    except FileNotFoundError:
        print("\nERROR: students.csv file was not found.")
        print("Make sure students.csv is in the same folder as main.py.")
        return None
    except Exception as error:
        print("\nERROR while loading the dataset:")
        print(error)
        return None


def validate_data(data):
    required_columns = [
        "Student_ID",
        "Name",
        "Department",
        "Python",
        "NumPy",
        "Pandas",
        "Attendance"
    ]

    for column in required_columns:
        if column not in data.columns:
            print(f"\nERROR: Required column '{column}' is missing.")
            return False

    if data[required_columns].isnull().any().any():
        print("\nERROR: Dataset contains missing values.")
        return False

    subject_columns = ["Python", "NumPy", "Pandas"]

    for subject in subject_columns:
        if not pd.api.types.is_numeric_dtype(data[subject]):
            print(f"\nERROR: {subject} marks must be numeric.")
            return False

        if ((data[subject] < 0) | (data[subject] > 100)).any():
            print(f"\nERROR: {subject} marks must be between 0 and 100.")
            return False

    if not pd.api.types.is_numeric_dtype(data["Attendance"]):
        print("\nERROR: Attendance must be numeric.")
        return False

    if ((data["Attendance"] < 0) | (data["Attendance"] > 100)).any():
        print("\nERROR: Attendance must be between 0 and 100.")
        return False

    return True


def calculate_total_marks(data, subjects):
    marks_array = data[subjects].to_numpy()
    total_marks = np.sum(marks_array, axis=1)
    return total_marks


def calculate_average_marks(data, subjects):
    marks_array = data[subjects].to_numpy()
    average_marks = np.mean(marks_array, axis=1)
    return average_marks


def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


def determine_result(row, subjects):
    for subject in subjects:
        if row[subject] < 40:
            return "Fail"

    if row["Attendance"] < 75:
        return "Fail"

    return "Pass"


def calculate_subject_averages(data, subjects):
    subject_averages = {}

    for subject in subjects:
        subject_averages[subject] = np.mean(data[subject].to_numpy())

    return subject_averages


def find_highest_performer(data):
    highest_index = data["Average_Marks"].idxmax()
    return data.loc[highest_index]


def find_lowest_performer(data):
    lowest_index = data["Average_Marks"].idxmin()
    return data.loc[lowest_index]


def find_top_performers(data, number_of_students=3):
    top_students = data.sort_values(
        by="Average_Marks",
        ascending=False
    ).head(number_of_students)

    return top_students


def calculate_class_average(data):
    class_average = np.mean(data["Average_Marks"].to_numpy())
    return class_average


def find_best_subject(subject_averages):
    best_subject = max(
        subject_averages,
        key=subject_averages.get
    )

    return best_subject


def display_dataset_information(data):
    print("\n" + "=" * 70)
    print("DATASET INFORMATION")
    print("=" * 70)

    print(f"Number of Students : {len(data)}")
    print(f"Number of Columns  : {len(data.columns)}")

    print("\nColumns:")

    for column in data.columns:
        print(f"- {column}")

    print("\nFirst 5 Records:")
    print(data.head().to_string(index=False))


def display_performance_summary(data):
    print("\n" + "=" * 70)
    print("STUDENT PERFORMANCE SUMMARY")
    print("=" * 70)

    summary_columns = [
        "Student_ID",
        "Name",
        "Department",
        "Total_Marks",
        "Average_Marks",
        "Grade",
        "Result"
    ]

    summary = data[summary_columns].copy()

    summary["Average_Marks"] = summary["Average_Marks"].round(2)

    print(summary.to_string(index=False))


def display_subject_analysis(data, subjects):
    subject_averages = calculate_subject_averages(
        data,
        subjects
    )

    print("\n" + "=" * 70)
    print("SUBJECT-WISE PERFORMANCE ANALYSIS")
    print("=" * 70)

    for subject, average in subject_averages.items():
        print(f"{subject:<15}: {average:.2f}")

    best_subject = find_best_subject(subject_averages)

    print("\nBest Performing Subject:")
    print(
        f"{best_subject} "
        f"with average marks of "
        f"{subject_averages[best_subject]:.2f}"
    )

    return subject_averages


def display_top_performers(data):
    top_students = find_top_performers(data, 3)

    print("\n" + "=" * 70)
    print("TOP 3 PERFORMING STUDENTS")
    print("=" * 70)

    for position, (_, student) in enumerate(
        top_students.iterrows(),
        start=1
    ):
        print(
            f"{position}. "
            f"{student['Name']} "
            f"({student['Student_ID']}) - "
            f"Average: {student['Average_Marks']:.2f} - "
            f"Grade: {student['Grade']}"
        )


def display_highest_lowest(data):
    highest = find_highest_performer(data)
    lowest = find_lowest_performer(data)

    print("\n" + "=" * 70)
    print("HIGHEST AND LOWEST PERFORMANCE")
    print("=" * 70)

    print("\nHighest Performing Student:")
    print(f"Student ID : {highest['Student_ID']}")
    print(f"Name       : {highest['Name']}")
    print(f"Average    : {highest['Average_Marks']:.2f}")
    print(f"Grade      : {highest['Grade']}")

    print("\nLowest Performing Student:")
    print(f"Student ID : {lowest['Student_ID']}")
    print(f"Name       : {lowest['Name']}")
    print(f"Average    : {lowest['Average_Marks']:.2f}")
    print(f"Grade      : {lowest['Grade']}")


def display_pass_fail_statistics(data):
    passed_students = data[
        data["Result"] == "Pass"
    ]

    failed_students = data[
        data["Result"] == "Fail"
    ]

    pass_count = len(passed_students)
    fail_count = len(failed_students)

    total_students = len(data)

    pass_percentage = (
        pass_count / total_students
    ) * 100

    fail_percentage = (
        fail_count / total_students
    ) * 100

    print("\n" + "=" * 70)
    print("PASS / FAIL STATISTICS")
    print("=" * 70)

    print(f"Total Students   : {total_students}")
    print(f"Passed Students  : {pass_count}")
    print(f"Failed Students  : {fail_count}")
    print(f"Pass Percentage  : {pass_percentage:.2f}%")
    print(f"Fail Percentage  : {fail_percentage:.2f}%")


def display_class_average(data):
    class_average = calculate_class_average(data)

    print("\n" + "=" * 70)
    print("OVERALL CLASS PERFORMANCE")
    print("=" * 70)

    print(f"Overall Class Average: {class_average:.2f}")


def display_attendance_analysis(data):
    average_attendance = np.mean(
        data["Attendance"].to_numpy()
    )

    highest_attendance_index = data[
        "Attendance"
    ].idxmax()

    lowest_attendance_index = data[
        "Attendance"
    ].idxmin()

    highest_attendance_student = data.loc[
        highest_attendance_index
    ]

    lowest_attendance_student = data.loc[
        lowest_attendance_index
    ]

    print("\n" + "=" * 70)
    print("ATTENDANCE ANALYSIS")
    print("=" * 70)

    print(
        f"Average Attendance: "
        f"{average_attendance:.2f}%"
    )

    print(
        f"Highest Attendance: "
        f"{highest_attendance_student['Name']} "
        f"({highest_attendance_student['Attendance']:.0f}%)"
    )

    print(
        f"Lowest Attendance: "
        f"{lowest_attendance_student['Name']} "
        f"({lowest_attendance_student['Attendance']:.0f}%)"
    )


def main():

    print("\n")
    print("=" * 70)
    print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 70)
    print("EWB Courses | Python with AI Project")
    print("=" * 70)

    file_name = "students.csv"

    subjects = [
        "Python",
        "NumPy",
        "Pandas"
    ]

    data = load_data(file_name)

    if data is None:
        return

    if not validate_data(data):
        print("\nPlease correct the dataset and run the program again.")
        return

    print("\nDataset loaded successfully.")

    display_dataset_information(data)

    data["Total_Marks"] = calculate_total_marks(
        data,
        subjects
    )

    data["Average_Marks"] = calculate_average_marks(
        data,
        subjects
    )

    grades = []

    for average in data["Average_Marks"]:
        grade = assign_grade(average)
        grades.append(grade)

    data["Grade"] = grades

    results = []

    for _, student in data.iterrows():
        result = determine_result(
            student,
            subjects
        )

        results.append(result)

    data["Result"] = results

    display_performance_summary(data)

    display_subject_analysis(
        data,
        subjects
    )

    display_highest_lowest(data)

    display_top_performers(data)

    display_pass_fail_statistics(data)

    display_class_average(data)

    display_attendance_analysis(data)

    print("\n" + "=" * 70)
    print("FINAL STUDENT RANKING")
    print("=" * 70)

    ranking = data.sort_values(
        by="Average_Marks",
        ascending=False
    ).reset_index(drop=True)

    ranking["Rank"] = ranking.index + 1

    ranking_display = ranking[
        [
            "Rank",
            "Student_ID",
            "Name",
            "Average_Marks",
            "Grade",
            "Result"
        ]
    ].copy()

    ranking_display["Average_Marks"] = (
        ranking_display["Average_Marks"].round(2)
    )

    print(
        ranking_display.to_string(index=False)
    )

    highest = find_highest_performer(data)
    lowest = find_lowest_performer(data)

    subject_averages = calculate_subject_averages(
        data,
        subjects
    )

    best_subject = find_best_subject(
        subject_averages
    )

    class_average = calculate_class_average(data)

    passed_students = len(
        data[data["Result"] == "Pass"]
    )

    failed_students = len(
        data[data["Result"] == "Fail"]
    )

    print("\n" + "=" * 70)
    print("PRACTICAL ANALYSIS QUESTIONS")
    print("=" * 70)

    print(
        "\n1. Which student has the highest average?"
    )

    print(
        f"   Answer: {highest['Name']} "
        f"with an average of "
        f"{highest['Average_Marks']:.2f}"
    )

    print(
        "\n2. Which student has the lowest average?"
    )

    print(
        f"   Answer: {lowest['Name']} "
        f"with an average of "
        f"{lowest['Average_Marks']:.2f}"
    )

    print(
        "\n3. Which subject has the best average?"
    )

    print(
        f"   Answer: {best_subject} "
        f"with an average of "
        f"{subject_averages[best_subject]:.2f}"
    )

    print(
        "\n4. How many students passed?"
    )

    print(
        f"   Answer: {passed_students} students"
    )

    print(
        "\n5. How many students failed?"
    )

    print(
        f"   Answer: {failed_students} students"
    )

    print(
        "\n6. What is the overall class average?"
    )

    print(
        f"   Answer: {class_average:.2f}"
    )

    print("\n" + "=" * 70)
    print("PROJECT ANALYSIS COMPLETED SUCCESSFULLY")
    print("=" * 70)
    print("\nThe Student Performance Analytics System has")
    print("successfully processed and analyzed the dataset.")
    print("\n")


if __name__ == "__main__":
    main()