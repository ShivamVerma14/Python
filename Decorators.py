def new_decorator(original_func):
    
    def wrap_func():
        print('New functionality before original function!')

        original_func()

        print('New functionality after original function!')

    return wrap_func

@new_decorator
def func_needs_decorator():
    print('It needs to be decorated!')

func_needs_decorator()