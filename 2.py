import random

def guess_the_number():
    # Генерируем случайное число от 1 до 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Добро пожаловать в игру 'Угадай число'!")
    print(f"Я загадал число от 1 до 100. У вас есть {max_attempts} попыток, чтобы угадать его.")

    while attempts < max_attempts:
        try:
            user_guess = int(input("Ваше предположение: "))
            attempts += 1

            if user_guess == secret_number:
                print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток!")
                return
            elif user_guess < secret_number:
                print("Слишком маленькое число. Попробуйте еще раз.")
            else:
                print("Слишком большое число. Попробуйте еще раз.")

        except ValueError:
            print("Пожалуйста, введите целое число.")

    print(f"К сожалению, вы исчерпали все попытки. Загаданное число было {secret_number}.")

if __name__ == "__main__":
    guess_the_number()