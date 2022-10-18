"""A Method that takes in an array, and for every element in the array, it calculates the product of all other elements excluding the selected one, thereby returns the products in the form of an array"""
def arrayOfProducts(array):
    # Write your code here.
    pdt = 1
    arr_pdts = []
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                pdt *= array[j]
        arr_pdts.append(pdt)
        pdt = 1
    return arr_pdts
    pass
