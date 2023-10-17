def curry_explicit(function, arity):
    if not callable(function):
        raise ValueError(f"{function} must be callable")
    if type(arity) != int or arity < 0:
        raise ValueError("Arity must be int => 0")
    if arity == 0:
        return function

    def function_on(arguments):
        if arity == len(arguments):
            return function(*arguments)

        def curry(argument):
            return function_on([*arguments, argument])

        return curry

    return function_on([])


def uncurry_explicit(function, arity):
    if not callable(function):
        raise ValueError(f"{function} must be callable")
    if type(arity) != int or arity < 0:
        raise ValueError("Arity must be int => 0")

    def uncurry(*arguments):
        if len(arguments) != arity:
            raise ValueError("Arity != the number of arguments! Returned None")
        if arity == 0:
            return function()
        function_result = function(arguments[0])
        for i in range(1, arity):
            function_result = function_result(arguments[i])
        return function_result

    return uncurry
