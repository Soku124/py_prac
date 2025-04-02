def print_out(a):
    print(f"Outer: {a}")

    def print_in():
        print(f"\tInner: {a}")
    
    return print_in

test2 = print_out("test")

del print_out

test2()