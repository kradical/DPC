import re

word_list = open('wordlist').read().split('\n')

cipher = {'H': 'a', 'D': 'o'}

def take_input():
    estring = input("encrypted string: ")
    num_hints = input("how many hints: ")
    hints = []
    try:
        for x in range(int(num_hints)):
            hints.append(input("hint #"+str(x)+": "))
    except TypeError:
        print("input a number")
        exit(1)
    estring2 = ''.join(n for n in estring)
    return estring2, hints

def find_possible_words(word, cipher):
    """returns a list of possible words"""
    letters = []
    repeated = [None]
    regex = '^'
    for char in word:
        if char in cipher:
            regex += cipher[char]
            if char not in letters:
                letters.append(char)
            continue
        if char not in letters:
            letters.append(char)
            if not char.isalpha():
                regex += char
                continue
            if word.count(char) > 1:
                repeated.append(char)
                regex += '(.)'
            else:
                regex += '.'
        else:
            regex += '\\' + str(repeated.index(char))
    regex += '$'
    return [x for x in word_list if re.match(regex, x) and len(letters) == len(set(x))]

def cipher_from_map(before, after, base):
    cipher = dict(base)
    for b, a in zip(before, after):
        if cipher.get(b, a) != a:
            return False
        cipher[b] = a
    if len(set(cipher.values())) != len(cipher):
        return False
    return cipher

def unscramble(cipherwords, depth, cipher):
    if depth >= len(cipherwords):
        return [cipher]
    ciphers = []
    for option in find_possible_words(cipherwords[depth], cipher):
        new_cipher = cipher_from_map(cipherwords[depth], option, cipher)
        if new_cipher:
            result = unscramble(cipherwords, depth + 1, new_cipher)
            if result:
                ciphers.extend(result)
    return ciphers

def apply_cipher(word, cipher):
    return ''.join([cipher.get(letter, letter) for letter in word])

def get_result(cipher_text, cipher):
    return ' '.join([apply_cipher(word, cipher) for word in cipher_text])

def decode(cipher_text):
    ciphers = unscramble(cipher_text.split(' '), 0, cipher)
    return [get_result(cipher_text.split(), c) for c in ciphers]

def main():
    cipher_text = "IAL FTNHPL PDDI DR RDNP WF IUD"
    # the square root of four is two

    print('\n'.join([solution for solution in decode(cipher_text)]))




if __name__ == "__main__":
    main()