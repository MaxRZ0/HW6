f_elem = int(input())
step = int(input())
quantity_num = int(input())

def proggres_ar(f_elem, step, quantity_num):
    ar_prog = f_elem
    prog_array = [f_elem]
    for i in range(quantity_num-1):
        ar_prog += step
        prog_array.append(ar_prog)
    return prog_array

print(proggres_ar(f_elem, step, quantity_num))
