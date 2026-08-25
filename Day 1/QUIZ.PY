questions = (
    "Largest desert in the World is : ",
    "Which city is known as the City of Joy ? ",
    "Mount Everest is located in ________",
    "The longest river in India is _________? "
)

options = (
    ("A. Thar", "B. Amazon", "C. Kalahari", "D. Sahara"),
    ("A. Delhi", "B.Jaipur", "C.Kolkata", "D. Banaras"),
    ("A. India", "B. Nepal", "C.China", "D. Bhutan"),
    ("A.Yamuna", "B. Kaveri", "C. Brahmaputra", "D. Ganga")
)

Answers = ("D", "C", "B", "D")

guesses = []
score = 0
question_num = 0

for question in questions:
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("A, B, C, D: ").upper()
    guesses.append(guess)

    if guess == Answers[question_num]:
        score += 1
        print("Correct choice!")
    else:
        print("Incorrect choice!")
        print(f"{Answers[question_num]} is the correct answer")

    question_num += 1

print("**********************")

print("Answers: ", end="")
for answer in Answers:
    print(answer, end=" ")

print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")

print()

score = score / len(questions) * 100

print(f"Your score is: {score}%")