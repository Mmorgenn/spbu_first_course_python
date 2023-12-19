from dataclasses import dataclass


@dataclass
class FSMachine:
    name: str
    states: dict[int, dict[str, int]]
    current_state: int
    end_states: list[int]


def create_fs_machine(
    name: str,
    states: dict[int, dict[str, int]],
    zero_state: int,
    end_state: list[int],
) -> FSMachine:
    return FSMachine(name, states, zero_state, end_state)


def move_state(fsm: FSMachine, symbol: str) -> bool:
    current_state = fsm.current_state
    current_transfers = fsm.states[current_state]
    for key, value in current_transfers.items():
        if symbol in key:
            fsm.current_state = value
            return True
    return False


def validate_string(fsm: FSMachine, word: str) -> bool:
    zero_state = fsm.current_state
    for symbol in word:
        if not move_state(fsm, symbol):
            fsm.current_state = zero_state
            return False
    validity = fsm.current_state in fsm.end_states
    fsm.current_state = zero_state
    return validity
