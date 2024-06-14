/*
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?
*/

#include <iostream>
#include <vector>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (head == nullptr || k == 1) return head;

        // Dummy node initialization
        ListNode* dummy = new ListNode(0);
        dummy->next = head;

        ListNode* current = dummy;
        ListNode* nex = dummy;
        ListNode* pre = dummy;
        int count = 0;
        while (current->next != nullptr) {
            current = current->next;
            count++;
        }

        while (count >= k) {
            current = pre->next;
            nex = current->next;
            for (int i = 1; i < k; i++) {
                current->next = nex->next;
                nex->next = pre->next;
                pre->next = nex;
                nex = current->next;
            }
            pre = current;
            count -= k;
        }
        return dummy->next;
    }
};

// Helper function to create linked list from vector (for local testing)
ListNode* createLinkedList(const std::vector<int>& values) {
    ListNode* dummy = new ListNode(0);
    ListNode* tail = dummy;
    for (int value : values) {
        tail->next = new ListNode(value);
        tail = tail->next;
    }
    ListNode* head = dummy->next;
    delete dummy; // Clean up the dummy node
    return head;
}

// Helper function to print linked list (for local testing)
void printLinkedList(ListNode* head) {
    while (head != nullptr) {
        std::cout << head->val;
        if (head->next != nullptr) {
            std::cout << "->";
        }
        head = head->next;
    }
    std::cout << std::endl;
}

int main() {
    // Example 1
    std::vector<int> values1 = {1, 2, 3, 4, 5};
    int k1 = 2;
    ListNode* head1 = createLinkedList(values1);

    Solution solution;
    ListNode* result1 = solution.reverseKGroup(head1, k1);
    printLinkedList(result1); // Output: 2->1->4->3->5

    // Example 2
    std::vector<int> values2 = {1, 2, 3, 4, 5};
    int k2 = 3;
    ListNode* head2 = createLinkedList(values2);

    ListNode* result2 = solution.reverseKGroup(head2, k2);
    printLinkedList(result2); // Output: 3->2->1->4->5

    return 0;
}
