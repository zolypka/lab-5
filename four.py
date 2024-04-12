input_words = input("Enter words separated by spaces: ").split()

def are_anagrams(*words):
    def normalize(word):
        return ''.join(sorted(word.lower()))

    normalized_words = [normalize(word) for word in words]
    return len(set(normalized_words)) == 1

print(are_anagrams(*input_words))

#O(k * n log n)
