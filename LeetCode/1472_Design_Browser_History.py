# 링크드 리스트를 활용해 풀어보기

class Node(object):
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        Node(homepage, None)

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        
        Node(url, None)
        

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
        
BrowserHistory("leetcode.com")
BrowserHistory.visit("google.com")
BrowserHistory.visit("facebook.com")
BrowserHistory.visit("youtube.com")
BrowserHistory.back(1)
BrowserHistory.back(1)
BrowserHistory.forward(1)
BrowserHistory.visit("linkedin.com")
BrowserHistory.forward(2)
BrowserHistory.back(2)
BrowserHistory.back(7)

