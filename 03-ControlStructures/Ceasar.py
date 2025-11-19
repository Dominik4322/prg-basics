###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    kod = ord(char) 
    # add one to the character's code
    nowy_kod = kod + 1
    # replace new character code with its
    # corresponding character (use chr())
    nowy_chr = chr(nowy_kod)
    # add encrypted character to encrypted text
    encrypted_text += nowy_chr

print(plain_text)
print(encrypted_text)