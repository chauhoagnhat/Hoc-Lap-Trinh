class sieunhangao:
    suc_manh = 100100
    def __init__(self, para_ten, para_vukhi, para_mau):
        self .ten = "sieu nhan " + para_ten
        self .vukhi = para_vukhi
        self .mau = para_mau
class sieunhanx(sieunhangao) :
    suc_manh = 20000
    def __init__(self, para_ten, para_vukhi, para_mau,para_thu):
        #self .ten = "sieu nhan " + para_ten
        #self .vukhi = para_vukhi
        #self .mau = 
        super().__init__(para_ten, para_vukhi, para_mau )
        self .thu = para_thu


sieu_nhan_con = sieunhanx('do','vang','xanh','5831')
print(sieu_nhan_con.__dict__)