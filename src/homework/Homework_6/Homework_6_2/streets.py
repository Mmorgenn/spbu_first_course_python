from os.path import exists
from src.homework.Homework_6.avl_tree import *


def check_files(file_input, file_output):
    if exists(file_input) and not exists(file_output):
        return True
    if not exists(file_input):
        print(f"Файл {file_input} ненайден")
    if exists(file_output):
        print(f"Файл {file_output} уже существует!")
    return False


def is_correct_address(address: list[str]) -> bool:
    if len(address) == 3:
        return address[1].isdigit() and address[2].isdigit()
    return False


def create(directory: TreeMap[Value], address: list[str], index: str):
    street, house, building = address
    put(directory, (street, int(house), int(building)), index)


def get(directory: TreeMap[Value], address: list[str]) -> str:
    street, house, building = address
    try:
        index_result = get_value(directory, (street, int(house), int(building)))
    except ValueError:
        return "None"
    return str(index_result)


def delete_block(directory: TreeMap[Value], address: list[str]):
    street, house, block = address
    try:
        remove(directory, (street, int(house), int(block)))
    except ValueError:
        return


def delete_house(directory: TreeMap[Value], street: str, house: int):
    remove_keys(directory, (street, house, 0), (street, house + 1, 0))


def delete_street(directory: TreeMap[Value], street: str):
    remove_keys(directory, (street, 0, 0), (street + "0", 0, 0))


def get_list_addresses(
    directory: TreeMap[Value], address_1: list[str], address_2: list[str]
) -> str:
    street_1, house_1, block_1 = address_1
    street_2, house_2, block_2 = address_2
    try:
        result_list = get_all_keys(
            directory,
            (street_1, int(house_1), int(block_1)),
            (street_2, int(house_2), int(block_2)),
        )
    except ValueError:
        result_list = []
    result = list(map(lambda x: f"{x[0]} {x[1]} {x[2]}", result_list))
    result.append("\n")
    return "\n".join(result)


def rename(directory: TreeMap[Value], old_street: str, new_street: str):
    required_addresses = get_all(
        directory, (old_street, 0, 0), (old_street + "0", 0, 0)
    )
    remove_keys(directory, (old_street, 0, 0), (old_street + "0", 0, 0))
    for address, index in required_addresses:
        put(directory, (new_street, address[1], address[2]), index)


def run_commands(directory: TreeMap[Value], command: str):
    arguments = command.split()
    if arguments[0] != "EXIT" and len(arguments) < 2:
        return "ERROR"
    command = arguments.pop(0)
    match command:
        case "CREATE":
            index = arguments.pop(-1)
            if not is_correct_address(arguments) or not index.isdigit():
                return "ERROR"
            create(directory, arguments, index)

        case "GET":
            if not is_correct_address(arguments):
                return "ERROR"
            return get(directory, arguments) + "\n"

        case "DELETE_BLOCK":
            if not is_correct_address(arguments):
                return "ERROR"
            delete_block(directory, arguments)

        case "DELETE_HOUSE":
            if len(arguments) != 2 or not arguments[1].isdigit():
                return "ERROR"
            delete_house(directory, arguments[0], int(arguments[1]))

        case "DELETE_STREET":
            if len(arguments) != 1:
                return "ERROR"
            delete_street(directory, *arguments)

        case "LIST":
            if (
                not len(arguments) == 6
                or not is_correct_address(arguments[:3])
                or not is_correct_address(arguments[3:])
            ):
                return "ERROR"
            address_1, address_2 = arguments[:3], arguments[3:]
            return get_list_addresses(directory, address_1, address_2)

        case "RENAME":
            if not len(arguments) == 2:
                return "ERROR"
            old_name, new_name = arguments
            rename(directory, old_name, new_name)

        case "EXIT":
            return "$EXIT"


def run_interactive_mode(directory: TreeMap[Value]):
    command = input("Input command: ")
    result = run_commands(directory, command)
    if result:
        match result:
            case "$EXIT":
                return

            case _:
                print(result)
    return run_interactive_mode(directory)


def file_scrolling(directory: TreeMap[Value], file_name_input: str) -> list[str]:
    results = list()
    with open(file_name_input, encoding="utf-8", mode="r") as file_input:
        count_command = int(file_input.readline())
        for command in range(count_command):
            command = file_input.readline()
            result = run_commands(directory, command)
            if result:
                results.append(result)
    return results


def file_writing_results(results: list[str], file_name_output: str):
    with open(file_name_output, "w") as file_output:
        file_output.writelines(result for result in results)


def run_static_mode(
    directory: TreeMap[Value], file_input_name: str, file_output_name: str
):
    results = file_scrolling(directory, file_input_name)
    file_writing_results(results, file_output_name)


def main():
    directory = create_tree_map()
    mode_selector = input("Choose: \n(1) - Interactive mode\n(2) - Static mode\n")
    match mode_selector:
        case "1":
            run_interactive_mode(directory)

        case "2":
            file_input = input("Input file for reading: ")
            file_output = input("Input file for writing: ")
            if check_files(file_input, file_output):
                run_static_mode(directory, file_input, file_output)

        case _:
            print("Error! You must choose 1 or 2")


if __name__ == "__main__":
    main()
