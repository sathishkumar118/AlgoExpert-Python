"""A Method that takes in an array, and for every element in the array, it calculates the product of all other elements excluding the selected one, thereby returns the products in the form of an array"""
def arrayOfProducts(array):
    # Write your code here.
    left,right = [1]*len(array),[1]*len(array)
    res = [0]*len(array)
    product = 1
    for i in range(len(array)):
        left[i] = product
        product *= array[i]
    product = 1
    for i in range(len(array)-1,-1,-1):
        res[i]  = product * left[i]
        product *= array[i]
    return res
    pass
