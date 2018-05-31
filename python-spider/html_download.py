import urllib
from urllib import request
class htmlDownload:
    def down(self,url):
        if url is None:
            return
        res=urllib.request.urlopen(url)
        if res.getcode() != 200:
            return None
        return res.read()