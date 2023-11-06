print("Application to Demonstrate Industrial Programing")

import Marvellousmodule

def main():
    print("Value of __name__ from main is : ", __name__)
    print("Enter first number :")
    no1 = int(input())
    print("Enter second number : ")
    no2 = int(input())

    Sum = Marvellousmodule.Addition(no1,no2)

    print("Addition is : ", Sum)

if __name__ == "__main__":
    main()