phrase = "Those who shine with their own light will never be in darkness."

index = 0
max_occurrences = 0
most_frequent_letter = ''

while index < len(phrase):
    current_letter = phrase[index]

    if current_letter == ' ':
        index += 1
        continue
    
    current_count = phrase.count(current_letter)

    if max_occurrences <= current_count:  # Change to < for the first most frequent letter
        max_occurrences = current_count
        most_frequent_letter = current_letter

    index += 1

print(
    'The letter that appeared the most is '
    f'"{most_frequent_letter}" which appeared '
    f'{max_occurrences} times.'
)