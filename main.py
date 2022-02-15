import sys, getopt
from image_man import *

if __name__ == "__main__":
    pass

argumentList = sys.argv[1:]
print(argumentList)
options = "hc:t:i:"
long_options = ["help", "code", "text =", "image ="]
 
try:
    # Parsing argument and checking them
    arguments, values = getopt.getopt(argumentList, options, long_options)
    for currentArgument, currentValue in arguments:
 
        if currentArgument.lower() in ("-h", "--help"):
            print ("""
-h, --help: print this help message
-c, --code: the code you want to put in the image, as a string
-t, --text: text file to read the code from
-i, --image: image to put the code in

example: python3 main.py -c "Hello World!" -i image.png""")
             
        elif currentArgument in ("-c", "--code"):
            pass

        else:
            print("command not recognized, please use -h or --help for help")
            
             
except getopt.error as err:
    print (str(err))