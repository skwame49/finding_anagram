# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here

    x = sorted(word)
    y = sorted(anagram)
    if x == y:
        return True
    else:
        return("False")

find_anagrams("below", "elbow")
find_anagrams("under", "upper")
find_anagrams("forget", "forgot")
find_anagrams("seam", "same")