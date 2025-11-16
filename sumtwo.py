# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        soma = ListNode()
        aux = l1
        aux2 = l2
        aux3 = soma
        carry = 0

        while aux and aux2:
            numb = int((aux.val + aux2.val + carry))%10

            aux3.val = numb
            carry = int((aux.val + aux2.val + carry)/10)
           # print(carry, numb)

            aux2 = aux2.next
            aux = aux.next
            if aux and aux2:
                aux3.next = ListNode()
                aux3 = aux3.next
        while aux:
            aux3.next = ListNode()
            aux3 = aux3.next
            aux3.val = int(aux.val + carry)%10
            carry = int(aux.val + carry)/10
            aux = aux.next
        while aux2:
            aux3.next = ListNode()
            aux3 = aux3.next
            aux3.val = int(aux2.val + carry)%10
            carry = int(aux2.val + carry)/10
            aux2 = aux2.next
        while int(carry):
            aux3.next = ListNode()
            aux3 = aux3.next
            aux3.val = int(carry)
            carry = 0

        aux3 = soma
        while aux3:
            print(aux3.val)
            aux3 = aux3.next



sum1 = ListNode(9)
sum1.next = ListNode(9)
sum1.next.next = ListNode(1)
#sum1.next.next.next = ListNode(9)
#sum1.next.next.next.next = ListNode(9)
#sum1.next.next.next.next.next = ListNode(9)
#sum1.next.next.next.next.next.next = ListNode(9)

sum2 = ListNode(1)
#sum2.next = ListNode(9)
#sum2.next.next = ListNode(9)
#sum2.next.next.next = ListNode(9)
Solution().addTwoNumbers(sum1, sum2)



