import codewars_test as Test


def remove_url_anchor(url):
    # TODO: complete
    print(url)


Test.assert_equals(remove_url_anchor(
    "www.codewars.com#about"), "www.codewars.com")
Test.assert_equals(remove_url_anchor(
    "www.codewars.com/katas/?page=1#about"), "www.codewars.com/katas/?page=1")
Test.assert_equals(remove_url_anchor(
    "www.codewars.com/katas/"), "www.codewars.com/katas/")
