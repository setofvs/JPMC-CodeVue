#Reverse an array of numbers by given chunk size
#O(n) time - 2 while loops but only 1 pass-through
#O(n) space - storing the returning numArray
def reverseGroup(numArray, k):
   i = 0
   n = len(numArray)
   while(i < n):
      left = i
      right = min(i + k - 1, n - 1) #Sets the chunk size and prevents right pointer from going out of bounds
      if k == 1: #If size of chunk is 1, there are no swaps
        break
      if right == n - 1 and i + k -1 > n - 1:  #Circuit breaker if chunk size > remaining number size, do not reverse
        break
      while (left < right):
         numArray[left], numArray[right] = numArray[right], numArray[left]
         left += 1;
         right -= 1
      i += k  #Moves left pointer to the next chunk


#User input
numArray = []
arraySize = int(input("Enter the size of the array: "))
print("Enter a number: ")
for i in range(int(arraySize)): #Populate numArray with user input
   numInput = int(input(""))
   numArray.append(int(numInput))
chunk = int(input("Enter the size of the chunk: "))


#Populate return array
reverseGroup(numArray, chunk)
for i in range(0, arraySize):
   print(numArray[i], end =" ")
