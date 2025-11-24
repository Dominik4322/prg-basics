

def letter(text, letter):
    count = 0
    for char in text:
        if char == letter:
            count += 1
    print(f'The number of letters: {count}')