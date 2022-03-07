# Yongdong Xi
def r_max(nest_lst):
    least = 0
    for x in nest_lst:
        if type(x) == list:
            least = r_max(x)
        elif least < x:
            least = x
    return least




lst = [1, 2, 3, [24, 31], 5]
print(r_max(lst))