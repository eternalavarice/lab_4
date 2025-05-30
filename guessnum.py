import random
import time

def guess_the_number():
    number = random.randint(1, 100)
    print("Загадано число от 1 до 100. Попробуй угадать.")

    attempts = 0
    start_time = time.time()

    while True:
        try:
            guess = int(input("Твой вариант: "))
            attempts += 1

            if guess < number:
                print("Слишком маленькое число.")
            elif guess > number:
                print("Слишком большое число.")
            else:
                print(f"Ты угадал! Это было число {number}.")
                break
        except ValueError:
            print("Введите целое число.")

    end_time = time.time()
    duration = round(end_time - start_time, 2)

    # Сохраняем статистику в файл
    with open("statistics.txt", "a", encoding='utf-8') as file:
        file.write(f"Попыток: {attempts}, Время: {duration} сек, Результат: Угадал\n")

    print(f"\nСтатистика сохранена. Попыток: {attempts}, Время: {duration} сек")

# Запуск
guess_the_number()
