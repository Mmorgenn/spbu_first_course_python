def quadratic_equation_solve(num_a, num_b, num_c):
    discriminant = num_b**2 - 4 * num_a * num_c
    if discriminant >= 0:
        return sorted(
            {(-num_b + sign * discriminant**0.5) / 2 / num_a for sign in (1, -1)}
        )
    raise ArithmeticError("Discriminant must be non-negative")


def linear_equation_solve(num_k, num_b):
    return [-num_b / num_k]


def choose_solution(first_num, second_num, third_num):
    if first_num == 0 and second_num == 0:
        raise ValueError("Leading coefficients must be non-zero")
    if first_num == 0:
        return linear_equation_solve(second_num, third_num)
    else:
        return quadratic_equation_solve(first_num, second_num, third_num)


def check_numbers(nums):
    if len(nums) != 3:
        raise TypeError("The numbers must be 3")
    for num in nums:
        num_check = num
        if num[0] == "-":
            num_check = num[1:]
        if num_check.count(".") == 1 and all(
            [i.isdigit() for i in num_check.split(".")]
        ):
            continue
        if num_check.isdigit():
            continue
        raise SyntaxError("Each element must be float")
    return [float(num) for num in nums]


def start():
    input_nums = input("Введите 3 числа: ").split()
    try:
        nums = check_numbers(input_nums)
    except TypeError:
        print("Чисел должно было быть ровно 3")
        return False
    except SyntaxError:
        print("Не все эллементы которые вы ввели являются числами")
        return False
    try:
        answer = (", ").join(str(num) for num in choose_solution(*nums))
        print(f"Решениe: {answer}")
    except ValueError:
        print(
            "Введенные данные не подходят ни для квадратного уравнения, ни для линейного"
        )
        return False
    except ArithmeticError:
        print("Уравнение не имеет корней")
        return False
    return True


if __name__ == "__main__":
    while True:
        start()
