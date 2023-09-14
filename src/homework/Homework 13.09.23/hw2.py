from math import *


def find_vectors():
    vector_1_input = (input("Введите первый вектор через пробел, без запятых (Например: x1 y2 z3): "))
    vector_2_input = (input("Введите второй вектор через пробел, без запятых (Например: x1 y2 z3): "))
    try:
        vector_1_otput = [int(x) for x in vector_1_input.split()]
        vector_2_otput = [int(y) for y in vector_2_input.split()]
        return(vector_1_otput, vector_2_otput)
    except Exception:
        print("Была допущена ошибка при вводе векторов! Попробуйте еще раз.")
        return find_vectors()


def scalar_product():
    vector_1, vector_2 = find_vectors()
    if len(vector_1) == len(vector_2) and len(vector_1) != 0:
        return sum(vector_1[i] * vector_2[i] for i in range(len(vector_1)))
    else:
        print("Ошибка в заданных векторах! Попробуйте еще раз.")
        return scalar_product()


def angle_vectors():
    vector_1, vector_2 = find_vectors()
    if len(vector_1) == len(vector_2):
        if len(vector_1)==0: return 0
        else: return acos((sum(vector_1[i] * vector_2[i] for i in range(len(vector_1))))/(sum(x**2 for x in vector_1)**0.5)/(sum(y**2 for y in vector_2)**0.5))*180/pi
    else:
        print("Векторы разных размеров! Попробуйте еще раз.")
        return scalar_product()


def len_vectors():
    vector_1, vector_2 = find_vectors()
    return [sum(x**2 for x in vector_1)**0.5, sum(y**2 for y in vector_2)**0.5]


def line_matrix_create(line, count_columns):
    try:
        line_matrix = (input(f"Введите содержания {line + 1} строки через пробел, без запятых (Например: a1 a2 a3): "))
        if len(line_matrix.split()) == count_columns:
            return [int(a) for a in line_matrix.split()]
        else:
            print("Эта строка не добавлена в матрицу")
            return line_matrix_create(line, count_columns)
    except Exception:
        print("Эта строка не добавлена в матрицу")
        return line_matrix_create(line, count_columns)


def matrix_create():
    try:
        count_lines = int(input("Введите количество строк в матрице: "))
        count_columns = int(input("Введите количество cтолбцов в матрице: "))
        return [line_matrix_create(line, count_columns) for line in range(count_lines)]
    except Exception:
        print("Ошибка! Попробуй еще раз")
        return matrix_create()


def matrix_addition():
    print("Задай первую матрицу")
    matrix_1 = matrix_create()
    print("Задай вторую матрицу")
    matrix_2 = matrix_create()
    if len(matrix_1) == len(matrix_2) and  len(matrix_1[0]) == len(matrix_2[0]):
        return [[matrix_1[row][col] + matrix_2[row][col] for col in range(len(matrix_1[row]))] for row in range(len(matrix_1))]
    else:
        print("Две матрицы не равны! Попробуй еще раз.")
        return matrix_addition()


def matrix_multiplication():
    print("Задай первую матрицу")
    matrix_1 = matrix_create()
    print("Задай вторую матрицу")
    matrix_2 = matrix_create()
    if len(matrix_1) == len(matrix_2[0]) and len(matrix_1)<=len(matrix_1[0]):
        matrix_1, matrix_2 = matrix_2, matrix_1
    if len(matrix_2) == len(matrix_1[0]) and len(matrix_1)>=len(matrix_1[0]):
        return [[sum(i_1 * i_2 for i_1, i_2 in zip(matrix_1_row, matrix_2_col)) for matrix_2_col in zip(*matrix_2)] for matrix_1_row in matrix_1]
    else:
        print("Эти матрицы нельзя перемножить! Попробуй еще раз.")
        return matrix_multiplication()


def matrix_transponition():
    print("Задайте матрицу")
    matrix = matrix_create()
    new_matrix = []
    for column in range(len(matrix[0])):
        new_matrix.append([matrix[i][column] for i in range (len(matrix))])
    return new_matrix


def matrix_output(matrix):
    for line in matrix:
        print(" ".join(map(str, line)))


def start_vector():
    try:
        vector_func = int(input("Введите цифру от 1 до 3: \n(1) Скалярное произведение векторов \n(2) Длины векторов \n(3) Угол между векторами \n"))
        if vector_func == 1: print(f"Скалярное произведение двух векторов: {scalar_product()}")
        elif vector_func == 2: print(f"Длина двух векторов: {', '.join(map(str, len_vectors()))}")
        elif vector_func == 3: print(f"Угол между двумя векторами: {angle_vectors()}")
        else: print("Такой функции нет!")
    except Exception:
        print("Такой функции нет!")
        start_vector()


def start_matrix():
    try:
        matrix_func = int(input("Введите цифру от 1 до 3: \n(1) Транспонирование матрицы \n(2) Сложение матриц \n(3) Умножение матриц \n"))
        if matrix_func == 1: matrix_output(matrix_transponition())
        elif matrix_func == 2: matrix_output(matrix_addition())
        elif matrix_func == 3: matrix_output(matrix_multiplication())
        else: print("Такой функции нет!")
    except Exception:
        print("Такой функции нет!")
        start_matrix()


def start():
    while True:
            try:
                vector_or_matrix = int(input("Выберите цифру от 1 до 2: \n(1) Вектора \n(2) Матрица \n"))
                if vector_or_matrix == 1: start_vector()
                elif vector_or_matrix == 2: start_matrix()
            except Exception: print("Ошибка!")


if __name__ == "__main__":
    start()
