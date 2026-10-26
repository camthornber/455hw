def squared_matrix(A):
    total = 0
    for row in A:
        for col in row:
            total += col ** 2
    return total

A = [
    [12.2, 1.2, 2.4],
    [2, 3, 4],
    [2.5, 6.2, 3.4]
]

print(squared_matrix(A))

def decimal_binary(num): 
    decint = int(num)
    decfrac = num - decint 

    #integer part 
    if decint == 0: 
        binint = "0" 
    else: 
        binint = ""
        while decint > 0: 
            rem = decint % 2 
            binint = str(rem) + binint 
            decint = decint // 2 

    #decimal part
    if decfrac == 0: 
        return binint 
    binfrac = "" 
    for i in range(10): #truncated
        decfrac = decfrac * 2 
        rem = int(decfrac)
        binfrac += str(rem) 
        decfrac = decfrac - rem 
        if decfrac == 0: 
            break 

    return binint + "." + binfrac 

print(decimal_binary(20.25))
print(decimal_binary(21.45))