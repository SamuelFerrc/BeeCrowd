class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        valores = []
        for l in lists:
            aux = l
            while aux:
                valores.append(aux.val)
                aux = aux.next
        valores.sort()
        valorF = None
        if valores:
            final = ListNode()
            aux = final
            while valores:
                aux.val = valores.pop(0)
                if valores:
                    aux.next = ListNode()
                aux = aux.next
            valorF = final
        return valorF