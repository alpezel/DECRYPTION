# ask user for the input (run program & test this text: th& q!#ck br+wn f+x j!mps +v&r th& l*zy d+g)
input_string = input("What's the encrypted text you want to decrypt?")
output_string = ""
# check the character using loop
for i in range(len(input_string)):
    # if *, change to "a"
    if input_string[i] == "*":
        output_string += "a"
    # if &, change to  "e"
    elif input_string[i] == "&":
        output_string += "e"
    # if #, change to "i"
    elif input_string[i] == "#":
        output_string += "i"
    # if +, change to "o"
    elif input_string[i] == "+":
        output_string += "o"
    # !, change to "u"
    elif input_string[i] == "!":
        output_string += "u"
    else:
        output_string += input_string[i]

# print output
print("\nThe decrypted text is: ","\033[4m"+"\033[1;33m"+ output_string)