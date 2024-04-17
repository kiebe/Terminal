import re
import random

def get_words() -> list:
    with open("maket") as f:
        html = f.read()
        
    maket = r'text-base lowercase text-left glow">([A-Z]+)'
    words = re.findall(maket, html)
    
    return words

def get_letter_positions(words: list):
    positions = {}
    for word in words:
        for letter in range(len(word)):
            if f"{word[letter]}{letter}" in positions:
                positions[f"{word[letter]}{letter}"] += 1
            else:
                positions[f"{word[letter]}{letter}"] = 1
                
    return positions

def get_better_position(positions: dict) -> str:
    better_position = None
    count_position = 0
    for position in positions:
        if positions[position] > count_position:
            better_position = position
            count_position = positions[position]
    return better_position

def get_better_word(words: list, better_position: str) -> str:
    better_words = []
    for word in words:
        if word[int(better_position[1:])] == better_position[0]:
            better_words.append(word)
    return random.choice(better_words)

def search_for_matching_words(target: str, words: list, n: int) -> list:
    results = []
    for word in words:
        if word != target:
            coincidences = 0
            for letter in range(len(word)):
                if word[letter] == target[letter]:
                    coincidences += 1
            if coincidences == n:
                results.append(word)
    return results
    
def main():
    words = get_words()
    
    while True:
        print(f"[INFO] {' | '.join(words)}")    
        positions = get_letter_positions(words)
        better_position = get_better_position(positions)
        better_word = get_better_word(words, better_position)
        print(words.pop(words.index(better_word)))
        
        coincidences = input(">")
        if coincidences != "!":
            words = search_for_matching_words(better_word, words, int(coincidences))
        else:
            return
    
main()