def func(words, wordpack, word, depth):
    if len(wordpack) == depth:
        return
    
    for i in range(len(wordpack)):
        new_word = word + wordpack[i]
        words.append(new_word)
        func(words, wordpack, new_word, depth + 1)

def solution(word):
    wordpack = ['A','E','I','O','U']
    words = []
    func(words, wordpack, '', 0)
    words.sort()
    # print(words)
    return words.index(word) + 1

print(solution('UUUEU'))