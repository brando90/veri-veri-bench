y = "g"
def gp():
    def p(y):
        def c():
            return y
        return c()
    r = p("param")
    y = "gp"
    return r + "," + p("again") + "," + y
print(gp())
