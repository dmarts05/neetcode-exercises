def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT


def test_is_anagram():
    s = "anagram"
    t = "nagaram"
    assert is_anagram(s, t)
    s = "rat"
    t = "car"
    assert not is_anagram(s, t)
