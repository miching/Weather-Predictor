import numpy as np

# function name: per_to_dec
# inputs: mat - n x n numpy array with percentages
# output: n x n numpy array where percentages are converted to decimal numbers
# assumptions: The test case shows a 3x3 matrix, but other test cases can have
			#  more or less rows/columns (always square matrix though)
def per_to_dec(mat):

	matTemp = []

	#Row
	for i in range(mat.shape[0]):
		indivRow = []

		#Column
		for k in range(mat.shape[1]):
			indivRow.append(mat[i, k] / 100)

		matTemp.append(indivRow)

	matDec = np.array(matTemp)
	return matDec



# function name: sig_change
# inputs: oldmat - n x n numpy array (decimal form)
		# newmat - n x n numpy array (decimal form)
# output: True if there is at least one element in newmat that is at least 0.0001 away
			# from its respective counterpart in oldmat
		# False otherwise
# assumptions: The test case shows a 3x3 matrix, but other test cases can have
			#  more or less rows/columns (always square matrix though)
def sig_change(oldmat, newmat):

	#Assume no significant change
	sigC = False

	for i in range (oldmat.shape[0]):
		for k in range (oldmat.shape[1]):

			#Check if difference is larger than 0.0001, there is Sig Change if True
			if( abs(oldmat[i,k] - newmat[i,k]) > 0.0001 ):
				sigC = True

	return sigC



# function name: prob_x
# inputs: mat - n x n numpy array with PERCENTAGES
		# x - number of iterations
# output: n x n numpy array that represents the probability matrix after x stages
		# Use per_to_dec here
# assumptions: The test case shows a 3x3 matrix, but other test cases can have
			#  more or less rows/columns (always square matrix though)
			#  x will always be >= 1
def prob_x(mat, x):

	#Update Matrix
	matDec = per_to_dec(mat)

	#Orginal Matrix
	orginalMat = np.array(matDec)

	#Number of iterations, minus one for the starting matrix
	for i in range(x-1):
		matDec = np.dot(matDec, orginalMat)

	return matDec



# function name: long_run_dist
# inputs: mat - n x n numpy array with PERCENTAGES
# output: n x n numpy array where percentages are converted to decimals
		# USE sig_change and per_to_dec
# assumptions: The test case shows a 3x3 matrix, but other test cases can have
			#  more or less rows/columns (always square matrix though)
def long_run_dist(probs):

	#Update Matrix
	matDec = per_to_dec(probs)

	#Orginal Matrix
	orginalMat = np.array(matDec)

	#Old Matrix to compare with
	oldMat = np.array(matDec)

	#Second iteration, or day after tomorrow
	matDec = np.dot(matDec, orginalMat)

	#Continue till no significant change
	while(sig_change(oldMat, matDec)):
		oldMat = matDec
		matDec = np.dot(matDec, orginalMat)


	return matDec



