student_name=input("Enter your name:")
score_1 = float(input("Enter your first score: "))
score_2 = float(input("Enter your second score: "))
score_3 = float(input("Enter your third score: "))
def average_score(score_1,score_2,score_3):
    """receives three scores and returns the average score"""
    return (score_1 + score_2 + score_3)/3
average=round(average_score(score_1,score_2,score_3),2)
def get_grade(average):
    if average>=80:
        return "A"
    elif average>=70:
        return "B"
    elif average>=60:
        return "C"
    elif average>=50:
        return "D"
    else:
        return "F"
grade=get_grade(average)
print(f"Sir,{student_name}'s average score is {average} and his grade is {grade}")



