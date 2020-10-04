def find_long_words(text, min_word_length):
    return [word for word in text.split() if len(word) > min_word_length]


def test_find_long_words():
    assert find_long_words('', 1) == []
    assert find_long_words('a', 1) == []
    assert find_long_words('word', 4) == []
    assert find_long_words('word', 3) == ['word']
    assert find_long_words('text', 3) == ['text']
    text = "Python is an easy to learn, powerful programming language."
    result = ['Python', 'is', 'an', 'easy', 'to', 'learn,', 'powerful', 'programming', 'language.']
    assert find_long_words(text, 1) == result
    assert find_long_words(text, 5) == ['Python', 'learn,', 'powerful', 'programming', 'language.']
