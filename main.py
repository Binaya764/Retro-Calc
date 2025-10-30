#includes the calcuatio part of the calculator
class User:
    def calculations(self,num1,num2):
            option = input("Enter the opetation you want to perform (add,subtract,multipley,divide):")
            if(option == "add"):
                   result = num1 + num2
                   self.display(result)
                   

            elif(option =="subtract"):
                   pass
            elif(option == "multiply"):
                   pass
            elif(option == "divide"):
                   pass
    


    def User_input(self):
            print("-------------------Calculator-----------------\n")
            data =  input("Enter any  for calulation or (history and clear): ")
            return data
    
    def User_value(self,data):
       
            if(data == "history"):
                   pass
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
       if(data=='q' or 'Q'):
              break
       else:
              u1.User_value(data)




