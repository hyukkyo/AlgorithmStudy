# 링크드 리스트를 활용해 풀어보기

class Node(object):
    def __init__(self, url = "", prev = None, next = None):
        self.url = url
        self.prev = next
        self.next = prev

class BrowserHistory(object):
    def __init__(self, homepage):
        new_node = Node(homepage, None, None)
        self.current_node = new_node


    def visit(self, url): # 이후의 히스토리들을 전부 삭제함
        new_node = Node(url, None, None)
        
        if self.current_node:
            new_node.prev = self.current_node
            self.current_node.next = new_node
            self.current_node = new_node
        else:
            self.current_node = new_node
            
        

    def back(self, steps):
        while steps > 0 and self.current_node.prev:
            self.current_node = self.current_node.prev
            steps -= 1
        return self.current_node.url
        

    def forward(self, steps):
        while steps > 0 and self.current_node.next:
            self.current_node = self.current_node.next
            steps -= 1
        return self.current_node.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

bh = BrowserHistory("leetcode.com")
bh.visit("google.com")
bh.visit("facebook.com")
bh.visit("youtube.com")
bh.back(1)
bh.back(1)
bh.forward(1)
bh.visit("linkedin.com")
bh.forward(2)
bh.back(2)
bh.back(7)

