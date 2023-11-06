#import Numbers
#from numbers import DisplayFactors
#from Numbers import *
import Numbers as NUM

def main():
    print("Enter Number : ")
    No = int(input())

    Numbers.DisplayFactors(No)

if __name__ == "__main__":
    main()