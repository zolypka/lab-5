words = list(input("Enter your words separated by space: ").split())


def longestCommonPrefix(words):
    if not words:
        return ""

    min_word = min(words)
    max_word = max(words)

    for i in range(len(min_word)):
        if min_word[i] != max_word[i]:
            return min_word[:i]

    return min_word


print(longestCommonPrefix(words))

#O(n)
