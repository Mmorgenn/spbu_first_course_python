from dataclasses import dataclass


@dataclass
class State:
    transfers: dict[str:int]


@dataclass
class FSMachine:
    alphabet: list[str]
    states: dict[int:State]
    current_state: int
    end_states: list[int]


def create_state(transfers: list[tuple[str, int]]):
    return State({symbol: state for (symbol, state) in transfers})


def create_fs_machine(
    alphabet: list[str],
    states: dict[int : list[tuple[str, int]]],
    zero_state: int,
    end_state: list[int],
) -> FSMachine:
    for position in states.keys():
        states[position] = create_state(states.get(position))
    return FSMachine(alphabet, states, zero_state, end_state)


def move_state(fsm: FSMachine, symbol: str) -> bool:
    if symbol in fsm.alphabet:
        current_state = fsm.current_state
        current_transfers = fsm.states[current_state].transfers
        if symbol in current_transfers.keys():
            fsm.current_state = current_transfers[symbol]
            return True
    return False


def validate_string(fsm: FSMachine, string: str) -> bool:
    zero_state = fsm.current_state
    for symbol in string:
        if not move_state(fsm, symbol):
            fsm.current_state = zero_state
            return False
    validity = fsm.current_state in fsm.end_states
    fsm.current_state = zero_state
    return validity
