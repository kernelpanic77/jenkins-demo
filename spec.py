from utils import add, sub, mul

def runner(blob, number):
    return f'Executing Test: {number}: {str(blob)}'

def e2e():
    res = add(1,2)
    expected = 3
    print(runner('add(1,2)', 1), end=' => ')
    assert res == expected 
    print('pass...')

    res = sub(1,1)
    expected = 0
    print(runner('sub(1,1)', 2), end=' => ')
    assert res == expected 
    print('pass...')

    res = mul(1,2)
    expected = 2
    print(runner('mul(1,2)', 3), end=' => ')
    assert res == expected 
    print('pass...')

if __name__ == "__main__":
    try:
        e2e()
    except Exception as e:
        print('Errors encountered')
        print(str(e))