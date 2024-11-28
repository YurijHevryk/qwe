class User:
    def __init__(self, name, age, role):
        self.id = None
        self.name = name
        self.age = age
        self.role = role

    def __str__(self):
        return f"ID: {self.id}, Ім'я: {self.name}, Вік: {self.age}, Роль: {self.role}"

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        """Додавання користувача з автоматичним призначенням ID"""
        user.id = self._generate_next_id()
        self.users.append(user)
        return user

    def _generate_next_id(self):
        """Приватний метод генерації наступного ID"""
        return max([user.id for user in self.users], default=0) + 1

    def find_users_by_criteria(self, criteria):
        """Пошук користувачів за довільним критерієм"""
        return [user for user in self.users if criteria(user)]

    def print_users(self, user_list=None):
        """Виведення списку користувачів"""
        print_list = user_list if user_list is not None else self.users
        for user in print_list:
            print(user)

# Демонстрація використання
def main():
    # Створення менеджера користувачів
    user_manager = UserManager()

    # Додавання початкових користувачів
    initial_users = [
        User("Іван", 25, "user"),
        User("Марія", 30, "admin"),
        User("Петро", 22, "user"),
        User("Олена", 35, "moderator")
    ]

    for user in initial_users:
        user_manager.add_user(user)

    # Пошук користувачів старших за 25
    print("Користувачі старші за 25:")
    older_users = user_manager.find_users_by_criteria(lambda u: u.age > 25)
    user_manager.print_users(older_users)

    # Пошук користувачів з роллю user
    print("\nКористувачі з роллю user:")
    user_role_users = user_manager.find_users_by_criteria(lambda u: u.role == "user")
    user_manager.print_users(user_role_users)

    # Додавання нового користувача
    new_user = User("Анна", 28, "user")
    user_manager.add_user(new_user)

    # Виведення всіх користувачів
    print("\nВсі користувачі:")
    user_manager.print_users()

# Запуск демонстрації
if __name__ == "__main__":
    main()