class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])

        row_0 = set()
        col_0 = set()


        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_0.add(i)
                    col_0.add(j)

        for i in range(row):
            for j in range(col):
                if i in row_0 :
                    matrix[i][j] = 0 
                if j in col_0:
                    matrix[i][j] = 0 
    

        # 123
        # 456
        # 789
        
# find where is 0 first
# than that same row and col all turn to 0