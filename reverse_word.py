import codewars_test as test


def reverse_word(word):
    rev = ""
    index = len(word) - 1
    while index > 0:
        rev += word[index]
        index -= 1
    return rev


def is_letter(l):
    return True if ord(l) >= 97 and ord(l) <= 122 else False


def reverse_words(text):
    # words = text[::-1].split()
    # words.reverse()
    # return "".join(words)
    rev = ''
    index = len(text) - 1
    # letters = list(text)
    words = []
    one_word = ""
    # start_index = 0
    # end_index = 0
    # for index, letter in enumerate(list(text)):
    #     l = letter.lower()
    #     print(index, letter)
    #     if is_letter(l):
    #         if one_word != "":
    #             one_word += l
    #         else:
    #             one_word = l
    #     else:
    #         words.append(reverse_word(one_word))
    #         if one_word != "":
    #             one_word += l
    #         else:
    #             one_word = l

    print(words, one_word)
    # while index >= 0:
    #     rev += text[index]
    #     index -= 1

    # as_array = list(rev)
    # as_array.reverse()
    # print(as_array, rev)
    # return "".join(as_array)


test.assert_equals(reverse_words('The quick brown fox jumps over the lazy dog.'),
                   'ehT kciuq nworb xof spmuj revo eht yzal .god')
test.assert_equals(reverse_words('apple'), 'elppa')
test.assert_equals(reverse_words('a b c d'), 'a b c d')
test.assert_equals(reverse_words('double  spaced  words'),
                   'elbuod  decaps  sdrow')
