average_score=input("Is your average score more than 60? (Give answer 'yes' or 'no') :")=="yes"
completed_assignments=input("Did you complete all assignments? (Give answer 'yes' or 'no') :")=="yes"
attendance=input("Did you attend at least 80% of classes? (Give answer 'yes' or 'no') :")=="yes"
if average_score and completed_assignments and attendance :
    print("Student passed an exam!")
else:
    print("Student couldn't pass an exam!")