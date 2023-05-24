vowels = "аеёиоуыэюя"
poem = input("Введите стихотворение: ")
syllables = []


for phrase in poem.split():
    phrase_syllables = 0
for word in phrase.split("-"):
    phrase_syllables += sum([1 for letter in word.lower() if letter in vowels])
syllables.append(phrase_syllables)


if syllables.count(syllables[0]) == len(syllables):
    print("Парам пам-пам")
else:
    print("Пам парам")
