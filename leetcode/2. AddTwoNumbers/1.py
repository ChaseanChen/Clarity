class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0) # dummy 假人，傀儡 
        curr = dummy # current 当前
        carry = 0 # carry 进位
        while l1 or l2 or carry: # 只要 l1 或 l2 或 carry 不为 0 就继续循环
            val1 = l1.val if l1 else 0 
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            num = total % 10
            curr.next = ListNode(num)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
    
if __name__ == "__main__":
    node13 = ListNode(3)
    node12 = ListNode(4, node13)
    l1 = ListNode(2, node12)
    
    
    node23 = ListNode(4)
    node22 = ListNode(6, node23)
    l2 = ListNode(5, node22)
    
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    
    print("the result is: ", end = "")
    curr = result
    while curr:
        print(curr.val, end = " ")
        curr = curr.next
    print()
    
    
    