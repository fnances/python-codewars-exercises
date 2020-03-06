import codewars_test as test

# Find the number with the most digits.

# If two numbers in the argument array have the same number of digits, return the first one in the array.


def get(key, arr):
    return [item[key] for item in arr]


def find(arr, expr):
    stuff = list(filter(expr, arr))
    return stuff[0] if len(stuff) > 0 else None


# def find_longest(arr):
#     arr_s = map(lambda n: len(str(n)), arr)
#     def lsm(n): return {"digits": len(str(n)), "num": n}
#     arr_t = max([lsm(n) for n in arr], key=lambda i: i['digits'])
#     # arr_t = max(get('digits', [lsm(n) for n in arr]))
#     # arr_t = max([lsm(n) for n in arr])
#     found = find(arr, lambda x: x == arr_t["num"])
#     print(arr, arr_s, arr_t)
#     return found


def find_longest(arr):
    arr_t = max([{"digits": len(str(n)), "num": n}
                 for n in arr], key=lambda i: i['digits'])
    return max(arr)
    # return arr_t["num"]


test.assert_equals(find_longest([1, 10, 100]), 100)
test.assert_equals(find_longest([9000, 8, 800]), 9000)
test.assert_equals(find_longest([8, 900, 500]), 900)
test.assert_equals(find_longest([3, 40000, 100]), 40000)
test.assert_equals(find_longest([1, 200, 100000]), 100000)
