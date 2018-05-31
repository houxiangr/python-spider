class htmlOutput:
    def __init__(self):
        self.datas=[]
    def collect(self,data):
        if data is None:
            return
        self.datas.append(data)
    def put(self):
        fout=open('output.html','w',encoding='utf-8')
        for data in self.datas:
            fout.write(data['url'])
            fout.write(data['title'])
            fout.write(data['summary'])
        fout.close()
