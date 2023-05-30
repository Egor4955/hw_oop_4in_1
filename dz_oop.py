class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"
   

    def avg_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        return round(sum_rating / len_rating, 2)
        

    def avg_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        return round(sum_rating / len_rating, 2)
    

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_rating()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'


    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.avg_rating() < other.avg_rating()




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []




class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def avg_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        return round(sum_rating / len_rating, 2)


    def avg_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        return round(sum_rating / len_rating, 2)


    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_rating()}"


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.avg_rating() < other.avg_rating()      




class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'
         



student_1 = Student('Lebron', 'James', 'Man')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Java']

student_2 = Student('Ana', 'De Armas', 'Girl')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Java']


lecturer_1 = Lecturer('Bon', 'Jovi')
lecturer_1.courses_attached += ['Python']
 
lecturer_2 = Lecturer('Arnold', 'Schwarzenegger')
lecturer_2.courses_attached += ['Git']


reviewer_1 = Reviewer('Sylvester', 'Stallone')
reviewer_1.courses_attached += ['Python']
 
reviewer_2 = Reviewer('Jackie', 'Chan')
reviewer_2.courses_attached += ['Git']


reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Git', 10)

reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Git', 5)
reviewer_2.rate_hw(student_2, 'Git', 5)

student_1.rate_lec(lecturer_1, 'Python', 7)
student_1.rate_lec(lecturer_1, 'Python', 7)
student_1.rate_lec(lecturer_1, 'Git', 5)
student_1.rate_lec(lecturer_1, 'Git', 5)

student_2.rate_lec(lecturer_2, 'Python', 7)
student_2.rate_lec(lecturer_2, 'Python', 7)
student_2.rate_lec(lecturer_2, 'Git', 5)
student_2.rate_lec(lecturer_2, 'Git', 5)


student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]
reviewer_list = [reviewer_1, reviewer_2]


def average_rating_for_course(course, list):
    sum_rating = 0
    quantity_rating = 0
    for el in list:
        for course in el.grades:
            stud_sum_rating = el.avg_rating_for_course(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return average_rating


print(average_rating_for_course('Python', student_list))
print(average_rating_for_course('Git', student_list))

print(average_rating_for_course('Python', lecturer_list))
print(average_rating_for_course('Git', lecturer_list))

print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)