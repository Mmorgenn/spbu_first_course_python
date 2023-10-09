def curry_explicit(function_name, arity: int):
    if arity < 0:
        print(f"Arity cannot be {arity}! Returned None")
        return None
    if arity == 0:
        return lambda: function_name()

    def function_on(arguments):
        if arity == len(arguments):
            return function_name(*arguments)

        def curry(argument):
            return function_on([*arguments, argument])

        return curry

    return function_on([])


def uncurry_explicit(function_name, arity: int):
    if arity < 0:
        print(f"Arity cannot be {arity}! Returned None")
        return None

    def uncurry(*arguments):
        if len(arguments) != arity:
            print("Arity != the number of arguments! Returned None")
            return None
        elif arity == 0:
            return function_name()
        function_result = function_name(arguments[0])
        for i in range(1, arity):
            function_result = function_result(arguments[i])
        return function_result

    return uncurry


if __name__ == "__main__":
    f2 = curry_explicit((lambda x, y, z: f"<{x},{y},{z}>"), 3)
    f3 = curry_explicit((lambda x: f"<{x}>"), 1)
    h3 = curry_explicit(print, 0)
    g2 = uncurry_explicit(f2, 3)
    h3()
    print(uncurry_explicit(f3, -10))
    print(uncurry_explicit(f3, 2)(123))
    print(f2(123)(456)(562))
    print(g2(123, 456, 562))
