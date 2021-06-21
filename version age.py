def age():
    while True:
        age = input("Please enter your age : ")
        if age.replace(' ','').isnumeric():#using replace to allow spaces after the answer
            if 3< int(age)<100: #allowing age, 3 to 100 only
                break
            else:
                print("=========================================================")
                print('Sorry you have to between 3 and 100 to play this quiz! ')
                print("Thank you come again!")
                print("=========================================================")
                exit()
               
        else:
            print("The data type you have used is invalid data type.\n")
age()
