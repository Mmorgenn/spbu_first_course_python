from src.practice.Pr_10.parser import *


def main():
    user_input = input("Enter the line for analysis: ").split()
    parser_node = parse(user_input)
    pretty_print(parser_node)


if __name__ == "__main__":
    main()
