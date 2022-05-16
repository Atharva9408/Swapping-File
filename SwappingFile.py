def swapFileData():
    file1=input("Select a file name from S1 & S2: ")
    file2= input("Where to swap data: ")

    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file1, 'w') as b:
        data_b=b.read()
    
    with open(file2, 'w') as a:
        a.write(data_b)

    with open(file2, 'w') as b:
        b.write(data_a)

swapFileData()
