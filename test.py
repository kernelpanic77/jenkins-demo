from utils import add, mul, sub

def tests():
    res = mul(69, 69)
    expected = 4761
    assert res == expected 
    print("add(1, 2) = ", res, "\nPass")

    res = sub(7, 3)
    expected = 4
    assert res == expected 
    print("add(2, 5) = ", res, "\nPass")


if __name__ == "__main__":
    try:
        tests()
    except Exception as e:
        print('Errors encountered')
        print(str(e))