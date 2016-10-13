#kadane algorithm:
#used for finding maximum sum of a subarray (non -ve sum only) in a shuffled array containing 
#-ve,0s and +ve elements

def Kadane(arr):
	tempSum, result_Sum = 0,0
	for i in range(len(arr)):
		tempSum = max(0,tempSum+arr[i])
		result_Sum = max(tempSum, result_Sum)

	print result_Sum



if __name__=='__main__':
	arr = map(int, raw_input("Enter your array elements one after each space\n Press enter when you are done\n").split())
	Kadane(arr)