/* 
submission Link: https://leetcode.com/submissions/detail/1274333355/  
*/ 

#include<bits/stdc++.h>
using namespace std;
#define loop(i, n) for(int i = 0; i < n; i++)
typedef long long ll;
const ll mod = 1000000007;

class Node {
    public:
        int data;
        Node *next;
    Node(int val) {
        data = val;
        next = nullptr;
    }
};

class MyLinkedList {
public:
    Node *head;
    int size;

    MyLinkedList() {
        head = nullptr;
        size = 0;
    }
    
    int get(int index) {
        if(index < 0 || index >= size) {
            return -1;
        }
        if(!head)
            return -1;
        
        Node* it = head;    
        for(int i = 0; i < index; i++) {
            it = it->next;
        }
        return it->data;
    }
    
    void addAtHead(int val) {
        Node* new_node = new Node(val);
        if(!head) {
            head = new_node;
            size++;
            return;
        } 
        new_node->next = head;
        head = new_node;
        size++;
        return;
    }
    
    void addAtTail(int val) {
        Node* new_node = new Node(val);
        if(head == nullptr) {
            this->addAtHead(val);
            return;
        } 
        Node* it = head;
        while(it && it->next) {
            it = it->next;
        }
        
        it->next = new_node;
        // tail = new_node;
        size++;
        return;
    }
    
    void addAtIndex(int index, int val) {
        if(index < 0 || index > size) {
            return;
        }
        if(index == size) {
            this->addAtTail(val);
            return;
        }
        else if(index == 0) {
            this->addAtHead(val);
            return;
        }
        Node *it = head;
        for(int i = 0; i < index - 1; i++) {
            it = it->next;
        }
        Node* new_node = new Node(val);
        new_node->next = it->next;
        it->next = new_node;
        size++;
        return;
    }
    
    void deleteAtIndex(int index) {
        if(index < 0 || index >= size) {
            return;
        }
        if(index == 0) {
            Node* temp = head;
            head = head->next;
            delete temp;
            size--;
            return;
        }   
        Node* it = head;
        loop(i, index - 1) {
            it = it->next;
        }
        Node* temp = it->next;
        it->next = it->next->next;
        delete temp;
        size--;
        return;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
   
    
    return 0;
}
