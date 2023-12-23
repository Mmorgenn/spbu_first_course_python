from dataclasses import dataclass


@dataclass
class FSMachine:
    name: str
    states: dict[int, dict[str, int]]
    zero_state: int
    end_states: list[int]


def create_fs_machine(
    name: str,
    states: dict[int, dict[str, int]],
    zero_state: int,
    end_state: list[int],
) -> FSMachine:
    return FSMachine(name, states, zero_state, end_state)


def move_state(fsm: FSMachine, symbol: str, current_state: int) -> int | None:
    current_transfers = fsm.states[current_state]
    for symbols, state in current_transfers.items():
        if symbol in symbols:
            return state


def validate_string(fsm: FSMachine, word: str) -> bool:
    state = fsm.zero_state
    for symbol in word:
        state = move_state(fsm, symbol, state)
        if state is None:
            return False
    validity = state in fsm.end_states
    return validity
