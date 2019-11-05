#Make sure to un-comment the function line below when you are done.
#Remember to name your function is_odd
# WRITE YOUR CODE HERE...
def is_odd(x):
    return True if x % 2 != 0 else False

#DO NOT remove lines below here,
#this is designed to test your code.

def test_is_odd():
    assert is_odd(2) == False
    assert is_odd(3) == True
    assert is_odd(8) == False
    assert is_odd(100) == False
    assert is_odd(101) == True
    print("YOUR CODE IS CORRECT!")
#test your code by un-commenting the line(s) below 
test_is_odd()