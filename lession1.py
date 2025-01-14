class Student:
    name = ''
    score = {}
    school = ''
    address = ''
    
    def score_average(self):
        score_average = 0
        for subject, point in self.score.items():
            score_average += point
            
        return score_average / 3
    
    def show_rank(self):
        score_average = 0
        for subject, point in self.score.items():
            score_average += point
        score_average = score_average / 3
        if score_average >= 9:
            return "giỏi"
        elif score_average > 6 and score_average <= 8:
            return "Khá"
        else:
            return "TB"
    
    def show_info_student(self):
        score_average = self.score_average()
        rank = self.show_rank()
        name = self.name
        print(f"Học sinh tên: {name} - Xếp loại {rank} - Điểm TB: {score_average}")
        
    def diem_cao_nhat(self):
        score = self.score
        diem_cao_nhat = 0
        mon_diem_cao_nhat = ''
        for subject, point in score.items():
            if point > diem_cao_nhat:
                diem_cao_nhat = point
                mon_diem_cao_nhat = subject
                
        print(f"Môn điểm cao nhất là môn: {mon_diem_cao_nhat} - điểm: {diem_cao_nhat}")
            

std2 = Student()
std2.name = "hiếu"
std2.school = "Trường THCS Cầu giấy" 
std2.address = "Hà Nội1" 

std1 = Student()
std1.name = "Nguyễn Thế Doanh"
std1.school = "Trường THCS Công nguyên"
std1.address = "Hà Nội"

std3 = Student()
std3.name = "Nguyễn Thị Hệ"
std3.school = "Trường THCS Công nguyên"
std3.address = "Hà Nội"

std2.score = {
    'toán': 9,
    'van' : 8,
    'english': 10
}
std2.show_info_student()
std2.diem_cao_nhat()
        
