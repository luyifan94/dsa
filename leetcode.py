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