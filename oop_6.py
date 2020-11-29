class nhat:
    def __init__(self, ho, ten,):
        self.ho = ho
        self.ten = ten 
    @property
    def ho_va_ten(self):
        return '{} {}'.format(self.ho,self.ten)
    @property
    def mailll(self):
        return self.ho + '-' +self.ten + '@gmail.com'
    @ho_va_ten.setter
    def ho_va_ten(self,ten_moi):
        ho_moi,ten_moi = ten_moi.split(' ')
        self.ho = ho_moi
        self.ten = ten_moi
    @ho_va_ten.deleter
    def ho_va_ten(self):
        self.ho = None
        self.ten = None
        print(' xoa xoa ')
anh = nhat('nam','tuantuan')
anh.ho_va_ten = 'chau hoang'
del anh.ho_va_ten
print(anh.ho_va_ten)

