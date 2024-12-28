import subprocess

# Команда для запуска только упавших тестов с последнего прогона и сохранения результатов Allure
command = [
    "pytest",
    "-v",
    "--lf",  # Для запуска только упавших тестов
    "--reruns", "0",  # Запрещаем повторные попытки выполнения тестов
    "--alluredir=./allure-failed-results"  # Для сохранения результатов в каталог allure-failed-results
]

# Выполнение команды
try:
    subprocess.run(command, check=True)
    print("Тесты успешно завершены.")
except subprocess.CalledProcessError as e:
    print(f"Ошибка при запуске тестов: {e}")
