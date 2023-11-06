
# Instance variable : Name, Account, Address, Account Number
# Instance method : CreateAccount(), Display Account info

class Bank_Account:

    def __init__(self):           # Default constructor
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def CreatAccount(self):
        print("Enter your name : ")
        self.Name = input()

        print("Enter your Initial Amount : ")
        self.Amount = int(input())

        print("Enter your Address : ")
        self.Address = input()

        print("Enter your Account Number : ")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("\n------Your Account Information is as below------")
        print("Name of Account Holder : ", self.Name)
        print("Account Number : ", self.AccountNo)
        print("Address of Account Holder : ", self.Address)
        print("Current Amount in account : ", self.Amount)


def main():
    User1 = Bank_Account()
    User2 = Bank_Account()

    print("Creating the First User Account")
    User1.CreatAccount()
    print("\nCreating the Second User Account")
    User2.CreatAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

if __name__ == "__main__":
    main()