#!/usr/bin/python3
"""
主要是练习字典这种数据结构,类似于js的obect
"""
quiz = {
    "question1": {
        "question":"where is China's capital",
        "anwser":"beijing"
    },
        "question2": {
        "question":"where is China's capital",
        "anwser":"Beijing"
    },
    "question3": {
        "question":"where is China's capital",
        "anwser":"Beijing"
    },
        "question4": {
        "question":"where is America's capital",
        "anwser":"Beijing"
    },
        "question5": {
        "question":"where is China's capital",
        "anwser":"Beijing"
    },
        "question6": {
        "question":"where is China's capital",
        "anwser":"Beijing"
    }
}

score=0
for key,value in quiz.items():
    print(value["question"])
    anwser = input("Anser?")

    if(anwser.lower() == value["anwser"]):
        print("Correct")
        score = score + 1
        print("Your now score is " + str(score))
    else:
        print("Anwser is wrong")
        print("Your score is" + str(score))
        quit()

