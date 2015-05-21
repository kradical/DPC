def check_sorting_network(A):
	number_of_wires = A.pop(0)
	number_of_comparators = A.pop(0)	   

	for N in range(2**number_of_wires):
	    test_sequence = [1 & int(N) >> i for i in range(number_of_wires)[::-1]]
	    
	    for N in range(number_of_comparators):
		compare_swap(test_sequence, A[2*N], A[2*N+1])
	    
	    if is_sorted(test_sequence):
		pass
	    else:
		print("Invalid Network")
		return
	print("Valid Network")


def compare_swap(A, a, b):  
	if(A[a] > A[b]):
		(A[a], A[b]) = (A[b], A[a])

def is_sorted(lst, key=lambda x, y: x < y):
	for i, el in enumerate(lst[1:]):
		if key(el, lst[i]):         
		    return False
	return True

test_input1 = [4, 5, 0, 2, 1, 3, 0, 1, 2, 3, 1, 2]
test_input2 = [
                8, 19,
                0, 2,
                1, 3,
                0, 1,
                2, 3,
                1, 2,
                4, 6,
                5, 7,
                4, 5,
                6, 7,
                5, 6,
                0, 4,
                1, 5,
                2, 6,
                3, 7,
                2, 4,
                3, 5,
                1, 2,
                3, 4,
                6, 7
                ]
test_input3 = [
                16, 60,
                0, 1,
                2, 3,
                4, 5,
                6, 7,
                8, 9,
                10, 11,
                12, 13,
                14, 15,
                0, 2,
                1, 3,
                4, 6,
                5, 7,
                8, 10,
                9, 11,
                12, 14,
                13, 15,
                0, 4,
                1, 5,
                2, 6,
                3, 7,
                8, 12,
                9, 13,
                10, 14,
                11, 15,
                0, 8,
                1, 9,
                2, 10,
                3, 11,
                4, 12,
                5, 13,
                6, 14,
                7, 15,
                5, 10,
                6, 9,
                3, 12,
                7, 11,
                13, 14,
                1, 2,
                4, 8,
                1, 4,
                7, 13,
                2, 8,
                11, 14,
                2, 4,
                5, 6,
                9, 10,
                11, 13,
                3, 8,
                7, 12,
                6, 8,
                3, 5,
                7, 9,
                10, 12,
                3, 4,
                5, 6,
                7, 8,
                9, 10,
                11, 12,
                6, 7,
                12, 13
                ]
test_input4 = [
                16, 60,
                0, 1,
                2, 3,
                4, 5,
                6, 7,
                8, 9,
                10, 11,
                12, 13,
                14, 15,
                0, 2,
                1, 3,
                4, 6,
                5, 7,
                8, 10,
                9, 11,
                12, 14,
                13, 15,
                0, 4,
                1, 5,
                2, 6,
                3, 7,
                8, 12,
                9, 13,
                10, 14,
                11, 15,
                0, 8,
                1, 9,
                2, 10,
                3, 11,
                4, 12,
                5, 13,
                6, 14,
                7, 15,
                5, 10,
                6, 9,
                3, 12,
                7, 11,
                13, 14,
                1, 2,
                4, 8,
                1, 4,
                7, 13,
                2, 8,
                11, 14,
                2, 4,
                5, 6,
                9, 10,
                11, 13,
                3, 8,
                7, 12,
                6, 8,
                3, 5,
                7, 9,
                10, 12,
                3, 4,
                5, 6,
                7, 8,
                9, 10,
                11, 12,
                6, 7,
                8, 9
                ]
check_sorting_network(test_input4)
