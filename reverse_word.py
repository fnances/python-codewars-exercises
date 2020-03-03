from python_test_framework import codewars_test as test

def reverse_words(text):
    words = text.split()
    for word in words:
        print(word.capitalize())
    return text


test.assert_equals(reverse_words('The quick brown fox jumps over the lazy dog.'),
                   'ehT kciuq nworb xof spmuj revo eht yzal .god')
test.assert_equals(reverse_words('apple'), 'elppa')
test.assert_equals(reverse_words('a b c d'), 'a b c d')
test.assert_equals(reverse_words('double  spaced  words'),
                   'elbuod  decaps  sdrow')


