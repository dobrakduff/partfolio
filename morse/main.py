import morsealphabet

phrase = input('Enter your phrase \n')
split_phrase = []

for letter in phrase:
    split_phrase += letter.lower()

morse_phrase = []
for letter in split_phrase:
    for symbol in morsealphabet.alphabet:
        if symbol == letter:
            morse_phrase.append(morsealphabet.alphabet[symbol])

print(f"Your origin phrase:{phrase}\nYour translate phrase:{morse_phrase}")
