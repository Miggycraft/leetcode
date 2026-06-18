def maxVowels(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    vowel = ['a', 'e', 'i', 'o', 'u'] 
    high = len(list(filter(lambda x : x.lower() in vowel, list(s[0:k]))))
    curr = high
    for i in range(1,len(s)-k+1):
        print(curr)
        if s[i-1] not in vowel:
            curr -= 1
        if s[i-1+k] in vowel:
            curr += 1
        high = max(high, curr)
    return high

if __name__ == "__main__":
    s = "leetcode"
    k = 3
    a = maxVowels(None, s, k)
    print(a)