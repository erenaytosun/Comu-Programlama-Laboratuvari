
# MATRİS DETERMİNANTI BULMA

my_Matris_1 =[[1 ,2] ,[3 ,4]]
my_Matris_2 =[[1 ,5 ,3] ,[4 ,7 ,6] ,[7 ,2 ,9]]
my_Matris_4 =[[13 ,2 ,3 ,4] ,[5 ,6 ,7 ,8] ,[92 ,10 ,31 ,42] ,[13 ,134 ,15 ,16]]
print(my_Matris_1)
print(my_Matris_2)
print(my_Matris_4)


def my_Matris_Determinant_2(m_1):

    s1 =(m_1[0][0] ) *(m_1[1][1])
    s2 =(m_1[0][1] ) *(m_1[1][0])
    s3 =s1 -s2
    return s3

print(my_Matris_Determinant_2(my_Matris_1))


def my_Matris_Determinant_Delete(m_1 ,m ,n):

    result =[]
    size_1 =len(m_1)
    size_2 =len(m_1[0])

    for i in range(size_1):
        if(i==m):
            continue
        row_1 =[]
        for j in range(size_2):
            if(j==n):
                continue
            row_1.append(m_1[i][j])
        result.append(row_1)
    return result

print(my_Matris_Determinant_Delete(my_Matris_2,0,0))


def my_Matris_Determinant_3(m_1):

    a1 =m_1[0][0]
    a2 =my_Matris_Determinant_Delete(m_1,0,0)
    a3 =my_Matris_Determinant_2(a2)
    a4 =a1 *a3

    b1 =m_1[0][1]
    b2 =my_Matris_Determinant_Delete(m_1,0,1)
    b3 =my_Matris_Determinant_2(b2)
    b4 =b1 *b3

    c1 =m_1[0][2]
    c2 =my_Matris_Determinant_Delete(m_1,0,2)
    c3 =my_Matris_Determinant_2(c2)
    c4 =c1 *c3

    return a4-b4+c4

print(my_Matris_Determinant_3(my_Matris_2))


def my_Matris_Determinant_4(m_1):

    a1 =m_1[0][0]
    a2 =my_Matris_Determinant_Delete(m_1 ,0 ,0)
    a3 =my_Matris_Determinant_3(a2)
    a4 =a1 *a3

    b1 =m_1[0][1]
    b2 =my_Matris_Determinant_Delete(m_1,0,1)
    b3 =my_Matris_Determinant_3(b2)
    b4 =b1 *b3

    c1 =m_1[0][2]
    c2 =my_Matris_Determinant_Delete(m_1,0,2)
    c3 =my_Matris_Determinant_3(c2)
    c4 =c1 *c3

    d1 =m_1[0][3]
    d2 =my_Matris_Determinant_Delete(m_1,0,3)
    d3 =my_Matris_Determinant_3(d2)
    d4 =d1 *d3

    return a4-b4+c4-d4

print(my_Matris_Determinant_4(my_Matris_4))


