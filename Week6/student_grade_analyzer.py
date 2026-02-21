# Exercise 2: Student Grade Analyzer

# 1. Initialize Data Structures
# TODO: Create an empty dictionary to store student names and their grades.

student_records =[]
stats = {}

print("=== GIOVANNI'S GRADE ANALYZER ===\n")

# 2. Function to Add Student Grades for 6 students
# TODO: Define a function that prompts the user for a student's name and multiple grades.

for i in range(1, 7):
    print(f"\nEnter Student {i}:")
    name = input(" Name: ")
    score = int(input(" Score: "))
    student_records.append((name, score))


# 3. Function to Calculate Statistics
# TODO: Define a function that takes a student's name and calculates their:

scores =[score for name, score in student_records]

stats['highest'] = max(scores)
stats['lowest'] = min(scores)
stats['average'] = sum(scores) / len(scores)


# 4. Function to Generate Full Report (Display results)
# TODO: Define a function that prints a report for all students, including their:

# find unique scores and count grade distribution

unique_scores = set(scores)

grade_distribution = {}
for score in scores:
    grade_distribution[score] = grade_distribution.get(score,0) + 1

#Display results
print("\n=== STUDENT RECORDS ===")
for i, record in enumerate(student_records, start = 1):
    print(f"{i}. {record[0]}: {record[1]}")

print("\n=== CLASS STATISTICS ===")
print(f"Highest Score: {stats['highest']}")
print(f"Lowest Score: {stats['lowest']}")
print(f"Average Score: {stats['average']}")

print("\n=== UNIQUE SCORES ===")
print(unique_scores)

print("\n=== GRADE DISTRIBUTION ===")
for score in grade_distribution.items():
    print(f"Score {score}: {stats} students")






# 5. Main Program Loop
# TODO: Implement a loop that allows the user to:
