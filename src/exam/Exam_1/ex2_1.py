from ex2 import create, head, tail, insert, delete, retrieve, locate


if __name__ == "__main__":
    print("Создаем пустой список")
    my_list = create()
    print(f"Проверим head: {head(my_list)} и tail: {tail(my_list)}")
    print("Добавим эллементы 1, 2, 3")
    insert(my_list, 1, 0)
    insert(my_list, 2, 1)
    insert(my_list, 3, 2)
    print(f"Проверим head: {head(my_list)} и tail: {tail(my_list)}")
    print(f"Попытаемся добавить элемент на 13 позицию: {insert(my_list, 0, 13)}")
    print(f"Попытаемся удалить элемент на 13 позицию: {delete(my_list, 13)}")
    print(f"Индекс элемента 2: {locate(my_list, 2)}")
    print(f"Под вторым индексом элемент: {retrieve(my_list, 2)}")
    print("Удалим элемент под индексом 1")
    delete(my_list, 1)
    print(f"Проверим head: {head(my_list)} и tail: {tail(my_list)}")
    print("Удалим элемент под индексом 1")
    delete(my_list, 1)
    print(f"Проверим head: {head(my_list)} и tail: {tail(my_list)}")
