

def close_number(num1,num2,num3):
    diff_12= abs(num1-num2)
    diff_23= abs(num2-num3)
    diff_31= abs(num3-num1)

    if diff_12 == 1:
        if diff_23 >= 2 and diff_31 >= 2:
            return True
        else:
            return False

    elif diff_23 == 1:
        if diff_12 >=2 and diff_31 >= 2:
            return True
        else:
            return False

    elif diff_31 == 1:
        if diff_12 >=2 and diff_23 >= 2:
            return True
        else:
            return False

    else:
        return False
    
    
print(close_number(5,4,2))
