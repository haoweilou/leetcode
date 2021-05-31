'''
We are given two arrays words1 and words2 of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from words1 is universal if for every b in words2, b is a subset of a. 

Return a list of all universal words in words1.  You can return the words in any order.
'''
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        hashMap = {}
        for word in words2:
            tempMap = {}
            for char in word:
                if char not in tempMap:
                    tempMap[char] = 1
                else:
                    tempMap[char] += 1
            for char in tempMap:
                if char not in hashMap:
                    hashMap[char] = tempMap[char]
                else:
                    hashMap[char] = max(hashMap[char],tempMap[char])
        output = []
        for word in words1:
            tempMap = {}
            for char in word:
                if char not in tempMap:
                    tempMap[char] = 1
                else:
                    tempMap[char] += 1
            contain = True
            for char in hashMap:
                if char not in tempMap or tempMap[char] < hashMap[char]:
                    contain = False
                    break
            if contain:
                output.append(word)
        return output