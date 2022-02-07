import traceback

try:
    x = 4/0
except:
    print("This is an exception message")
    traceback.print_exc()

print("Program continue...")