def maxset(A):
    result = []
    glo_result = []
    glo_sum, cur_sum = 0, 0
    for i in range(len(A)):
        if A[i] >= 0:
            cur_sum += A[i]
            result.append(A[i])
        else:
            if cur_sum > glo_sum:
                glo_sum = cur_sum
                glo_result = result[:]

            cur_sum = 0
            result = []

    if cur_sum > glo_sum:
        glo_result = result[:]
    return glo_result


A = [1, 2, 5, -7, 2, 3]
print(maxset(A))
