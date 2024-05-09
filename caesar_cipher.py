def encrypt(text,s):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        if(char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def decrypt(text,s):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        if(char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result
    
text = input("Enter Message: ")
shift = int(input("Enter shift value: "))
print("text: " + text)
print("Shift: " + str(shift))
enycrpt_text = encrypt(text,shift)
print("Cipher Text: " + enycrpt_text)
print("Decrypted Text: " + decrypt(enycrpt_text,shift))