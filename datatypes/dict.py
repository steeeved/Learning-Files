squares = {}
for x in range(1000000):
    squares[x] = x*x
print(squares)
print(squares.get(7888))

odd_squares = {x: x*x for x in range(11) if x % 2 == 1}
for i in odd_squares:
    print(odd_squares[i])
print(odd_squares)