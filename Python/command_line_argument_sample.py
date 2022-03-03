import sys

# To test this program with different parameters, modify the args of the launch.json file and press F5 to run in debug mode
# sys.argv is a list containing the python script name (entry 0) + the parameters passed in command line (the remaining entries)
print(f"The program is invoked with {len(sys.argv) - 1} parameters") 
print(f"The parameters are listed follows:")
for i in range(1, len(sys.argv)):
    print(sys.argv[i])