class sieunhan:
    def __init__(self, para_ten, para_vukhi, para_mau):
        self .ten = "sieu nhan " + para_ten
        self .vukhi = para_vukhi
        self .mau = para_mau
    def xin_chao(self):
        return "xin chao ta la " + self.ten
sieu_nhan_A = sieunhan("gao","jozz","den")
print(sieu_nhan_A.xin_chao())