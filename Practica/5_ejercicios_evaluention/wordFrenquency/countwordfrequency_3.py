

def word_frequency(text):
    dict_text = {}
    text_divided = text.split()

    for el in text_divided:
        dict_text[el] = dict_text.get(el, 0) + 1
    
    return dict_text


# Example usage:
text = "the quick brown fox jumps over the lazy dog the quick brown fox"

if __name__== '__main__':
    
    word_dict = word_frequency(text)
    print(word_dict)