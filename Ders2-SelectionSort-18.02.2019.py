
#    Selection Sort

def mySearchSelection(my_array):
    swap_sayisi = 0
    for i in range(len(my_array)-1,0,-1):
        positionOfMax=0
        for location in range(1,i+1):
            #print("j: ",location,"İ: ",end="\n")
            if(my_array[location]>my_array[positionOfMax]):
                positionOfMax=location
        temp=my_array[location]
        my_array[location]=my_array[positionOfMax]
        my_array[positionOfMax]=temp
        swap_sayisi=swap_sayisi+1


    print("swap sayisi: ",swap_sayisi)
    return



my_arr=[21,12,13,44,25,2,7,16,14,35]
mySearchSelection(my_arr)
print(my_arr)
