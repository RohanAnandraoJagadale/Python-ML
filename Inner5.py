
def Substraction(No1,No2): #200 #PYC - not allowed change ex.write by another devlop
    Ans = 0
    Ans = No1 - No2
    return Ans

def Decorated_Function(Function_Name):   #Function_name = 200
    def Inner(A,B):  #300
        if(A < B):
            A,B = B,A    #swap
        Output = Function_Name(A,B)  #200(12,8)
        return Output
    return Inner  # return 300

def main():   #100
    Value1 = int(input("Enter first number : "))   #ex 8
    Value2 = int(input("Enter second number : "))  #ex 12

    New_Function = Decorated_Function(Substraction)   #Decorated_function 200
    Ret = New_Function(Value1,Value2)# ret = 300(8,12)
    print("Substraction is : ",Ret)

if __name__ == "__main__":
    main()   # call 100()
