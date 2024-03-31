try:
    fo=open("myfile.txt","r")
    print("Opened file")
except FileNotFoundError:
    print("File doesnt exist")
except:
    print("Other error")
print("Bye")