class Student:
    def __init__(self, name, student_id, grade):
        self._name = name            
        self.__student_id = student_id 
        self.grade = grade
    
    def get_info(self):
        return f"Студент: {self._name}, ID: {self.__student_id}, Оценка: {self.grade}"

student1 = Student("Alexey Pavlov", "S00123", 4.5)

print(student1.get_info())
print(f"Доступ к защищенному имени: {student1._name}") 

try:
    print(student1.__student_id)
except AttributeError as e:
    print(f"Ошибка при попытке прямого доступа к приватному атрибуту: {e}")