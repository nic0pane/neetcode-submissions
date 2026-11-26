class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}

        for item in s:
            if item not in hash_s:
                hash_s[item] = 1
            else:
                hash_s[item] += 1
        for key in t:
            if key not in hash_t:
                hash_t[key] = 1
            else:
                hash_t[key] += 1

        if hash_s == hash_t:
            return True
        else: 
            return False
            
    