class sieunhan:
    stt = 1
    so_thu_tu = 1
    suc_manh = 50
    def __init__(self, para_ten, para_vukhi, para_mau):
        self .ten = "sieu nhan " + para_ten
        self .vukhi = para_vukhi
        self .mau = para_mau
        self.stt = sieunhan.so_thu_tu
        sieunhan.so_thu_tu += 1
    def xin_chao(self):
        print( "xin chao ta la " + self.ten)
sieu_nhan_A = sieunhan("gao","jozz","den")
sieu_nhan_B = sieunhan('xuan','nam','vang')
print(sieunhan.suc_manh)
sieunhan.suc_manh = 40
sieu_nhan_A.suc_manh = 80
print(sieu_nhan_A.suc_manh)
print(sieu_nhan_A.stt)
print(sieu_nhan_B.stt)
sieu_nhan_A.xin_chao()