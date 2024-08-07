def anagram_checker(word1, word2):
    # Check if lengths of both words are the same
    if len(word1) != len(word2):
        return False
    
    # Sort both words and compare
    return sorted(word1) == sorted(word2)

def print_anagram_result(result):
    if result:
        print('The words are anagrams')
    else:
        print('The words are not anagrams')

if __name__ == '__main__':
    word1 = 'nacionalista'
    word2 = 'altisonancia'

    result = anagram_checker(word1, word2)
    print_anagram_result(result)
