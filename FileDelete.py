import os

def DeleteFile(FileName):
    if (os.path.exists(FileName)):
        os.remove(FileName)

    else:
        print("There is no such file")

def main():
    print("Enter the file name ")
    Name = input()

    DeleteFile(Name)


if __name__ == "__main__":
    main()