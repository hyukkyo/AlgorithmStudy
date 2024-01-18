# 링크드 리스트를 활용해 풀어보기

class Node(object):
    def __init__(self, url = "", next = None, prev = None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory(object):
    def __init__(self, homepage):
        self.current_node = None
        self.size = 0


    def visit(self, url):
        new_node = Node(url, None, None)
        
        if self.current_node:
            pass
        else:
            self.current_node = new_node
            
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        


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

