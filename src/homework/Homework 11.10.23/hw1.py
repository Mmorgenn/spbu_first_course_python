def curry_explicit(function, arity):
    if not callable(function):
        print(f"{function} is not function! Returned None")
        return None
    elif not type(arity) == int or arity < 0:
        print("Arity should be int > 0! Returned None")
        return None
    elif arity == 0:
        return function()

    def function_on(arguments):
        if arity == len(arguments):
            return function(*arguments)

        def curry(argument):
            return function_on([*arguments, argument])

        return curry

    return function_on([])


def uncurry_explicit(function, arity):
    if not callable(function):
        print(f"{function} is not function! Returned None")
        return None
    if not type(arity) == int or arity < 0:
        print("Arity should be int > 0! Returned None")
        return None

    def uncurry(*arguments):
        if len(arguments) != arity:
            print("Arity != the number of arguments! Returned None")
            return None
        elif arity == 0:
            return function()
        function_result = function(arguments[0])
        for i in range(1, arity):
            function_result = function_result(arguments[i])
        return function_result

    return uncurry
