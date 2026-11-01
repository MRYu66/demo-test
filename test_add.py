from add import add

def test_add():
    assert add(2, 3) == 5
    print("测试通过！")

if __name__ == "__main__":
    test_add()