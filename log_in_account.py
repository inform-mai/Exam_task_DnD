import os
import sys

# Имя файла с аккаунтами
ACCOUNTS_FILE = "accounts.txt"


def generate_initial_accounts():
    """Генерирует начальный файл с 5 аккаунтами"""
    initial_accounts = [
        ("Supervasya", "1111"),
        ("Mamalop", "1234"),
        ("Superclaster", "4321"),
        ("Vanya228", "8888"),
        ("AvtomatpoInformatike", "55555")
    ]
    with open(ACCOUNTS_FILE, "w", encoding="utf-8") as f:
        for login, password in initial_accounts:
            f.write(f"{login}:{password}\n")


def load_accounts():
    """Загружает все аккаунты из файла в словарь"""
    accounts = {}
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "r", encoding=" utf-8") as f:
            for line in f:
                line = line.strip()
                if line and ":" in line:
                    login, password = line.split(":", 1)
                    accounts[login] = password
    return accounts


def save_account(login, password):
    """Добавляет новый аккаунт в файл"""
    with open(ACCOUNTS_FILE, "a", encoding="utf-8") as f:
        f.write(f"{login}:{password}\n")


def register():
    """Регистрация нового пользователя"""
    accounts = load_accounts()

    while True:
        login = input("Введите логин для регистрации: ").strip()
        if not login:
            print("Логин не может быть пустым!")
            continue
        if login in accounts:
            print("Этот логин уже занят. Попробуйте другой.")
            continue
        break

    while True:
        password = input("Введите пароль: ").strip()
        if not password:
            print("Пароль не может быть пустым!")
            continue
        break

    save_account(login, password)
    print(f"Аккаунт '{login}' успешно зарегистрирован!")
    return login, password


def login():
    """Авторизация пользователя"""
    accounts = load_accounts()

    print("\n=== Вход в профиль ===")
    while True:
        login = input("Введите логин: ").strip()
        password = input("Введите пароль: ").strip()

        if login in accounts and accounts[login] == password:
            print(f"Добро пожаловать, {login}!")
            return login
        else:
            print("Неверный логин или пароль. Попробуйте снова.")


def main():
    # Генерируем файл с аккаунтами, если его нет
    if not os.path.exists(ACCOUNTS_FILE):
        generate_initial_accounts()
        print(f"Создан файл '{ACCOUNTS_FILE}' с 5 начальными аккаунтами.")

    print("Добро пожаловать!")
    print("1. Зарегистрировать новый аккаунт")
    print("2. Войти в существующий аккаунт")

    while True:
        choice = input("Выберите действие (1 или 2): ").strip()
        if choice == "1":
            register()
            break
        elif choice == "2":
            break
        else:
            print("Введите 1 или 2.")

    # Авторизация (обязательна для всех)
    current_user = login()

    # Основная часть программы (после успешного входа)
    print(f"\nВы вошли в систему как '{current_user}'.")
    print("Теперь вы можете использовать программу.")


if __name__ == "__main__":
    main()

import branch_1