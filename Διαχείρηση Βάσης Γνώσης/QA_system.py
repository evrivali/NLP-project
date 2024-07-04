import pandas as pd
from Levenshtein import ratio
data = pd.read_csv('qa.csv')
def getResults(questions, fn):
    for q in questions:
        answer = fn(q)
        print("Question:",q,"Answer:",answer)
test_data = [
    "in the matrix neo takes which pill?",
    "Jennifer Lawrence won the oscar for what 2012 film",
    "Who wrote the famous scary theme music from Halloween?",
    "What crime film revitalized John Travolta’s career?",
    "For which 1964 movie did Julie Andrews win Best Actress?",
    "For what movie did Tom Hanks win his 1st Academy Award nomination?",
    "is Joker R rated?"
]
def getApproximateAnswer(q):
    max_score = 0
    answer = ""
    for idx, row in data.iterrows():
        score = ratio(row["Question"], q)
        if score >= 0.9:
            return row["Answer"]
        elif score > max_score:
            max_score = score
            answer = row["Answer"]
    if max_score > 0.5:
        return answer
    return "Sorry, I didn't get you."
getResults(test_data, getApproximateAnswer)



