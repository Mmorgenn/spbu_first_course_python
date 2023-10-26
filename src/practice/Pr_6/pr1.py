def quadratic_equation_solve(num_a, num_b, num_c):
    discriminant = num_b**2 - 4 * num_a * num_c
    if discriminant >= 0:
        return {(-num_b + sign * discriminant**0.5) / 2 / num_a for sign in (-1, 1)}
    raise ArithmeticError("Discriminant must be non-negative")


def linear_equation_solve(num_k, num_b):
    return -num_b / num_k


def choose_solution(first_num, second_num, third_num):
    if first_num == 0 and second_num == 0:
        raise ValueError("Leading coefficients must be non-zero")
    if first_num == 0:
        return linear_equation_solve(second_num, third_num)
    else:
        return quadratic_equation_solve(first_num, second_num, third_num)


def check_numbers(nums):
    if len(nums) != 3:
        raise ValueError("The numbers must be 3")
    try:
        nums_float = [float(num) for num in nums]
    except ValueError:
        raise ValueError("Each element must be float")
    if ("inf" or "-inf" or "+inf") in nums:
        raise ValueError("Each element must be float")
    return nums_float


def start():
    input_nums = input("Введите 3 числа: ").split()
    try:
        nums = check_numbers(input_nums)
    except ValueError:
        print(
            "Произошла ошибка! Это могло произойти по нескольким причинам:\n"
            "1)Вы ввели не 3 эллемента\n"
            "2)Не все эллементы которые вы ввели являются стандартными числами (Пример: +2.0 -3 0.5)\n"
            "3)Бесконечность не будет учтена!"
        )
        return
    try:
        answer = choose_solution(*nums)
        if type(answer) == float:
            print(f"Решениe: {answer}")
        else:
            answer_output = (", ").join(str(num) for num in sorted(answer))
            print(f"Решениe: {answer_output}")
    except ValueError:
        print(
            "Введенные данные не подходят ни для квадратного уравнения, ни для линейного"
        )
    except ArithmeticError:
        print("Уравнение не имеет корней")


if __name__ == "__main__":
    while True:
        start()
