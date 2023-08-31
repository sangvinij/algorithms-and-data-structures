def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)


def is_palindrome(s1):
    return s1.lower() == s1[::-1].lower()
