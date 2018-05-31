import url_manager
import html_download
import html_output
import html_parse
class Spider(object):
    def __init__(self):
        self.url=url_manager.urlManager()
        self.download=html_download.htmlDownload()
        self.output=html_output.htmlOutput()
        self.parse=html_parse.htmlParse()
    def run(self,root_url):
        count=1
        self.url.add_new_url(root_url)
        while self.url.has_url():
            craw_url=self.url.get_url();
            print('Craw %d %s:'%(count,craw_url))
            html_cont=self.download.down(craw_url)
            new_urls,content=self.parse.analysis(craw_url,html_cont)
            self.url.add_new_urls(new_urls)
            self.output.collect(content)
            if count==10:
                break
            count+=1
            self.output.put()

if __name__=='__main__':
    root_url="https://baike.baidu.com/item/Python/407313?fr=aladdin"
    spider=Spider()
    spider.run(root_url)