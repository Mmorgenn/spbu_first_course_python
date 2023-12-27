from dataclasses import dataclass


@dataclass
class ParserNode:
    value: str
    children: list["ParserNode"]


def _start(tokens: list[str], index: int):
    t_node, t_index = _t(tokens, index)
    sum_node, new_index = _sum(tokens, t_index)
    return ParserNode("START", [t_node, sum_node]), new_index


def _sum(tokens: list[str], index: int):
    if index < len(tokens) and tokens[index] == "+":
        index += 1
        t_node, t_index = _t(tokens, index)
        sum_node, new_index = _sum(tokens, t_index)
        return ParserNode("SUM", [ParserNode("+", []), t_node, sum_node]), new_index
    else:
        return ParserNode("SUM", [ParserNode("eps", [])]), index


def _t(tokens: list[str], index: int):
    token_node, token_index = _token(tokens, index)
    prod_node, prod_index = _prod(tokens, token_index)
    return ParserNode("T", [token_node, prod_node]), prod_index


def _prod(tokens: list[str], index: int):
    if index < len(tokens) and tokens[index] == "*":
        index += 1
        token_node, token_index = _token(tokens, index)
        prod_node, new_index = _prod(tokens, token_index)
        return (
            ParserNode("PROD", [ParserNode("*", []), token_node, prod_node]),
            new_index,
        )
    else:
        return ParserNode("PROD", [ParserNode("eps", [])]), index


def _token(tokens: list[str], index: int):
    if index >= len(tokens):
        raise ValueError(f"The element under index {index} is missing!")
    if tokens[index] == "(":
        start_node, start_index = _start(tokens, index + 1)
        if start_index < len(tokens) and tokens[start_index] == ")":
            return (
                ParserNode(
                    "TOKEN", [ParserNode("(", []), start_node, ParserNode(")", [])]
                ),
                start_index + 1,
            )
        raise ValueError("')' is missing")
    elif tokens[index].isdigit():
        token_node = ParserNode(f"id({tokens[index]})", [])
        return ParserNode("TOKEN", [token_node]), index + 1
    raise ValueError(f"Incorrect symbol: {tokens[index]}. Must be digit")


def parse(tokens: list[str]) -> ParserNode:
    index = 0
    result_tree, result_index = _start(tokens, index)
    if result_index == len(tokens):
        return result_tree
    raise ValueError(f"The line is broken!")


def pretty_print(tree: ParserNode):
    result = []

    def get_result(node, indent=0):
        result.append(("...." * indent + str(node.value)))
        for child in node.children:
            get_result(child, indent + 1)

    get_result(tree)
    print(*result, sep="\n")
