class HocSinh:
    so_luong = 0
    def __init__(self, name, school, address):
        self.name = name
        self.school = school
        self.address = address
        HocSinh.so_luong += 1
    
    @classmethod  
    def so_luong_hs(cls):
        return cls.so_luong
    
    @staticmethod
    def ten_truong():
        return "ICANTECH"
    
hs1 = HocSinh("An", "THCS Công nguyên", "Hà Nội")
hs2 = HocSinh("Huy", "THCS Cầu giải", "Hà Nội")

print(HocSinh.so_luong_hs())
print(HocSinh.ten_truong())


class Student:
    def __init__(self, name, math, literature, english):
        self.name = name
        self.score = {
            'toán': math,
            'van' : literature,
            'english': english
        }

    @classmethod
    def from_string(cls, string):
        name, math, literature, english = string.split(',')
        return cls(name, math, literature, english)

    @staticmethod
    def show_class_name():
        return "ICANTECH"
    
    def score_average(self):
        score_average = 0
        for subject, point in self.score.items():
            score_average += point
        return score_average / 3
