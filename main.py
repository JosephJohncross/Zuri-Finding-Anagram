# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    sorted_word = ''.join(sorted(word));
    sorted_anagram = ''.join(sorted(anagram));
    if (sorted_word == sorted_anagram):
        return True;
    return False

print(find_anagram("hello", "check"));
print(find_anagram("below", "elbow"));
