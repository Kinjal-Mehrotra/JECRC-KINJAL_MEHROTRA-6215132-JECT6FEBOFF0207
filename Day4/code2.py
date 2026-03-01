#Loan approval

salary=int(input("Enter salary: "))
cibil_score=int(input("Enter cibil score: "))

if salary>25000 and cibil_score>700:
    if salary>50000 and cibil_score>750:
        print("instant approval")
    else:
        print("approved")
else:
    print("rejected")