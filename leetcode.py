#1. Two Sum
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_hash = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_hash:
                return [num_hash[diff] ,i]
            num_hash[nums[i]] = i
        return None

#2. Add Two Numbers
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        node = res
        flag = 0
        while l1 and l2:
            temp = l1.val + l2.val + flag
            flag = 0
            if temp > 9:
                flag = 1
                temp = temp%10
            node.next = ListNode(temp)
            node = node.next
            l1 = l1.next
            l2 = l2.next
        rest = l1 or l2
        node.next = rest
        if rest is None and flag:
            node.next = ListNode(flag)
        while rest and flag:
            rest.val += flag
            flag = 0
            if rest.val > 9:
                flag = 1
                rest.val %= 10
            if rest.next is None and flag:
                rest.next = ListNode(flag)
                flag = 0
            rest = rest.next
        return res.next
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(-1)
        node = res
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry,10)
            node.next = ListNode(val)
            node = node.next
        return res.next

#3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_hash = {}
        res = temp = 0
        head = 0
        for i in range(len(s)):
            if s[i] in s_hash and s_hash[s[i]] >= head:
                temp = i - s_hash[s[i]]
                head = s_hash[s[i]] +1
            else:
                temp += 1
                res = max(res, temp)
            s_hash[s[i]] = i
        return res

#4. Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        while nums1 and nums2:
            if nums1[0] <= nums2[0]:
                nums.append(nums1.pop(0))
            else:
                nums.append(nums2.pop(0))
        nums += nums1 or nums2
        lens = len(nums)
        return nums[lens//2] if lens%2 != 0 else (nums[lens//2-1] + nums[lens//2])/2
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        k = (m+n-1)//2
        lo, hi = 0, m
        while lo < hi:
            mid = (lo + hi)//2
            if k-mid-1 < 0 or a[mid] > b[k-mid-1]:
                hi = mid
            else:
                lo = mid + 1
        i = lo
        rest = sorted(a[i:i+2] + b[k-i:k-i+2])
        return (rest[0]+rest[1-(m+n)%2])/2.0

#5. Longest Palindromic
class Solution: #从两边到中间判断回文超时，中间几个数不是回文会导致最差的时间复杂度
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def is_palindromic(s):
            lo = 0
            hi = len(s) - 1
            while lo < hi:
                if s[lo] == s[hi]:
                    lo += 1
                    hi -= 1
                else:
                    return False
            return True

        maxs = s[0]
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if j - i <= len(maxs):
                    break
                if is_palindromic(s[i:j]):
                    maxs = s[i:j]
        return maxs

class Solution: #从中间到两边判断回文超时，避免上一种方法中最差的情况
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1 or not s:
            return s
        lens = len(s)
        maxlen = 1
        maxstr = s[0]
        for i in range(lens):
            x = 1
            while i-x >= 0 and i+x < lens:  #奇数回文
                if s[i-x] != s[i+x]:
                    break
                x += 1
            x -= 1
            curlen = 2*x+1
            if curlen > maxlen:
                maxlen = curlen
                maxstr = s[i-x:i+x+1]
            x = 1
            while i-x+1 >= 0 and i+x <lens: #偶数回文
                if s[i-x+1] != s[i+x]:
                    break
                x += 1
            x -= 1
            curlen = 2*x
            if curlen > maxlen:
                maxlen = curlen
                maxstr = s[i-x+1:i+x+1]
        return maxstr


class Solution: #manacher算法
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '#' + '#'.join(s) + '#'
        lens = len(s)
        p = []
        idx = 0
        mx = 0
        for i in range(lens):
            if mx > i:
                r = min(p[2 * idx - i], mx - i)  # 当i处在mx的范围内，有两个下限值，一个是关于idx对称的值和超过边界的值
            else:
                r = 1
            while i - r >= 0 and i + r < lens and s[i - r] == s[i + r]:
                r += 1
            p.append(r - 1)
            if (i + p[i]) > mx:
                mx, idx = i + p[i], i

        maxr = max(p)
        maxi = p.index(maxr)
        res = s[maxi - maxr:maxi + maxr + 1].split('#')
        res = res[1:-1]
        return ''.join(res)

