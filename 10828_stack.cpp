#include <iostream>

using namespace std;

struct Node {
	int data;
	Node* next;
};

Node* top = NULL;

int main() {
	int num;
	cin >> num;

	int i, element;
	string cmd;

	int size = 0;

	for (i = 0; i < num; i++) {
		cin >> cmd;	
		if (cmd == "push") {
			cin >> element;
			Node* newnode = new Node();
			newnode->data = element;
			newnode->next = top;
			top = newnode;

			size++;
		}
		else if (cmd == "pop") {
			if(top == NULL) {
				cout << "-1" << endl;
			}
			else {
				cout << top->data << endl;
				top = top->next;

				size--;
			}
		}
		else if (cmd == "size") {
			cout << size << endl;
		}
		else if (cmd == "empty") {
			if(top == NULL) {
				cout << "1" << endl;
			}
			else {
				cout << "0" << endl;
			}
		}
		else if (cmd == "top") {
			if(top == NULL) {
				cout << "-1" << endl;
			}
			else {
				cout << top->data << endl;
			}
		}
	}

	return 0;
}
