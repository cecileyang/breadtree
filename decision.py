from typing import List

def decision(user_selections: List) -> List:
    '''
    :param user_selections: the user selections from the questionnaire
    :return: default_answer
    '''
    default_answer = ["Based on your answer, we recommend:"]
    print(user_selections)
    if user_selections[3] == "0-5":
        default_answer.append("* You may want to select a more conservative 60/40 portolio")
    if user_selections[1] == "190k-230k":
        default_answer.append("* While your child may not qualify for financial aid, your child may apply for internships to cover some of his/her tuition")
    if user_selections[7] == "yes":
        default_answer.append("* You may want to consider setting up a trust fund for your child")
    if len(default_answer) == 1:
        default_answer.append('You keep your current portfolio and reduce spending by 10%')

    return default_answer

print(decision(["2 years", "0", "0", "Strongly agree", "0", "0", "0", "0", "0"]))
