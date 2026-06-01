quiz_data = {
    "What is the capital of India?": "Delhi",
    "Which programming language are we learning?": "Python",
    "What is 5 + 7?": "12",
    "Which keyword is used to define a function in Python?": "def",
    "What is the extension of a Python file?": ".py",
    "Which data type is used to store text in Python?": "str",
    "What does CPU stand for?": "Central Processing Unit",
    "Which loop is used when the number of iterations is known beforehand?": "for",
    "What symbol is used for comments in Python?": "#",
    "What is the output of: print(2 * 3)": "6"
}

score = 0

print("=== Python Quiz App ===")

for question, answer in quiz_data.items():
    user_answer = input(f"\n{question}\nYour Answer: ")

    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct Answer:", answer)

total_questions = len(quiz_data)

print("\n=== Quiz Finished ===")
print(f"Your Score: {score}/{total_questions}")

if score == total_questions:
    print("Excellent! Perfect Score 🎉")
elif score >= 7:
    print("Good Job! 👍")
elif score >= 5:
    print("Keep Practicing 🙂")
else:
    print("Need More Practice 📚")
