from utils import add, mul, sub

def tests():
    res = mul(7, 5)
    expected = 35
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