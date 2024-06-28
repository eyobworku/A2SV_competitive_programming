# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        dummy = ListNode()
        ans = dummy
        for i in range(len(lists)):
            if lists[i]:
                arr.append((lists[i].val,i))
        heapify(arr)
        while arr:
            v,i = heappop(arr)
            dummy.next = ListNode(v)
            dummy = dummy.next
            if lists[i].next:
                lists[i] = lists[i].next
                heappush(arr,(lists[i].val,i))
        return ans.next
        