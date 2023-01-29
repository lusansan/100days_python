from material import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

shift_num = 5

pw = 'abc'

def encode_letter(letter,shift_num):
    letter_index = alphabet.index(letter)
    letter_shift_index = (letter_index + shift_num) % 26
    encode_letter = alphabet[letter_shift_index]


def caesar(start_text, shift_amount, cipher_direction):
    if cipher_direction == 'encode':
        shift_text = []
        for letter in start_text:
            letter_index = alphabet.index(letter)
            letter_shift_index = (letter_index + shift_num) % 26
            shift_text.append(alphabet[letter_shift_index])


run = True
while run:
  print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))