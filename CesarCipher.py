def encryptstr(message):
    #declare variables
    newstring = str()
    ascii_letter_value = int()
    one_letter = str()
    new_ascii_value = int()
    #loop to assign new ACSII value
    for index in range(0, len(message)):
        one_letter = message[index]
        ascii_letter_value = ord(one_letter)
        #checking if the lterr is Z or z
        if ascii_letter_value == 122:
            new_ascii_value = 97
        elif ascii_letter_value == 90:
            new_ascii_value = 65
        #reassigning a new ascii value if not Z or z
        else:
            new_ascii_value = ascii_letter_value + 1
        newstring = newstring + chr(new_ascii_value)
    return newstring

def decryptstr(message):
    #declare variables
    newstring = str()
    ascii_letter_value = int()
    one_letter = str()
    new_ascii_value = int()
    #loop to assign new ACSII value
    for index in range(0, len(message)):
        one_letter = message[index]
        ascii_letter_value = ord(one_letter)
        #checking if the lterr is Z or z
        if ascii_letter_value == 122:
            new_ascii_value = 97
        elif ascii_letter_value == 90:
            new_ascii_value = 65
        #reassigning a new ascii value if not Z or z
        else:
            new_ascii_value = ascii_letter_value - 1
        newstring = newstring + chr(new_ascii_value)
    return newstring

def main():
    message = str()
    choice = str()
    message = input("Enter text:")
    choice = input("(E)ncrypt or (D)ecrypt?")
    if choice == "E":
        output = encryptstr(message)
        print(output)
    else:
        output = decryptstr(message)
        print(output)
    
main()