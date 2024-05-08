def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    x = str(x)
    return x == x[::-1]
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    output = 0
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    for i in range(len(s) - 1):
        temp = romanToIntHelper(s[i], s[i + 1])
        if temp == 0:
            output += roman[s[i]]
        else:
            output += temp
    output += roman[s[-1]]
    return output
def romanToIntHelper(s1, s2):
    if s1 == 'I' and (s2 == 'V' or s2 == 'X'):
        return -1
    elif s1 == 'X' and (s2 == 'L' or s2 == 'C'):
        return -10
    elif s1 == 'C' and (s2 == 'D' or s2 == 'M'):
        return -100
    return 0
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    strs = sorted(strs, key=len)
    prefix = strs[0]
    for s in strs:
        for i in range(len(prefix)):
            if s[i] != prefix[i]:
                prefix = s[0:i]
                break
    return prefix
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    pushers = ['{', '(', '[']
    for l in s:
        if pushers.__contains__(l):
            stack.append(l)
        try:
            if l == ')' and stack.pop() != '(':
                return False
            if l == '}' and stack.pop() != '{':
                return False
            if l == ']' and stack.pop() != '[':
                return False
        except:
            return False

    return len(stack) == 0
def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not haystack.__contains__(needle):
        return -1
    for i in range(len(haystack) - len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


