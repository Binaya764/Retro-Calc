#includes the calcuatio part of the calculator
class User:
    def calculations(self,num1,num2):
            option = input("Enter the opetation you want to perform (add,subtract,multipley,divide):")
            if(option == "add"):
                   result = num1 + num2
                   

            elif(option =="subtract"):
                   pass
            elif(option == "multiply"):
                   pass
            elif(option == "divide"):
                   pass
    


    def User_input(self):
            print("-------------------Calculator-----------------\n")
            data =  input("Input value for calulation or (history and clear): ")
            if(data == "history"):
                   pass
            elif(data == "clear"):
                   pass
            else:
                   num1 = int(input("Enter the first number: "))
                   num2 = int(input("Enter the second number: "))

    def display(self,result):
           print("The answer is : ", result)
    

u1 = User()
u1.User_input()
u1.calculations()
u1.display()

