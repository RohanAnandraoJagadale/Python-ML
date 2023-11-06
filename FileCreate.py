
def CreateFile(FileName):
    fd = open(FileName, "w")   # crete the file if it not there, juni file delete houn navin yete

def main():
    print("Enter the file name to create")
    Name = input()

    CreateFile(Name)

if __name__ == "__main__":
    main()

