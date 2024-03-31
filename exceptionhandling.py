'''try:
    a=int(input())
    b=int(input())
    print (a/b)
except ZeroDivisionError:
    print("Not allowed to divide by 0")

#
try:
    a=int(input())
    b=int(input())
    print (a/b)
except TypeError:
    print("Unsupported")
except ZeroDivisionError:
    print("Not allowed to divide by 0")
except ValueError:
    print("Out of Try except Block")
print ("Bye")
'''


randomList = ['a', 0, 2]
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)
