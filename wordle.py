import random
get_input, wordList, word, result, tries = (lambda inp="": inp if len(inp)==5 and inp.lower() in wordList else get_input(inp = input("Enter a guess: "))), [i.strip() for i in open("wordlist.txt")], random.choice([i.strip() for i in open("wordlist.txt")]), "", 0
while result != "🟩🟩🟩🟩🟩" and tries < 6:
    result, tries = "".join([("🟩" if i==j else "🟨" if i in word else "⬛️") for i,j in zip(get_input().lower(), word.lower())]), tries + 1
    print(result + ("\nWell Done!" if result=="🟩🟩🟩🟩🟩" else "") + (f"\nUnlucky, word was {word}" if tries > 5 else ""))