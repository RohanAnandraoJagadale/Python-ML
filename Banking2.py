# Instance variable : Name, Account, Address, Account Number
# Instance method : CreateAccount(), DisplayAccountinfo
# Class variable : Bank_Name , ROI_On_FD
# Class Method :  DisplayBankInformation
# Static Method : DisplayKYCInfo

class Bank_Account:

    Bank_Name = "HDFC Bank PVT LTD"
    ROI_On_FD = 6.7

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

    def DisplayAccountInfo(self):  #Constructor madhun aali
        print("\n------Your Account Information is as below------")
        print("Name of Account Holder : ", self.Name)
        print("Account Number : ", self.AccountNo)
        print("Address of Account Holder : ", self.Address)
        print("Current Amount in account : ", self.Amount)

    @classmethod
    def DisplayBankInformation(cls):   #class madhun aali
        print("\nWelcome to Banking Console")
        print("Name of our Bank is : ",cls.Bank_Name)
        print("Rate of Intrest we offer on fixed deposite : ",Bank_Account.ROI_On_FD)

    @staticmethod
    def DisplayKYCInfo():
        print("Please consider below KYC information")
        print("According to the rules of Government of India you have to submite")
        print("1 : Clear and recent passport size photo")
        print("2 : Photo of Adhar card")
        print("3 : photo of PAN card")

    def Deposite(self,value):    # instance method
        self.Amount = self.Amount + value

    def Withdraw(self,value):
        self.Amount = self.Amount - value

def main():

    Bank_Account.DisplayKYCInfo()

    print("\nName of Bank : ",Bank_Account.Bank_Name)
    print("Rate of Interest on Fixed Deposit : ",Bank_Account.ROI_On_FD)

    Bank_Account.DisplayBankInformation()

    User1 = Bank_Account()
    User2 = Bank_Account()

    print("\nCreating the First User Account")
    User1.CreatAccount()
    print("\nCreating the Second User Account")
    User2.CreatAccount()


    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

    User1.Deposite(500)
    User2.Deposite(1200)

    print("Amount of {} after deposite is {}: ",format(User1.Amount))
    print("Amount of {} after deposite is {}: ",format(User2.Amount))

    User1.Withdraw(200)
    User2.Withdraw(3000)

    print("Amount of {} after deposite is {}: ",format(User1.Amount))
    print("Amount of {} after deposite is {}: ",format(User2.Amount))

if __name__ == "__main__":
    main()