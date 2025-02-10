def Tri_fusion(lst):
    if len(lst) <= 1:
        return lst
    else:
        m = len(lst) // 2
        List_A = lst[:m]
        List_B = lst[m:]

        List_A = Tri_fusion(List_A)
        List_B = Tri_fusion(List_B)

        return fusion(List_A, List_B)
    
def fusion(List_A, List_B):
    List_F = []

    while List_A != [] and List_B != []:
        if List_A[0] < List_B[0]:
            List_F.append(List_A.pop(0))
        else:
            List_F.append(List_B.pop(0))

    List_F = List_F + List_A + List_B
    
    return List_F

List_C = [10,5,6,9,7,8,4,2,3,6,9,11,12,29,8,12,31,21]

print(Tri_fusion(List_C))