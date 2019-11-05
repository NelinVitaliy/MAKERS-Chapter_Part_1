#Make sure to un-comment the square_test() line below
#when you are done.
# WRITE YOUR CODE HERE...
def square_number(number):
    return number ** 2

#DO NOT remove lines below here,
#this is designed to test your code.

def test_square_number():
    assert square_number(2) == 4
    assert square_number(8) == 64
    assert square_number(10) == 100
    print("YOUR CODE IS CORRECT!")
#test your code by un-commenting the line(s) below
test_square_number()