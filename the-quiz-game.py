"""Task 1: Develop a list of questions and answers.
Task 2: Write a function that quizzes the user and takes their answers.
Task 3: Score the quiz and give the user feedback on their performance."""


# Task 1

questions = ["What is 2 + 2? ", "What is 4 * 4? ", "What is 100 / 2? "]
answers = [4, 16, 50]


# Task 2

questions_right = 0

def quiz_question(question_array):
    for question in range(len(question_array)):
        user_answer = input(question_array[question])

        if int(user_answer) == answers[question]:
            global questions_right
            questions_right += 1

    return questions_right


# Task 3
quiz_question(questions)
print(f'You Have Scored {questions_right} Out of {len(questions)}')