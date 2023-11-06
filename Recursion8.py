#4
#4+3+2+1 = 10

def Add(No):
    if(No <= 0):
        return 0  #1
    else:
        return (No + Add(No-1))    # + == * factorial

Ret = Add(4)

print("Result is : ",Ret)