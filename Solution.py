class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1


def addTwoNumbers_old(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode

    note: works but not using ListNode
    """
    output = []
    carry = False
    if len(l2) > len(l1):
        first = l2
        second = l1
    else:
        first = l1
        second = l2

    for i in range(len(first)):
        if carry:
            first[i] += 1
            carry = False
        try:
            sum = first[i] + second[i]
        except:
            sum = first[i]
        if sum >= 10:
            output.append(sum % 10)
            carry = True
        else:
            output.append(sum)
    if carry:
        output.append(1)
    return output


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummy = ListNode()
    cur = dummy

    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        val = v1 + v2 + carry
        carry = val // 10
        val = val % 10
        cur.next = ListNode(val)

        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


def read(l1):
    if l1.next:
        read(l1.next)
    print(l1.val)


def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if not list1 and list2:
        return ListNode(list2.val, list2.next)
    elif not list2 and list1:
        return ListNode(list1.val, list1.next)
    if not list1 and not list2:
        return

    if list1.val < list2.val:
        return ListNode(list1.val, mergeTwoLists(list1.next, list2))
    else:
        return ListNode(list2.val, mergeTwoLists(list1, list2.next))


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = 1

    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1
    return l


def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
            i -= 1
        i += 1
    return len(nums)


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # linear insertion
    for i in range(len(nums)):
        if target <= nums[i]:
            return i
    return len(nums)


def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    if n == 1:
        return "1"
    else:
        return countAndSayHelper(countAndSay(n - 1))


def countAndSayHelper(s):
    output = ""
    ptr = s[0]
    count = 0
    for i in s:
        if ptr == i:
            # keep up
            count += 1
        else:
            # new pointer
            output += str(count) + ptr
            count = 1
            ptr = i
    output += str(count) + ptr
    return output


def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    u = {}
    for i in range(len(s)):
        if u.__contains__(s[i]):
            u[s[i]] = -1
        else:
            u[s[i]] = i
    for i in u.values():
        if i != -1:
            return i
    return -1


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    map = {}
    for n in nums:
        if map.__contains__(n):
            map[n] += 1
        else:
            map[n] = 1
    map = {k: v for k, v in sorted(map.items(), key=lambda item: item[1])}
    return list(map.keys())[len(map) - 1]


def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    m = list(filter(None, s.split(' ')))
    return len(m[len(m)-1])


def tribonacci_old(n):
    """
    :type n: int
    :rtype: int
    found something better
    """
    t = [0,1,1]
    p = 2
    for i in range(n-2):
        t.append(t[p] + t[p-1] + t[p-2])
        p += 1
    return t[n]


def tribonacci(n):
    """
    :type n: int
    :rtype: int
    """
    t = [0, 1, 1]
    # lol
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    for i in range(n - 3):
        temp = t[0] + t[1] + t[2]
        t[0] = t[1]
        t[1] = t[2]
        t[2] = temp
    return t[0] + t[1] + t[2]

n = 0
ans = tribonacci(n)
print('PRINT:', ans)
