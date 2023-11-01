def quadratic_equation_solve(num_a, num_b, num_c):
    discriminant = num_b**2 - 4 * num_a * num_c
    if discriminant >= 0:
        return tuple(
            {(-num_b + sign * discriminant**0.5) / 2 / num_a for sign in (-1, 1)}
        )
    raise ArithmeticError("Discriminant must be non-negative")


def linear_equation_solve(num_k, num_b):
    return (-num_b / num_k,)


def get_solution(first_num, second_num, third_num):
    if first_num == 0 and second_num == 0:
        raise ValueError("Leading coefficients must be non-zero")
    if first_num == 0:
        return linear_equation_solve(second_num, third_num)
    else:
        return quadratic_equation_solve(first_num, second_num, third_num)


def parsing_numbers(nums):
    if len(nums) != 3:
        raise ValueError("The numbers must be 3")
    try:
        nums_float = [float(num) for num in nums]
    except ValueError:
        raise ValueError("Each element must be float")
    if ("inf" or "-inf" or "+inf") in nums:
        raise ValueError("Element must not be inf")
    return nums_float


def start():
    input_nums = input("Введите 3 числа: ").split()
    try:
        nums = parsing_numbers(input_nums)
    except ValueError as e:
        print(f"Произошла ошибка! Причина: {e}")
        return
    try:
        answer = get_solution(*nums)
        answer_output = (", ").join(str(num) for num in answer)
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
