def diagonalDifference(a):
    sum_of_diagonal_1=0
    sum_of_diagonal_2=0
    for each_inner_list in range (0,len(a)):
        sum_of_diagonal_1 += a[each_inner_list][each_inner_list]
        sum_of_diagonal_2 += a[each_inner_list][len(a)-each_inner_list-1]
        print("1=",sum_of_diagonal_1)
        print("2=",sum_of_diagonal_2)
    diagonal_abs_difff = abs(sum_of_diagonal_1-sum_of_diagonal_2)
    print("diagonal_abs_difff====",diagonal_abs_difff)

    return diagonal_abs_difff

a=[[11, 2, 4], [4, 5, 6], [10, 8, -12]]
diagonalDifference(a)
