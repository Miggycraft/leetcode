def isSubsequence(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    a = list(s)
    for i in t:
        if i == a[0]:
            a.pop(0)
        if not a:
            return True
    return False

if __name__ == "__main__":
    s = "acb"
    t = "ahbgdc"
    a = isSubsequence(None, s, t)
    print(a)