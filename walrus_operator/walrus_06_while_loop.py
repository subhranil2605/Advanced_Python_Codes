question: str = "Will you use the walrus operator?"
valid_answers: set = {"yes", "Yes", "y", "Y", "no", "No", "n"}

# user_answer: str = input(f"\n{question}")
# while user_answer not in valid_answers:
#     print(f"Please answer one of {', '.join(valid_answers)}")
#     user_answer = input(f"\n{question}")

# This works but has an unfortunate repetition of identical input() lines

user_answer = str()
while (user_answer := input(f"\n{question}")) not in valid_answers:
    print(user_answer)
    print(f"Please answer one of {', '.join(valid_answers)}")
