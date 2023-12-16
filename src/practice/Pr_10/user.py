from src.practice.Pr_10.parser import *


def main():
    user_input = input("Enter the line for analysis: ").split()
    try:
        parser_node = parse(user_input)
    except ValueError as e:
        print(f"Error due to reason: {e}")
        return
    pretty_print(parser_node)


if __name__ == "__main__":
    main()
