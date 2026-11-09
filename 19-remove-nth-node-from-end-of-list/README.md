# [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

**Difficulty:** Medium · **Topic:** Linked List · **Solved:** 2026-11-09 · **Language:** Python3

**Approach:** two pointers with a gap. Move `cur` n steps ahead; if it is already `None`, the node to remove is the head, so return `head.next`. Otherwise move both pointers until `cur` falls off the end, with the slow pointer starting one step late so it stops on the node *before* the one to remove, then skip over it with `head.next = head.next.next`.

**Complexity:** O(L) time for a list of length L, one pass; O(1) space.
