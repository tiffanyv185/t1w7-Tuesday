def greet():
    print("I love coding!")

greet()

scope_out = "outside"

def test_scope():
    print(scope_out)

test_scope()

def test_scope_1():
    scope_in = "Inside"

