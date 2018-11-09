def f(n):
    print("Number received:", n)
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        print("---- First recursion ----")
        a = f(n-1)
        print("---- Second recursion ----")
        b = f(n-2)
        print(" a=:",a,"; b=",b,"; returning:", a+b)
        return a + b

print("Final f(4)=", f(4))