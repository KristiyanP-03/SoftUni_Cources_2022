def func_executor(*args):
    function_results = []

    for function, elements in args:
        function_results.append(f"{function.__name__} - {function(*elements)}")

    return '\n'.join(function_results)