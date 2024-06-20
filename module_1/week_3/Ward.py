class Person:
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    def describe(self):
        print(f"Student - Name: {self._name} - YoB: {self._yob}", end=" - ")


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self.__grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Specialist: {self.__specialist}")


class Ward:
    def __init__(self, name):
        self.__name = name
        self.__list_people_in_ward = []

    def add_person(self, person):
        self.__list_people_in_ward.append(person)

    def describe(self):
        print(f"Ward name: {self.__name}")
        for obj in self.__list_people_in_ward:
            obj.describe()

    def count_object(self, object):
        count = 0
        for obj in self.__list_people_in_ward:
            if isinstance(obj, object):
                count += 1
        return count

    def sort_age(self):
        list_people = self.__list_people_in_ward
        for i in range(len(list_people)):
            for j in range(i+1, len(list_people)):
                if list_people[i]._yob < list_people[j]._yob:
                    temp = list_people[i]
                    list_people[i] = list_people[j]
                    list_people[j] = temp

        self.__list_people_in_ward = list_people

    def compute_average_object(self, object):
        list_object = []
        for obj in self.__list_people_in_ward:
            if isinstance(obj, object):
                list_object.append(obj._yob)

        return sum(list_object) / len(list_object)


student = Student("Tu", 2004, "7")
student.describe()

teacher1 = Teacher("ad Vinh", 1986, "AI")
teacher1.describe()

teacher2 = Teacher("TA Thang", 1996, "AI")
teacher2.describe()

teacher3 = Teacher("TA Nguyen", 1996, "Keep track")
teacher3.describe()

doctor1 = Doctor("Cao Huu Thinh", 1979, "Gynecological")
doctor1.describe()

doctor2 = Doctor("Le Hoang", 1990, "Cardiologists")
doctor2.describe()
print()

print("====Add member in a ward====")
ward1 = Ward("Ward1")
ward1.add_person(teacher3)
ward1.add_person(student)
ward1.add_person(teacher1)
ward1.add_person(doctor1)
ward1.add_person(teacher2)
ward1.add_person(doctor2)
ward1.describe()
print()

print("=====Count people method======")
print(f"Number of doctors: {ward1.count_object(Doctor)}")
print(f"Number of teachers: {ward1.count_object(Teacher)}")
print(f"Number of students: {ward1.count_object(Student)}")

print("=====Sort list=====")
print("After sorting Age of Ward1 people ")
ward1.sort_age()
ward1.describe()
print()

print("=====Average list=====")
print(f"Average year of birth ( teachers ): {
      round(ward1.compute_average_object(Teacher), 1)}")
print(f"Average year of birth ( doctors ): {
      round(ward1.compute_average_object(Doctor), 1)}")
print(f"Average year of birth ( students ): {
      round(ward1.compute_average_object(Student), 1)}")
