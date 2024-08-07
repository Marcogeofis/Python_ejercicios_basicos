def word_frequency(text):
    dict_text = {}
    text_divided = text.split()

    for el in text_divided:
        if el in dict_text:
            dict_text[el] += 1
        else:
            dict_text[el] = 1

    return dict_text


# Example usage:
text = "the quick brown fox jumps over the lazy dog the quick brown fox"

word_dict = word_frequency(text)
print(word_dict)