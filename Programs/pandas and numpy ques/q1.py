#Write a function that takes a list of numerical values and returns the minimum,
#maximum, average, and sum.

def calc(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    summ = sum(numbers)
    lengthh = len(numbers)
    average = summ/lengthh

    return minimum, maximum, summ, average

listofnos = [10,20,30,40]
min, max, sum, avg = calc(listofnos)
print("minimum: ", min)
print("maximum: ", max)
print("average: ", avg)
print("sum: ", sum)