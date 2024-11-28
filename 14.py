from abc import ABC, abstractmethod

# Базовий клас для співробітників
class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_bonus(self):
        pass

# Клас для штатного співробітника
class Senior(Employee):
    def calculate_bonus(self):
        return self.salary * 0.1  # Бонус 10% від зарплати

# Клас для контрактного співробітника
class Middle(Employee):
    def calculate_bonus(self):
        return self.salary * 0.05  # Бонус 5% від зарплати

# Додати новий тип співробітника - Практикант
class Junior(Employee):
    def calculate_bonus(self):
        return self.salary * 0.02  # Бонус 2% від зарплати

# Функція для обчислення бонусів
def calculate_employee_bonus(employees):
    for employee in employees:
        print(f"{employee.name} отримує бонус: {employee.calculate_bonus()}")

# Використання
employees = [
    Senior("Юрій", 5000),
    Middle("Юра", 3000),
    Junior("Георгій", 1000),
]

calculate_employee_bonus(employees)
