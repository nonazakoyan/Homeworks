def is_letter(char):
    if (ord('a') <= ord(char) <= ord('z')) or (ord('A') <= ord(char) <= ord('Z')):
        return True
    return False

lst_vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

character = input("input the character \
>>>  ")

if is_letter(character):
    if character in lst_vowel:
        print("vowel")
    else:
        print("consonant")
else:
    print("input isn't letter")