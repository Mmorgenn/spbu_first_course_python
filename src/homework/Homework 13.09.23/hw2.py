from math import *


def find_vectors():
    vector_1_input = (input("Введите первый вектор через пробел, без запятых (Например: x1 y2 z3): "))
    vector_2_input = (input("Введите второй вектор через пробел, без запятых (Например: x1 y2 z3): "))
    if all([i.isdigit() for i in (vector_1_input.split() + vector_2_input.split())]):
        vector_1_otput = [int(x) for x in vector_1_input.split()]
        vector_2_otput = [int(y) for y in vector_2_input.split()]
        return(vector_1_otput, vector_2_otput)
    else:
        print("Была допущена ошибка при вводе векторов! Попробуйте еще раз.")
        return find_vectors()


def scalar_product(vector_1, vector_2):
    if len(vector_1) == len(vector_2) and len(vector_1) != 0:
        return sum(vector_1[i] * vector_2[i] for i in range(len(vector_1)))
    else:
        return "Ошибка в заданных векторах! Попробуйте еще раз."


def len_vectors(vector_1, vector_2):
    return [sum(x**2 for x in vector_1)**0.5, sum(y**2 for y in vector_2)**0.5]


def angle_vectors(vector_1, vector_2):
    if len(vector_1) == len(vector_2):
        if len(vector_1)==0: return 0
        else:
            vectors_len = sum(x ** 2 for x in vector_1) ** 0.5 * sum(y ** 2 for y in vector_2) ** 0.5
            return acos(sum(vector_1[i] * vector_2[i] for i in range(len(vector_1)))/vectors_len)*180/pi
    else:
        return "Векторы разных размеров! Попробуйте еще раз."


def line_matrix_create(line, count_columns):
        line_matrix = (input(f"Введите содержания {line + 1} строки через пробел, без запятых (Например: a1 a2 a3): "))
        if len(line_matrix.split()) == count_columns and all(a.isdigit() for a in line_matrix.split()):
            return [int(a) for a in line_matrix.split()]
        else:
            print("Эта строка не добавлена в матрицу")
            return line_matrix_create(line, count_columns)


def matrix_create():
        count_lines = (input("Введите количество строк в матрице: "))
        count_columns = (input("Введите количество cтолбцов в матрице: "))
        if count_lines.isdigit() and count_columns.isdigit():
            return [line_matrix_create(line, int(count_columns)) for line in range(int(count_lines))]
        else:
            print("Ошибка! Попробуй еще раз")
            return matrix_create()


def matrix_addition(matrix_1, matrix_2):
    if len(matrix_1) == len(matrix_2) and  len(matrix_1[0]) == len(matrix_2[0]):
        return [[matrix_1[row][col] + matrix_2[row][col] for col in range(len(matrix_1[row]))] for row in range(len(matrix_1))]
    else:
        print("Две матрицы не равны! Попробуй еще раз.")
        return "Error"


def matrix_transponition(matrix):
    return [[matrix[i][column] for i in range (len(matrix))] for column in range(len(matrix[0]))]


def matrix_multiplication(matrix_1, matrix_2):
    if len(matrix_1) == len(matrix_2[0]):
        matrix_2 = matrix_transponition(matrix_2)
        return [[scalar_product(line_1, line_2) for line_2 in matrix_2] for line_1 in matrix_1]
    else:
        print("Эти матрицы нельзя перемножить! Попробуй еще раз.")
        return "Error"


def matrix_output(matrix):
    if matrix != "Error":
        for line in matrix:
            print(" ".join(map(str, line)))


def start_vector():
    vector_func = str(input("Введите цифру от 1 до 3: \n(1) Скалярное произведение векторов \n(2) Длины векторов \n(3) Угол между векторами \n"))
    vector_1, vector_2 = find_vectors()
    if vector_func == "1": print(scalar_product(vector_1, vector_2))
    elif vector_func == "2": print(', '.join(map(str, len_vectors(vector_1, vector_2))))
    elif vector_func == "3": print(angle_vectors(vector_1, vector_2))
    else: print("Такой функции нет!")


def start_matrix():
    matrix_func = str(input("Введите цифру от 1 до 3: \n(1) Транспонирование матрицы \n(2) Сложение матриц \n(3) Умножение матриц \n"))
    print("Задай матрицу")
    matrix_1 = matrix_create()
    if matrix_func == "1":
        matrix_output(matrix_transponition(matrix_1))
    elif matrix_func == "2":
        print("Задай вторую матрицу")
        matrix_2 = matrix_create()
        matrix_output(matrix_addition(matrix_1, matrix_2))
    elif matrix_func == "3":
        print("Задай вторую матрицу")
        matrix_2 = matrix_create()
        matrix_output(matrix_multiplication(matrix_1, matrix_2))
    else: print("Такой функции нет!")


def start():
    while True:
        vector_or_matrix = str(input("Выберите цифру от 1 до 2: \n(1) Вектора \n(2) Матрица \n"))
        if vector_or_matrix == "1": start_vector()
        elif vector_or_matrix == "2": start_matrix()

if __name__ == "__main__":
    start()