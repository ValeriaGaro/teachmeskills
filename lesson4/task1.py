from datetime import datetime
import time

# Создать генератор для заполнения списка
print([i for i in range(1, 51) if i % 5 == 0])

# Создать функцию для генерации списков с аннотациями


def generate_list(end_number: int ) -> list:
    return [i for i in range(0, end_number + 1)]


print(generate_list(10))
print(generate_list(20))


# Создать функцию, которая будет вызываться из генератора и отдавать текущее время


def get_current_time():
    time.sleep(1)
    now = datetime.now()
    return now.strftime("%H:%M:%S")


[get_current_time() for i in range(5)]