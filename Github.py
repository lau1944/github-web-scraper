class Github :
    def __init__(self,title,githublink,detail,language,star,folk):
        self.title=title,
        self.githublink=githublink,
        self.detail=detail,
        self.language=language,
        self.star=star,
        self.folk=folk
    def reponseJson(self) :
        return {
            'title' : self.title,
            'link' : self.githublink,
            'detail' : self.detail,
            'language' : self.language,
            'star' : self.star,
            'folk' : self.folk
        }