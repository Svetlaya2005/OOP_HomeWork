class Student:
  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}



  def add_courses(self, course_name):
    self.finished_courses.append(course_name)

  def rate_lw(self, lecturer, course, grade):
    if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
      if course in lecturer.grades:
        lecturer.grades[course] += [grade]
      else:
        lecturer.grades[course] = [grade]
    else:
      return 'Ошибка'
   

  def avarage_score(self):
    grade = 0
    average_score = 0
    count = 0
    for val in self.grades.values():
      for v in val:
        grade += v
        count += 1
        average_score = grade / count
      self.avarage_score.append(average_score)



  def __str__(self):
    name_surname_grade = f'Имя:{self.name}\nФамилия:{self.surname}'\
      f'\nСредняя оценка за домашние задания{round(self.avarage_score(),1)}'\
      f'\nКурсы в процессе изучения:{",".join(self.courses_in_progress)}'\
      f'\nЗавершенные курсы:{",".join(self.finished_courses)}'
    return name_surname_grade


  def __lt__(self, other):
    if not isinstance(other, Student):
      print('Можно сравнивать только Студентов между собой.')
    else:
      return self.avarage_score() < other.avarage_score()


class Mentor:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []

class Lecturer(Mentor):
  def __init__(self, name, surname):
    super().__init__(name, surname)
    self.grades = {}

    
  def avarage_score(self):
    grade = 0
    average_score = 0
    count = 0
    for val in self.grades.values():
      for v in val:
        grade += v
        count += 1
        average_score = grade / count
      self.avarage_score.append(average_score)


  def __str__(self):
    name_surname_grade = f'Имя:{self.name}'
    f'\nФамилия:{self.surname}'
    f'\nСредняя оценка за лекции: {round(self.avarage_score(),1)}'
    return name_surname_grade


  def __lt__(self, other):
    if isinstance(other, Lecturer):
      return self.avarage_score() < other.avarage_score()

class Reviever(Mentor):
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
    name_surname = f'Имя:{self.name}\nФамилия:{self.surname}'
    return name_surname

  
student_1 = Student('Ruoy', 'Eman', 'm')
student_1.courses_in_progress += ['Python', 'JS', 'C']
student_1.finished_courses += ['Git']   
student_1.rate_lw(lecturer_1,'Python', 9)
student_1.rate_lw(lecturer_2, 'JS', 9)
student_1.rate_lw(lecturer_3, 'C', 9)


student_2 = Student('Sigurni', 'Viver', 'w')
student_2.courses_in_progress += ['Python', 'JS', 'C']
student_2.finished_courses += ['Web']   
student_2.rate_lw(lecturer_1,'Python', 8)
student_2.rate_lw(lecturer_2, 'JS', 8)
student_2.rate_lw(lecturer_3, 'C', 8)

student_3 = Student('Christian', 'Bale', 'm')
student_3.courses_in_progress += ['Pithon', 'JS', 'C']
student_3.finished_courses += ['Django']
student_3.rate_lw(lecturer_1,'Python', 7)
student_3.rate_lw(lecturer_2, 'JS', 7)  
student_3.rate_lw(lecturer_3, 'C', 7)



lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python']
    
lecturer_2 = Lecturer('Leo', 'Di')
lecturer_2.courses_attached += ['JC']

lecturer_3 = Lecturer('Bob', 'Dilan')
lecturer_3.courses_attached += ['C']


reviever_1 = Reviever('Coco', 'Junbo')
reviever_1.courses_attached += ['Python']
reviever_1.rate.hw(student_1, 'Python', 9)
reviever_1.rate.hw(student_1, 'C', 8)
reviever_1.rate.hw(student_2, 'Python', 7)
reviever_1.rate.hw(student_2, 'C', 9)
reviever_1.rate.hw(student_3, 'Python', 3)
reviever_1.rate.hw(student_3, 'C', 10)


reviever_2 = Reviever('Adam', 'Lumbert')
reviever_2.courses_attached += ['JS']
reviever_2.rate.hw(student_1, 'JS', 9)
reviever_2.rate.hw(student_2, 'JS', 7)
reviever_2.rate.hw(student_3, 'JS', 5)


student_list = [student_1, student_2, student_3]

def all_student_score():
  score_py_student = []
  score_js_student = []
  score_c_student = []
  for student in student_list:
    for subject, score in student.grades.items():
      if subject == 'Python':
        score_py_student.append(score)
      if subject == 'JS':
        score_js_student.append(score)
      if subject == 'C':
        score_c_student.append(score)
        
    middle_py_student = sum(sum(score_py_student, [])) / len(sum(sum(score_py_student, [])))
    middle_js_student = sum(sum(score_js_student, [])) / len(sum(sum(score_js_student, [])))
    middle_c_student = sum(sum(score_c_student, [])) / len(sum(sum(score_c_student, [])))

  return f'\nСредняя оценка студентов курса Python:{middle_py_student}'\
  f'\nСредняя оценка студентов курса JS:{midlle_js_student}'\
  f'\nСредняя оценка студентов курса C:{middle_c_student}'

lecturer_list = [lecturer_1, lecturer_2, lecturer_3]

def all_lecturer_score():
  score_py_lecturer = []
  score_js_lecturer = []
  score_c_lecturer = []
  for lecturer in lecturer_list:
    for subject, score in lecturer.grades.items():
      if subject == 'Python':
        score_py_lecturer.append(score)
      if subject == 'JS':
        score_js_lecturer.append(score)
      if subject == 'C':
        score_c_lecturer.append(score)


    middle_py_lecturer = sum(sum(score_py_lecturer, [])) / len(sum(sum(score_py_lecturer, [])))
    middle_js_lecturer = sum(sum(score_js_lecturer, [])) / len(sum(sum(score_js_lecturer, [])))
    middle_c_lecturer = sum(sum(score_c_lecturer, [])) / len(sum(sum(score_c_lecturer, [])))

  return f'\nСредняя оценка лекторов курса Python:{middle_py_lecturer}'\
  f'\nСредняя оценка лекторов курса JS:{midlle_js_lecturer}'  
  f'\nСредняя оценка лекторов курса C:{middle_c_lecturer}'


print(student_1, student_2, student_3)
print(lecturer_1, lecturer_2, lecturer_3)
print(reviever_1, reviever_2)

