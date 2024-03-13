

def ErrorCheck(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(f"ERROR: {func} {e}\n")
    return wrapper

