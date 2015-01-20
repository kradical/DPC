import string


def caesar(plaintext, shift) -> string:
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

text = input("Enter input to be encrypted: ")
key = input("Enter an offset: ")
new_text = caesar(text, int(key))
print(new_text)
new_text = caesar(new_text, -int(key))
print(new_text)