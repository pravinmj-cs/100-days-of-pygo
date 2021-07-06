alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input("Type 'encode' or 'decode' to decrypt: ")
text = input("Type you message:\n").lower()
shift = int(input("Type the shift number: "))


# def encrypt(text, shift):
#     list_text = list(text)
#     encode_text = []
#     for l in text:
#         pos = alphabet.index(l)
#         new_position = pos+shift
#         new_letter = alphabet[new_position]
#         encode_text.append(new_letter)
#     return ''.join(encode_text)


# def decrypt(text, shift):
#     list_text = list(text)
#     decode_text = []
#     for l in text:
#         pos = alphabet.index(l)
#         new_position = pos-shift
#         new_letter = alphabet[new_position]
#         decode_text.append(new_letter)
#     return ''.join(decode_text)


def caesar(etype, text, shift):
    list_text = list(text)
    cipher_text = []
    if etype == "decode":
        shift *= -1
    for l in text:
        print(l)
        pos = alphabet.index(l)
        new_position = pos+shift
        new_letter = alphabet[new_position]
        cipher_text.append(new_letter)
    return ''.join(cipher_text)


print(caesar(etype=direction, text=text, shift=shift))

# if direction == "encode":
#     print(encrypt(text, shift))
# elif direction == "decode":
#     print(decrypt(text, shift))
# else:
#     print("Type encode or decode")
