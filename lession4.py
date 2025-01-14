class Game:
    so_tien = 10000
    so_luong = 0
    def __init__(self, ten):
        self.ten = ten
        self.nuoc = 0
        self.anh_sang = 0
        Game.so_luong += 1
        Game.so_tien -= 200
      
    @property  
    def tinh_trang(self):
        if self.nuoc == None and self.anh_sang == None:
            return "Đã bán"
        elif self.nuoc == 0 and self.anh_sang == 0:
            return "Hạt mầm"
        elif self.nuoc > 0 and self.anh_sang > 0:
            return "Đang sống"
        else:
            return "Đã chết"