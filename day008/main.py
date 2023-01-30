from material import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    if cipher_direction == 'decode':
        shift_amount = -1 * shift_amount
    cipher_text = ""
    for letter in start_text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            letter_shift_index = (letter_index + shift_amount + 26) % 26
            cipher_text += alphabet[letter_shift_index]
        else:
            cipher_text += letter
    print(f"Here's the {cipher_direction}d result: {cipher_text}\n")


run = True
while run:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher_text = caesar(start_text = text, shift_amount = shift, cipher_direction = direction)
    choice = input("Do you want to run this program again?\nType 'Yes' or 'No': ").lower()
    if choice == 'no':
        run = False
        print("Goodbye.")