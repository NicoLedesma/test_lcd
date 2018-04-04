class Junior():
    def __init__(self,id,nickname,code=None):
        self.id=id
        self.code=code
        self.nickname=nickname

    def __str__(self):
        return self.nickname
