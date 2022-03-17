def LSS(arr):
    new_arr = []
    for i in range(0, len(arr)): 
        b = []
        for j in range(i, len(arr)):
            b.append(np.sum(arr[j:j+1]))
            new_arr.append(b[:])
    sum_arr = []
    for h in new_arr:
        sum_arr.append(sum(h))
        indices = [index for index, value in enumerate(sum_arr) if value == max(sum_arr)]
    length = [len(new_arr[i]) for i in indices]
    p = length.index(max(length))
    winner = new_arr[indices[p]]
    print('New Array =' , new_arr )
    return print('Largest Sum =' , max(sum_arr), ', Longest Sequence =' , winner) 
            