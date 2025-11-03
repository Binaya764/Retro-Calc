#includes the calcuatio part of the calculator
from History import Back_history
class User:
    def calculations(self,num1,num2):
            option = input("Enter the operation you want to perform (add,subtract,multiply,divide):")
            if(option == "add"):
                   result = num1 + num2
                   self.display(result)
                   

            elif(option =="subtract"):
                   result = num1 - num2
                   self.display(result)

            elif(option == "multiply"):
                   result = num1*num2
                   self.display(result)

            elif(option == "divide"):
                   if(num2 == 0):
                          print("cannot be divided by zero!")
                   else:
                          result = num1/num2
                          self.display(result)
                          

                     
              

    


    def User_input(self):
            print("-------------------Calculator-----------------\n")
            data =  input("Enter any  for calulation or (history and clear): ")
            return data
    
    def User_value(self,data):
       
            if(data.lower() == "history"):
                   Back_history.show_history()

            elif(data == "clear"):
                   pass
            else:
                   num1 = int(input("Enter the first number: "))
                   num2 = int(input("Enter the second number: "))
                   result =   self.calculations(num1,num2)
              
    def display(self,result):
           print("The answer is : ", result)


u1 = User()
while(True):
       data = u1.User_input()
       if(data.lower()=='q'):
              break
       else:
              u1.User_value(data)




