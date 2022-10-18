"""A Method that takes in an array, and for every element in the array, it calculates the product of all other elements excluding the selected one, thereby returns the products in the form of an array"""
def arrayOfProducts(array):
    # Write your code here.
    left,right = [1]*len(array),[1]*len(array)
    res = []
    product = 1
    for i in range(len(array)):
        left[i] = product
        product *= array[i]
    product = 1
    for i in range(len(array)-1,-1,-1):
        right[i] = product
        product *= array[i]
    for i in range(len(array)):
        res.append(left[i]*right[i])
    return res
    pass
