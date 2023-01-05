# RECURSIVE
# A Naive recursive Python implementation of LCS problem

def LCS(X, Y, m, n):

 
	if m == 0 or n == 0:
		return 0
	elif X[m-1] == Y[n-1]:
		return 1 + LCS(X, Y, m-1, n-1)
	else:
		return max(LCS(X, Y, m, n-1), LCS(X, Y, m-1, n))


# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", LCS(X , Y, len(X), len(Y)) )
# 
# NOTE: here you need to pass len(X) and len(Y)
# 💡 because you need to access from (0 - n-1) so in this case if you pass n-1 then 
# 💡 case become -1 at m = 0 and n = 0 so 0 will be left 
# 💡 that's why we are shifting index by 1 and accessing by n-1 and m-1
# 💡 so in that case you will get ans 1 less 
# COMPLEXITY
# Time complexity of the above naive recursive approach is  imp : O(2^n)
# -----------------------------------------------------------------------

# MEMOIZATION / optimized
# A Top-Down DP implementation of LCS problem

# Returns length of LCS for X[0..m-1], Y[0..n-1]
def LCS(X, Y, m, n, dp):

	if (m == 0 or n == 0):
		return 0

	if (dp[m][n] != -1):
		return dp[m][n]

	if X[m - 1] == Y[n - 1]:
		dp[m][n] = 1 + LCS(X, Y, m - 1, n - 1, dp)
		return dp[m][n]

	dp[m][n] = max(LCS(X, Y, m, n - 1, dp),LCS(X, Y, m - 1, n, dp))
	return dp[m][n]

# Driver code

X = "AGGTAB"
Y = "GXTXAYB"

m = len(X)
n = len(Y)
dp = [[-1 for i in range(n + 1)]for j in range(m + 1)]

print(f"Length of LCS is {LCS(X, Y, m-1, n-1, dp)}")

# COMPLEXITY
# Time Complexity : O(m*n) ignoring recursion stack space
# Auxiliary Space: O(m*n)
# -----------------------------------------------------------


# TABULATION 
# we go from imp   0 to n-1 

def lcs(X , Y):
	# find the length of the strings
	m = len(X)
	n = len(Y)

	# declaring the array for storing the dp values
	L = [[None]*(n+1) for i in range(m+1)]

	"""Following steps build L[m+1][n+1] in bottom up fashion
	Note: L[i][j] contains length of LCS of X[0..i-1]
	and Y[0..j-1]"""
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0 :
				L[i][j] = 0
			elif X[i-1] == Y[j-1]:
				L[i][j] = L[i-1][j-1]+1
			else:
				L[i][j] = max(L[i-1][j] , L[i][j-1])

	# L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
	return L[m][n]
#end of function lcs


# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", lcs(X, Y) )

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


