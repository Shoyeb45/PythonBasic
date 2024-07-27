#include<bits/stdc++.h>
using namespace std;

// Submission Link: https://leetcode.com/submissions/detail/1335169768/

class Node {
public:
    int data;
    Node *next;
    Node *prev;

    Node(int val) {
        data = val;
        next = prev = nullptr;
    }
};

class DoublyLinkedList {
    unordered_map<int, pair<int, Node*>> mp;
    Node* head;
    Node* tail;

    public:
    DoublyLinkedList() {
        head = tail = nullptr;
    }

    bool search(int key) {
        return mp.find(key) != mp.end();
    }

    int get(int key) {
        if(search(key)) {
            return mp[key].first;
        }
        return -1;
    }

    void assignRecent(int key) {
        Node* curr = mp[key].second;
        if(curr -> next == nullptr && curr -> prev == nullptr || curr -> next == nullptr) {
            return;
        }
        else if(curr -> prev == nullptr) {
            Node* newHead = curr -> next;
            curr -> next -> prev = nullptr;
            curr -> next = nullptr;
            tail -> next = curr;
            curr -> prev = tail;
            tail = curr;
            head = newHead;
            cout << "Imhere\n";
            return;
        }
        curr -> prev -> next = curr -> next;
        curr -> next -> prev = curr -> prev;
        tail -> next = curr;
        curr -> prev = tail;
        tail = curr;
        curr -> next = nullptr;
    }

    void update(int key, int val) {
        mp[key].first = val;
    }
    void deleteHead() {
        Node* temp = head;
        mp.erase(mp.find(temp -> data));
        head = head -> next;
        temp -> next = temp -> prev = nullptr;

        if(head)
            head -> prev = nullptr;
        delete temp;
    }

    void insert(int key, int value) {
        if(!head) {
            head = tail = new Node(key);
            mp[key] = {value, head};
            return;
        }
        Node* newNode = new Node(key);
        mp[key] = {value, newNode};
        tail -> next = newNode;
        newNode -> prev = tail;
        tail = tail -> next;
    }

    void display() {
        cout << "HashMap: " << '\n';
        for(auto it: mp) {
            cout << "Key : " << it.first << " Value: " << it.second.first << "\n"; 
        }

        cout << "DoublyLinkedList\n";
        Node* temp = head;
        while(temp) {
            cout << temp -> data << " ";
            temp = temp -> next;
        } 
        cout << '\n';
    }
};


class LRUCache {
    DoublyLinkedList dll;
    int maxCap;
    int size;
public:
    LRUCache(int capacity) {
        maxCap = capacity;
        size = 0;
    }
    
    int get(int key) {
        if(dll.search(key)) {
           dll.assignRecent(key);
        } 
        return dll.get(key);
    }
    
    void put(int key, int value) {
        if(dll.search(key)) {
            dll.update(key, value);
            dll.assignRecent(key);
            return;
        }

        if(size == maxCap) {
            dll.deleteHead();
            size--;
        }

        dll.insert(key, value);
        size++;
    }

    void display() {
        dll.display();
    }
};


// Main Function 
int main() {
    LRUCache lru(1);
    cout << "Put: " << '\n';
    lru.put(2, 1);
    lru.display();
    cout << "\n";

    cout << "Get:\n" << lru.get(2) << '\n';
    lru.display();
    cout << "\n";

    cout << "Put: " << '\n';
    lru.put(3, 2);
    lru.display();
    cout << "\n";
    
}
