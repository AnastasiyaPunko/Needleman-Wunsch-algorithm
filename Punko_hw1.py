# Прочитаем первые две строки из файла, указанного в командной строке
from sys import argv
indata = open(argv[1], "r")
s1 = indata.readline().strip()
s2 = indata.readline().strip()
indata.close()

# Очки за мэтч, мисмэтч и штраф за гэп
match = 1
mismatch = 0
gap = -1

# Создадим матрицу
def mymatrix(rows, cols):
    retval = []
    for x in range(rows):
        retval.append([])
        for y in range(cols):
            retval[-1].append(0)
    return retval

# Определим скор между любыми двумя основаниями при выравнивании
def match_score(a, b):
    if a == b:
        return match
    elif a == '-' or b == '-':
        return gap
    else:
        return mismatch
        
# Функция для выравнивания двух последовательностей по алгоритму Нидлмана – Вунша        
def N_W(s1, s2):
    
    n = len(s1)  
    m = len(s2)
    
    # Создадим матрицу нулей для сохранения скоров
    score = mymatrix(m+1, n+1)
   
    # Таблица расчета скоров
    
    # Первая колонка
    for i in range(0, m + 1):
        score[i][0] = gap * i
    
    # Первая строка
    for j in range(0, n + 1):
        score[0][j] = gap * j
    
    # Все остальные значения 
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            equal = score[i - 1][j - 1] + match_score(s1[j-1], s2[i-1])
            delete = score[i - 1][j] + gap
            insert = score[i][j - 1] + gap
            score[i][j] = max(equal, delete, insert)
    
    # Восстанавливаем выравнивание 
    
    align1 = ""
    align2 = ""
    
    i = m
    j = n
    
    while i > 0 and j > 0: 
        score_current = score[i][j]
        score_diagonal = score[i-1][j-1]
        score_up = score[i][j-1]
        score_left = score[i-1][j]
        
        if score_current == score_diagonal + match_score(s1[j-1], s2[i-1]):
            align1 += s1[j-1]
            align2 += s2[i-1]
            i -= 1
            j -= 1
        elif score_current == score_up + gap:
            align1 += s1[j-1]
            align2 += '-'
            j -= 1
        elif score_current == score_left + gap:
            align1 += '-'
            align2 += s2[i-1]
            i -= 1

    # Идем до верхнего левого угла
    while j > 0:
        align1 += s1[j-1]
        align2 += '-'
        j -= 1
    while i > 0:
        align1 += '-'
        align2 += s2[i-1]
        i -= 1
    
    # Так как мы шли снизу справа, нужно перевернуть выравненные последовательности
    align1 = align1[::-1]
    align2 = align2[::-1]
    
    return(score[m][n], align1, align2)

output1, output2, output3 = N_W(s1, s2)

print(output1)
print(output2 + "\n" + output3)
