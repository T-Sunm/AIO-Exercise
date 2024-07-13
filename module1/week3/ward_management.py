from abc import ABC, abstractmethod

class Person:
  def __init__(self, name: str, yob: int) -> None:
    self.__name = name
    self.__yob = yob

  def get_name(self):
    return self.__name

  def set_name(self, name):
    self.__name = name

  def get_yob(self):
    return self.__yob

  def set_yob(self, yob):
    self.__yob = yob

  @abstractmethod
  def describe(self):
    """Mỗi lớp con sẽ phải định nghĩa lại phương thức này."""
    # hàm pass xài nếu khi mình chưa muốn định nghĩa , mình mới tạo ra thôi
    pass

class Student(Person):
  def __init__(self, name: str, yob: int, grade: str) -> None:
    super().__init__(name, yob)
    self.__grade = grade

  def get_grade(self):
    return self.__grade

  def set_grade(self, grade):
    self.__grade = grade

  def describe(self):
    print(
        f"Student - Name: {self.get_name()} - Yob: {self.get_yob()} - Grade: {self.__grade}")

class Teacher(Person):
  def __init__(self, name: str, yob: int, subject: str) -> None:
    super().__init__(name, yob)
    self.__subject = subject

  def get_subject(self):
    return self.__subject

  def set_subject(self, subject):
    self.__subject = subject

  def describe(self):
    print(
        f"Teacher - Name: {self.get_name()} - Yob: {self.get_yob()} - Subject: {self.__subject}")

class Doctor(Person):
  def __init__(self, name: str, yob: int, specialist: str) -> None:
    super().__init__(name, yob)
    self.__specialist = specialist

  def get_specialist(self):
    return self.__specialist

  def set_specialist(self, specialist):
    self.__specialist = specialist

  def describe(self):
    print(
        f"Doctor - Name: {self.get_name()} - Yob: {self.get_yob()} - Specialist: {self.__specialist}")

class Ward:
  def __init__(self, name) -> None:
    self.__name = name
    self.__people = []

  def add_person(self, person):
    self.__people.append(person)

  def set_name(self, name):
    self.__name = name

  def get_name(self):
    return self.__name

  def describe(self):
    print("Ward Name: " + self.__name)
    for person in self.__people:
      person.describe()

  def count_doctor(self):
    count = 0
    for person in self.__people:
      if isinstance(person, Doctor):
        count += 1
    return count

  def sort_age(self):
    self.__people.sort(key=lambda x: x.get_yob(), reverse=True)

  def compute_average(self):
    average = 0
    length = 0
    for person in self.__people:
      if isinstance(person, Teacher):
        average += person.get_yob()
        length += 1
    return average / length


# Examples
# 2(a)
student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()

doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor1.describe()

print()

# 2(b)
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

# 2(c)
print(f"\nNumber of doctors: {ward1.count_doctor()}")

# 2(d)
print("\n After sorting Age of Ward1 people ")
ward1.sort_age()
ward1.describe()

# 2(e)
print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
