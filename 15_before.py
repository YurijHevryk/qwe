users = [
    {"id": 1, "name": "Іван", "age": 25, "role": "user"},
    {"id": 2, "name": "Марія", "age": 30, "role": "admin"},
    {"id": 3, "name": "Петро", "age": 22, "role": "user"},
    {"id": 4, "name": "Олена", "age": 35, "role": "moderator"}
]

def get_users_older_than(age_limit):
    result = []
    for user in users:
        if user["age"] > age_limit:
            result.append(user)
    return result

def get_users_by_role(role):
    result = []
    for user in users:
        if user["role"] == role:
            result.append(user)
    return result

def add_user(user):
    max_id = 0
    for u in users:
        if u["id"] > max_id:
            max_id = u["id"]
    user["id"] = max_id + 1
    users.append(user)

def print_users(user_list):
    for user in user_list:
        print(f"ID: {user['id']}, Ім'я: {user['name']}, Вік: {user['age']}, Роль: {user['role']}")

# Приклад використання
print("Користувачі старші за 25:")
older_users = get_users_older_than(25)
print_users(older_users)

print("\nКористувачі з роллю user:")
user_role = get_users_by_role("user")
print_users(user_role)

# Додавання нового користувача
new_user = {"name": "Анна", "age": 28, "role": "user"}
add_user(new_user)

print("\nВсі користувачі після додавання:")
print_users(users)