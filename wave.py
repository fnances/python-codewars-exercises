import codewars_test as test


def is_letter(l):
    return True if ord(l) >= 97 and ord(l) <= 122 else False


# def wave(str):
#     upper = []
#     for index, letter in enumerate(str):
#         if is_letter(letter):
#             new_word = str[0:index] + str[index].upper() + \
#                 str[index + 1:len(str)]
#             upper.append(new_word)
#     print(upper)
#     return upper

def wave(str):
    return [
        str[:index] + str[index].upper() + str[index + 1:]
        for index, letter in enumerate(str) if is_letter(letter)]


result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
test.assert_equals(wave("hello"), result)

result = ["Codewars", "cOdewars", "coDewars", "codEwars",
          "codeWars", "codewArs", "codewaRs", "codewarS"]
test.it("Should return: '["+", ".join(result)+"]'")
test.assert_equals(wave("codewars"), result)

result = []
test.it("Should return: '["+", ".join(result)+"]'")
test.assert_equals(wave(""), result)

result = ["Two words", "tWo words", "twO words", "two Words",
          "two wOrds", "two woRds", "two worDs", "two wordS"]
test.it("Should return: '["+", ".join(result)+"]'")
test.assert_equals(wave("two words"), result)

result = [" Gap ", " gAp ", " gaP "]
test.it("Should return: '["+", ".join(result)+"]'")
test.assert_equals(wave(" gap "), result)
