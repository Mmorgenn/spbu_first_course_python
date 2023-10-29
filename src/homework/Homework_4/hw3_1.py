from src.homeworks.Homework_4.hw3 import create, get_size, view_top, push, pop


def get_top(queue):
    try:
        result = view_top(queue)
        print(f"Верхний элемент очереди: {result}")
    except AttributeError:
        print("Верхнего элемента нет! Очередь пуста.")


def get_pop(queue):
    try:
        result = pop(queue)
        print(f"Удаленый элемент: {result}")
    except AttributeError:
        print("Элемент не удален! Очередь пуста.")


if __name__ == "__main__":
    print("Созданим пустую очередь 1, 2, 3")
    queue_test = create()
    push(queue_test, 1)
    push(queue_test, 2)
    push(queue_test, 3)
    print(f"Размер оереди {get_size(queue_test)}")
    get_top(queue_test)
    get_pop(queue_test)
    print(f"Размер оереди {get_size(queue_test)}")
    get_top(queue_test)
    get_pop(queue_test)
    print(f"Размер оереди {get_size(queue_test)}")
    get_top(queue_test)
    get_pop(queue_test)
    print(f"Размер оереди {get_size(queue_test)}")
    get_top(queue_test)
    get_pop(queue_test)
