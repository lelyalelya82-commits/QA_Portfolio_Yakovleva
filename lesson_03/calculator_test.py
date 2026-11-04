from lesson_04.lesson4.calculator import calculator

calculator = calculator()

# + +
# - -
# - +
# . .
# n 0

@pytest.mark.parametrize('num1, num2, result', [(4,5,9), (-6,-10,-16),(-6, 6,0)(5.6, 4.29, 9.9),(10, 0, 10)])
def test_avg_empty_list():
    calculator= Calculator()
    numbers=[]
    res = calculatorfvg(numbers)
    assert==0

res = calculator.sum(4, 5)
assert res == 9

res = calculator.sum(-10, -6)
assert res == -16

res = calculator.sum(-6, 6)
assert res == 0

res = calculator.sum(5.6, 4.3)
res = round(res, 1)
assert res == 9.9

res = calculator.sum(10, 0)
assert res == 10

numbers = []
res = calculator.avg(numbers)
assert res ==0

print("finish")


res = calculator.div(10, 0)
assert res == none
