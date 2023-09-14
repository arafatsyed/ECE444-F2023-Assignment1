from q4_functions import utils

# reversed function tests
def reverse_unit_test():
    inst = utils()
    
    result1 = inst.reversed("1231")
    assert result1 == "invalid"
    
    result2 = inst.reversed(123.31)
    assert result2 == "invalid"

    result3 = inst.reversed(12345)
    assert result3 == 54321

# formatter function tests
def formatter_unit_test():
    inst = utils()
    
    result1 = inst.formatter("1231")
    assert result1 == "invalid"
    
    result2 = inst.formatter(123.31)
    assert result2 == "invalid"

    result3_bin,result3_oct = inst.formatter(234)
    assert result3_bin == '0b11101010'
    assert result3_oct == '0o352'

if __name__ == '__main__':
    reverse_unit_test()
    formatter_unit_test()
    print("SUCCESS")
