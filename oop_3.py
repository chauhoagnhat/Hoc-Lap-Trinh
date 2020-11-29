class sieunhan:
    suc_manh = 9595
    def __init__(self, para_ten, para_vukhi, para_mau):
        self .ten = "sieu nhan " + para_ten
        self .vukhi = para_vukhi
        self .mau = para_mau
    @classmethod
    def cap_nhat_suc_manh(cls,smanh):
        cls.para_ten = smanh+smanh
sieu_nhan_A = sieunhan("do",'gao','tim')
sieunhan.cap_nhat_suc_manh(100)
print(sieunhan.suc_manh)
class sieunhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vukhi, para_mau):
        self .ten = "sieu nhan " + para_ten
        self .vukhi = para_vukhi
        self .mau = para_mau
    @classmethod
    def from_string(cls, s):
        lst = s.split('-')
        new_lst = [st.strip()for st in lst]
        ten, vu_khi, mau_sac = new_lst
        return cls(ten, vu_khi, mau_sac)
infor_str = "do - kiem - do"
sieu_nhan_A = sieunhan.from_string(infor_str)
class sieunhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vukhi, para_mau):
        self .ten = "sieu nhan " + para_ten
        self .vukhi = para_vukhi
        self .mau = para_mau
    @staticmethod
    def bien_hinh ():
        print('sieu nhan bien hinh')
sieu_nhan_A = sieunhan("do",'gao','tim')
sieunhan.bien_hinh()