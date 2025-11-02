
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        raise NotImplementedError("Метод calculate_bonus должен быть переопределен в дочернем классе.")

# Дочерний класс 1: Manager
class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.15

class Programmer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.10

employees = [
    Manager("Ivan", 120000),
    Programmer("Maria", 90000),
    Manager("Sergey", 140000)
]

print("\n--- Расчет годовых бонусов ---")
for emp in employees:
    bonus = emp.calculate_bonus()
    print(f"{emp.name} ({emp.__class__.__name__}): Зарплата {emp.salary}, Бонус {bonus:,.2f}")