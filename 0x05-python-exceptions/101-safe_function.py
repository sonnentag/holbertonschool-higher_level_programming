#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        ret = fct(*args)
    except Exception as err:
        print('Exception:', err)
        ret = None
    return(ret)
