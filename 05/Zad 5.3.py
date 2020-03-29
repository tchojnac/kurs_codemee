#Nie korzystając z funkcji wbudowanej max(),
#napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).
def max_of_2(a, b):
    return a if a > b else b

  def maximum_of(a, b, c):
        max_num = max_of_2(max_of_2(a, b), c)
        return max_num


n1, n2, n3 = 31, 15, 1
print(maximum_of(n1, n2, n3))