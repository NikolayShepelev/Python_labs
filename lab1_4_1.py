text = "абвгдееежзззийклмнопрссттууфхцчшщъыыыььэээюя"

tally = {}
for char in text:
    if char.isalpha():
        tally[char] = tally.get(char, 0) + 1

most_common_char = max(tally, key=tally.get)
most_common_freq = tally[most_common_char]

alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
char_freq_in_alphabet = {char: index for index, char in enumerate(alphabet)}

result = sorted(tally.keys(), key=lambda x: abs(tally[x] - char_freq_in_alphabet[x]))

print(result)
