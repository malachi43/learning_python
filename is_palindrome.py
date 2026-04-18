import palindrome

def is_palindrome(word):
    if len(word) == 1:
        return True
    elif len(word) == 2 and palindrome.first(word) == palindrome.last(word):
        return True
    elif palindrome.first(word) == palindrome.last(word):
        return is_palindrome(palindrome.middle(word))
    else:
        return False
    