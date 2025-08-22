# List of dictionaries: Each dictionary contains a question, its options, and the correct answer
questions = [
    {
        "question": "Who directed the movie 'Enthiran'?",
        "options": ["A. Mani Ratnam", "B. Shankar", "C. Kamal Haasan", "D. Gautham Menon"],
        "answer": "B"
    },
    {
        "question": "Who played the lead role in the movie 'Vikram' (2022)?",
        "options": ["A. Vijay", "B. Ajith", "C. Kamal Haasan", "D. Suriya"],
        "answer": "C"
    },
    {
        "question": "What is the first film of actor Thalapathy Vijay?",
        "options": ["A. Poove Unakkaga", "B. Nenayvael Selvan", "C. Naalaiya Theerpu", "D. Kadhalukku Mariyadhai"],
        "answer": "C"
    },
    {
        "question": "Who acted as Bharathiyar in the movie 'Bharathi'?",
        "options": ["A. Vivek", "B. Sayaji Shinde", "C. Sayaji Rao", "D. Sayaji Shinda"],
        "answer": "B"
    },
    {
        "question": "In which year was the movie 'Pasanga' released?",
        "options": ["A. 2005", "B. 2007", "C. 2009", "D. 2011"],
        "answer": "C"
    },
    {
        "question": "Under whose direction did Arvind Swamy act in 'Roja'?",
        "options": ["A. Shankar", "B. Mani Ratnam", "C. Bharathiraja", "D. Vijay"],
        "answer": "B"
    },
    {
        "question": "What was director Mysskin’s debut movie?",
        "options": ["A. Sathiyam", "B. Chithiram Pesuthadi", "C. Yuddham Sei", "D. Pisaasu"],
        "answer": "B"
    },
    {
        "question": "Which is a popular Tamil song by singer Srinivas?",
        "options": ["A. Enaadi Enaadi", "B. En Kaadhal Kanbikkave", "C. Manasula Ninaivu", "D. Sukhama"],
        "answer": "B"
    }
]

score = 0
user_answers = [] #user answers are stored in this list

for index, q in enumerate(questions, 1): # questions start from the index 1 
    print(f"{index} question : {q['question']}") # 1 question : text
    for opt in q["options"]: # loop the options
        print(opt)

    user_input = input("Enter your choice (A/B/C/D): ").strip().upper()
    user_answers.append(user_input) #add user input in list

    if user_input == q["answer"]:
        print("The answer is correct!! ✅")
        score += 1
    else:
        print(f"Your answer is wrong ❌. Correct answer is: {q['answer']}")

# Show summary
for index, q in enumerate(questions, 1): # questions start from the index 1 
    print(f"{index}. {q['question']}")
    print(f"   Your answer: {user_answers[index - 1]} | Correct answer: {q['answer']}") #index - 1 because user_answers in list starts from 0 so we minus 1 from the index
    if user_answers[index - 1] == q["answer"]:
        print("   ✅ Correct")
    else:
        print("   ❌ Wrong")


print("\n--- QUIZ OVER ---\n")
print(f"Your Final Score: {score}/{len(questions)}\n")
