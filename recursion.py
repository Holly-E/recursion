
def triangular_sum(num):
    """
    Computes arithmetic sum.
    Returns 0 + 1 + ... + (num - 1) + num
    """
    if num == 0:
        return 0
    else:
        return num + triangular_sum(num - 1)

def test_triangular_sum():
    """
    Some test cases for triangular_sum
    """
    print "Computed:", triangular_sum(0), "Expected: 0"
    print "Computed:", triangular_sum(1), "Expected: 1"
    print "Computed:", triangular_sum(3), "Expected: 6"
    print "Computed:", triangular_sum(10), "Expected: 55"

test_triangular_sum()


def number_of_threes(num):
    """
    Returns the number of times the digit 3 appears
    in the decimal representation of a non-negative integer
    """
    if len(str(num)) == 0:
        return 0

    string = str(num)
    if string[0] == "3":
        return 1 + number_of_threes(string[1:])
    else:
        return number_of_threes(string[1:])

def test_number_of_threes():
    """
    test cases for number of threes
    """
    print
    print "Computed:", number_of_threes(0), "Expected: 0"
    print "Computed:", number_of_threes(2345), "Expected: 1"
    print "Computed:", number_of_threes(3298333233), "Expected: 6"
    print "Computed:", number_of_threes(103231), "Expected: 2"

test_number_of_threes()

def is_member(my_list, elem):
    """
    Returns true if elem is a member of my_list and False otherwise.
    """
    if len(my_list) == 0:
        return False

    current_elem = my_list[0]
    if current_elem == elem:
        return True
    else:
        return is_member(my_list[1:], elem)

def test_is_member():
    """
    Some test cases for is_member
    """
    print
    print "Computed:", is_member([], 1), "Expected: False"
    print "Computed:", is_member([1], 1), "Expected: True"
    print "Computed:", is_member(['c', 'a', 't'], 't'), "Expected: True"
    print "Computed:", is_member(['c', 'a', 't'], 'd'), "Expected: False"

test_is_member()

def remove_x(my_string):
    """
    Deletes all occurrences of the character 'x' from this string.
    """
    if len(my_string) == 0:
        return ""

    if my_string[-1] == 'x':
        return remove_x(my_string[:-1])
    else:
        return remove_x(my_string[:-1]) + my_string[-1]

def test_remove_x():
    """
    Some test cases for remove_x
    """
    print
    print "Computed:", "\"" + remove_x("") + "\"", "Expected: \"\""
    print "Computed:", "\"" + remove_x("cat") + "\"", "Expected: \"cat\""
    print "Computed:", "\"" + remove_x("xxx") + "\"", "Expected: \"\""
    print "Computed:", "\"" + remove_x("dxoxg") + "\"", "Expected: \"dog\""

test_remove_x()
