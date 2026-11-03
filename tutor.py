print("=" * 45)
print("       PERSONALIZED TUTOR AGENT")
print("=" * 45)

student_name = input("Enter Student Name: ")

questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["1. function", "2. def", "3. fun", "4. define"],
        "answer": 2
    },
    {
        "question": "Which data type is used to store True or False?",
        "options": ["1. int", "2. string", "3. bool", "4. float"],
        "answer": 3
    },
    {
        "question": "Which symbol is used to start a comment in Python?",
        "options": ["1. //", "2. #", "3. /*", "4. --"],
        "answer": 2
    },
    {
        "question": "Which function is used to find the length of a list?",
        "options": ["1. size()", "2. count()", "3. length()", "4. len()"],
        "answer": 4
    },
    {
        "question": "Which collection stores data as key-value pairs?",
        "options": ["1. List", "2. Tuple", "3. Dictionary", "4. Set"],
        "answer": 3
    }
]

score = 0

print("\nWelcome,", student_name)
print("Topic: Python Basics")
print("\nAnswer each question by entering 1, 2, 3, or 4.\n")

# Conduct Quiz
for i, q in enumerate(questions, start=1):
    print(f"Q{i}. {q['question']}")

    for option in q["options"]:
        print(option)

    while True:
        try:
            answer = int(input("Enter your answer: "))

            if answer in [1, 2, 3, 4]:
                break
            else:
                print("Please enter a number between 1 and 4.")

        except ValueError:
            print("Please enter a valid number.")

    if answer == q["answer"]:
        score += 1
        print("Correct!\n")
    else:
        print("Incorrect.\n")

# Calculate Result
percentage = (score / len(questions)) * 100

print("=" * 45)
print("             QUIZ RESULT")
print("=" * 45)

print("Student Name :", student_name)
print("Score        :", score, "/", len(questions))
print("Percentage   :", percentage, "%")

# Personalized Learning
if percentage >= 80:
    level = "Advanced Learner"
    material = [
        "Practice advanced Python functions",
        "Learn lambda functions and list comprehension",
        "Practice file handling and exception handling",
        "Solve intermediate-level Python programs"
    ]
    recommendation = "You can move to advanced Python topics."

elif percentage >= 60:
    level = "Intermediate Learner"
    material = [
        "Revise Python functions",
        "Practice loops and conditional statements",
        "Practice lists, tuples, sets, and dictionaries",
        "Solve intermediate-level programming problems"
    ]
    recommendation = "Revise the suggested topics and attempt another quiz."

else:
    level = "Needs Improvement"
    material = [
        "Revise Python variables and data types",
        "Practice if-else statements and loops",
        "Practice basic lists and dictionaries",
        "Solve simple Python programming problems"
    ]
    recommendation = "Review the basic concepts and then attempt the quiz again."

# Display Personalized Result
print("\nLearning Level:", level)

print("\nPersonalized Learning Material:")
for i, topic in enumerate(material, start=1):
    print(f"{i}. {topic}")

print("\nRecommended Next Step:")
print(recommendation)

print("\nThank you for using the Personalized Tutor Agent!")
