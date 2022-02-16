import sys, getopt
from text_man import *
from encoder import init_encode

argumentList = sys.argv[1:]
print(argumentList)
options = "hc:t:i:d:"
long_options = ["help", "code", "text =", "image =", "decode ="]

#Variables
mode = -1 #0: code 1: file 2: decode
text = ''
filename = ''
imagesrc = ''

if __name__ == "__main__":
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
example: python3 main.py -c "Hello World!" -i image.png
or just run the program without any arguments to see the menu""")
                
            elif currentArgument in ("-c", "--code"):
                if(mode != -1): raise Exception("You can't use -c and -t at the same time")
                text = currentValue
                mode = 0

            elif currentArgument in ("-t", "--text"):
                if(mode != -1): raise Exception("You can't use -c and -t at the same time")
                filename = currentValue
                mode = 1
                
            elif currentArgument in ("-i", "--image"):
                imagesrc = currentValue
            
            elif currentArgument in ("-d", "--decode"):
                if(mode != -1): raise Exception("You can't use -d and other arguments at the same time")
                imagesrc = currentValue
                mode = 2
            
            else:
                print("command not recognized, please use -h or --help for help")
    except getopt.error as err:
        print (str(err))
    
    if mode == 0:
        code_bytes = str_to_bytes([text])
        code_bits = bytes_to_bin(code_bytes)
        init_encode(code_bits, imagesrc)
    elif mode == 1:
        text_list = read_file(filename)
        code_bytes = str_to_bytes(text_list)
        code_bits = bytes_to_bin(code_bytes)
        init_encode(code_bits, imagesrc)
    elif mode == 2:
        #TODO
        #init_decode(imagesrc)
        pass