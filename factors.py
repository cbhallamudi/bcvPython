def getFactors():
    number = eval(input("Get the number to get factors: "))
    dummyVariable = 2
    while dummyVariable < number:
        if number%dummyVariable == 0:
            print(dummyVariable,end=" ")
        dummyVariable += 1
getFactors()        
