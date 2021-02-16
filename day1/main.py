import sys, os

def main():
  expenses = []
  for _ in range(200):
    expenses.append(int(input()))

  radixSort(expenses)

  a, b, c = find3sum(expenses, 2020)

  print("A: " + str(a))
  print("B: " + str(b))
  print("C: " + str(c))
  print("A+B+C: " + str(a+b+c))
  print("A*B*C " + str(a*b*c))

def find2sum(int_arr, two_sum_val):
  j = -1
  for i in range(len(int_arr)-1):
    if int_arr[i]+int_arr[j] == two_sum_val:
      return int_arr[i], int_arr[j]

    else:
      while int_arr[i]+int_arr[j] > two_sum_val:
        j -= 1

def find3sum(int_arr, three_sum_val):

  for k in range(len(int_arr)):  
    j = -1
    for i in range(1,len(int_arr)):
      if int_arr[k]==int_arr[i]:
        continue
      if int_arr[i]+int_arr[j]+int_arr[k] == three_sum_val:
        return int_arr[i], int_arr[j], int_arr[k]

      else:
        while j*-1 < len(int_arr) and (int_arr[k] == int_arr[j] or int_arr[i]+int_arr[j]+int_arr[k] > three_sum_val):
          print(j)
          j -= 1
    


# Python program for implementation of Radix Sort 
   
# A function to do counting sort of arr[] according to 
# the digit represented by exp. 
def countingSort(arr, exp1): 
   
    n = len(arr) 
   
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
   
    # initialize count array as 0 
    count = [0] * (10) 
   
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[int((index)%10)] += 1
   
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
   
    # Build the output array 
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = arr[i] 
        count[int((index)%10)] -= 1
        i -= 1
   
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
 
# Method to do Radix Sort
def radixSort(arr):
 
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10
 

main()