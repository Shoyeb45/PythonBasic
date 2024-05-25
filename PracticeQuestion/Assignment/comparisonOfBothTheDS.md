## Comparison of Time Complexity 
| Functions | Array | Singly Linked List |
|----------|----------|----------|
| Insert element at kth index    | $$O(n)$$     | $$O(n)$$     |
| Delete element at kth index    | $$O(n)$$     | $$O(n)$$     |
| Size    | $$O(1)$$     | $$O(1)$$     |
| Rotate    | $$O(n)$$     | $$O(n)$$     |
| Reverse     | $$O(n)$$     | $$O(n)$$     |
| Append at the end    | $$O(1)$$     | $$O(n)$$     |
| Preappend at the beginning     | $$O(n)$$     | $$O(1)$$     |
| Merge     | $$O(n + m)$$     | $$O(n + m)$$     |
| Interleave     | $$O(n + m)$$     | $$O(n + m)$$     |
| Middle     | $$O(1)$$     | $$O(n)$$     |
| First Occurence     | $$O(n)$$     | $$O(n)$$     |
| Split     | $$O(n)$$     | $$O(n)$$     |
| Empty     | $$O(1)$$     | $$O(1)$$     |


## Comparison of Space Complexity 
| Functions | Array | Singly Linked List |
|----------|----------|----------|
| Insert element at kth index    | $$O(1)$$     | $$O(1)$$     |
| Delete element at kth index    | $$O(1)$$     | $$O(1)$$     |
| Size    | $$O(1)$$     | $$O(1)$$     |
| Rotate    | $$O(1)$$     | $$O(1)$$     |
| Reverse     | $$O(1)$$     | $$O(1)$$     |
| Append at the end    | $$O(1)$$     | $$O(1)$$     |
| Preappend at the beginning     | $$O(1)$$     | $$O(1)$$     |
| Merge     | $$O(n + m)$$     | $$O(1)$$     |
| Interleave     | $$O(n + m)$$     | $$O(1)$$     |
| Middle     | $$O(1)$$     | $$O(1)$$     |
| First Occurence     | $$O(1)$$     | $$O(1)$$     |
| Split     | $$O(1)$$     | $$O(1)$$     |
| Empty     | $$O(1)$$     | $$O(1)$$     |

---

## Comparing Array and Linked List
| Array | Singly Linked List|
|-------|-------------------|
|An array is a grouping of data elements of equivalent data type.|A linked list is a group of entities called a node. The node includes two segments: data and address.|
|It stores the data elements in a contiguous memory zone.|It stores elements randomly, or we can say anywhere in the memory zone.|
|In the case of an array, memory size is fixed, and it is not possible to change it during the run time.|In the linked list, the placement of elements is allocated during the run time.|
|	The elements are not dependent on each other.|The data elements are dependent on each other.|
|The memory is assigned at compile time.|The memory is assigned at run time.|
|It is easier and faster to access the element in an array.|In a linked list, the process of accessing elements takes more time.|
|In the case of an array, memory utilization is ineffective.|In the case of the linked list, memory utilization is effective.|
|When it comes to executing any operation like insertion, deletion, array takes more time.|When it comes to executing any operation like insertion, deletion, the linked list takes less time.|