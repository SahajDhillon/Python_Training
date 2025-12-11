alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

continue_cypher = True


def encode(num):
    code = input("Enter string you want to encode: ")
    result_encoded = ""
    for letter in code.lower():
        letter_place = alphabets.index(letter)
        cyphered_letter = alphabets[letter_place + num]
        result_encoded += cyphered_letter
    print(result_encoded)


def decode(num):
    code = input("Enter string you want to decode: ")
    result_decoded = ""
    for letter in code.lower():
        letter_place = alphabets.index(letter)
        cyphered_letter = alphabets[letter_place - num]
        result_decoded += cyphered_letter
    print(result_decoded)


def ceaser_cypher():
    if option.lower() == "encode":
        encode(shift)
    elif option.lower() == "decode":
        decode(shift)


if __name__ == '__main__':
    while continue_cypher:
        continue_game = input("Do you want to cypher? ")
        if continue_game.lower() == "yes":
            option = input("Do you want to encode or decode: ")
            shift: int = int(input("Select the shift number: "))
            ceaser_cypher()
        else:
            continue_cypher = False
