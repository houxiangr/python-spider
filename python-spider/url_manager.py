class urlManager:
    def __init__(self):
        self.newurls=set()
        self.oldurls=set()
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.oldurls and url not in self.newurls:
            self.newurls.add(url)
    def has_url(self):
        return len(self.newurls)!=0
    def get_url(self):
        url=self.newurls.pop()
        self.oldurls.add(url)
        return url
    def add_new_urls(self,new_url):
        if new_url is None or len(new_url)==0:
            return
        for url in new_url:
            self.add_new_url(url)