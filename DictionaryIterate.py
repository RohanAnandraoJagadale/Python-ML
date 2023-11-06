Batches = {"PPA" : 18000, "LB" : 16700, "Python" : 16500, "Angular" : 15000}

print("Data of Dictionary : ", Batches)

print("Data traversal using for loop")
for x in Batches:
    print(x)

print("Data traversal using for loop")
for x in Batches:
    print(x,Batches[x])

print("Data traversal using for loop")
for x in Batches:
    print(x, Batches.get(x))

keyBatches = Batches.keys()
print(keyBatches)
print(type(keyBatches))

valueBatches = Batches.values()
print(valueBatches)
print(type(valueBatches))

