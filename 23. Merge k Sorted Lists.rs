/*
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
*/

#include <vector>
#include <queue>

using namespace std;

// Definition for singly-linked list.
// The ListNode definition is provided by LeetCode and should not be redefined.
// struct ListNode {
//     int val;
//     ListNode *next;
//     ListNode() : val(0), next(nullptr) {}
//     ListNode(int x) : val(x), next(nullptr) {}
//     ListNode(int x, ListNode *next) : val(x), next(next) {}
// };

// Comparator for the priority queue
struct compare {
    bool operator()(ListNode* l1, ListNode* l2) {
        return l1->val > l2->val;
    }
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // Min-heap (priority queue)
        priority_queue<ListNode*, vector<ListNode*>, compare> pq;
        
        // Push the head of each list into the min-heap
        for (ListNode* list : lists) {
            if (list != nullptr) {
                pq.push(list);
            }
        }
        
        // Dummy node to help with the result list
        ListNode dummy;
        ListNode* tail = &dummy;
        
        while (!pq.empty()) {
            // Get the smallest node
            ListNode* smallest = pq.top();
            pq.pop();
            
            // Add it to the result list
            tail->next = smallest;
            tail = tail->next;
            
            // If there is a next node in the list, push it into the heap
            if (smallest->next != nullptr) {
                pq.push(smallest->next);
            }
        }
        
        return dummy.next;
    }
};
