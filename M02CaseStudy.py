'''
Layla Nettavong
M02CaseStudy
App will take student names and grades to determine if the student is on the Dean's List, Honor Roll, or neither
'''
#Step1: ask for student's last name. quit processing if the last name is 'ZZZ'.
    #All in while loop, make all name inputs uppercase
last_name = input("Please enter your last name. If you are done, enter 'ZZZ'")
last_name = last_name.upper()

while last_name != "ZZZ":
    #Step2: ask for and accept a student's first name. ask for and accept the student's GPA as a float.
    first_name = input("What's your first name?")
    first_name = first_name.upper()
    #Checks if input is a float
    try:
        grade = float(input("What's your grade in deciaml form?"))
        
    except ValueError:
        grade = float(input("Invalid input. What's your grade in deciaml form?"))

 

    #Step3: if the student's GPA is 3.5 or greater, print message saying student has made the Dean's List. 
    #if student's GPA is 3.25 or greater, print message saying studnet has made the Honor Roll.

    if grade >= 3.5:
        print("You made it to the Dean's List!")

    elif grade >= 3.25:
        print("You made it to Honor Roll!")
    
    else:
        print("You won no award.")
        
    last_name = input("Please enter your last name. If you are done, enter 'ZZZ'")
    last_name = last_name.upper()

quit()