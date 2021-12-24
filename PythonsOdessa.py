outer = input("Outer variable")
inner = input("inner variable")

def formula(outer):
    for item in outer:
        print(f"{item}")


formula(outer)
formula(inner)
formula("234234")