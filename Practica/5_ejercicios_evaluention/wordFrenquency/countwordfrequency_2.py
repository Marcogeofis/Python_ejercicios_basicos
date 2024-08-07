from collections import Counter

def word_frequency(text):
    text_divided = text.split()
    return Counter(text_divided)


# Example usage:
text = "the quick brown fox jumps over the lazy dog the quick brown fox"

if __name__== '__main__':
    
    word_dict = word_frequency(text)
    print(word_dict)