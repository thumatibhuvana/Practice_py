def action(x,y,z):
    if z == "add":
        z = x+y
    elif z == "sub":
        z = x-y
    elif z == "mul":
        z = x*y
    elif z == "div":
        z = x/y
    return z
