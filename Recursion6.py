
def Display(No):

    if(No > 0):
        No = No - 1
        Display(No)  # recursive call # head recursion
        print(No)   # back traking
Display(4)