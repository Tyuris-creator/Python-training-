def main():
    counts = {}
    words = get_words("address.txt")
    lowercase_words = [word.lower() for word in words if len(word) > 4]

    counts = {word: word.count(word) for word in lowercase_words}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    
    save_counts(counts)