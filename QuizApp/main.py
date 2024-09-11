import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

correct_answers_count = 0

for question in data:
    print(question["Question"])
    for index, answer in enumerate(question["Answers"]):
        print(f"{index+1}. {answer}")
    user_answer = int(input("Which answer is correct one? "))
    if user_answer == question["Correct"]:
        correct_answers_count += 1

print(f"Your result is: {correct_answers_count} out of {len(data)}")
