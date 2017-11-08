def intersect(A, B):
    l1, l2 = 0, 0
    answer = []

    while (l1 < len(A) and l2 < len(B)):
        if (A[l1] == B[l2]):
            answer.append(A[l1])
            l1 += 1
            l2 += 1
        elif (A[l1] < B[l2]):
            l1 += 1
        else:
            l2 += 1

    print(answer)
    return answer


intersect([1, 2, 3], [1, 2])
