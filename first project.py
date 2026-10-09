#  Student Grading & Record System

students_database={}
while True:
    print('1, Add a student')
    print('2, View all records')
    print('3, Exit')

    choice=(input('select an option: '))
    
    if choice=='1':
        student_name=input("What's your name: ")
        math_score=int(input('how much did you score on the math exam: '))
        science_score=int(input('how much you scored on the science exam: '))
        english_score=int(input('what about english: '))

        total=math_score + science_score + english_score
        average=total/3
        if average>=90:
            grade='A'
        elif average>=80:
            grade='B'
        elif average>=70:
            grade='C'
        elif average>=60:
            grade='D'
        else:
            grade='F'
        students_database[student_name]={"math":math_score,"science":science_score,"english":english_score,"average":average,"grade":grade}
        print(f"student {student_name} has bes added succssfully")

    elif choice=='2':
        if len(students_database)==0:
            print('no records exist yet')
        else:
            print('>>>>>> STUDENTS RECORDS <<<<<<')
            for name,data in students_database.items():
                print(f"Name: {name}")
            print(
            f"  Scores -> Math: {data['math']}, Science:"
            f" {data['science']}, English: {data['english']}" )
            print(f"  Average: {data['average']}")
            print(f"  Grade: {data['grade']}")
    
    elif choice=='3':
        print('........................................................................')
        
        print('goodbye sucker✌️✌️😭')
        break
    else:
        print('Error : invalid option!!!')


