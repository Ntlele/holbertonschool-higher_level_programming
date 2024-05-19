#!/usr/bin/pyhton3

def safe_print_division(a, b):
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        return None
    finally:
        try:
            print(result)
        except UnboundLocalError:
            pass
    return result
