a = [25, (1, 2, 3), [1, 2, 3], 'abc', 1254, {1, 2, 3}]
result = {
    25: int,
    (1, 2, 3): tuple,
    [1. 2. 3]: list,
    'abc': str,
    {1. 2. 3}: set,

}
def return_values(data):
    result = {}
    for d in data:
        try:
            result[d] = type(d).__name__
        except TypeError









