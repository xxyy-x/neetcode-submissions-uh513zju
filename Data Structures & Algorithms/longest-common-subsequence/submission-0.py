class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 把兩個string攤開放再rol and col, 他們的交叉點去表示相同的數量

        len1 = len(text1)
        len2 = len(text2)

        df = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if text1[i-1] == text2[j-1]:
                    df[i][j] = df[i-1][j-1] + 1
                else:
                    df[i][j] = max(df[i-1][j], df[i][j-1])

        
        return df[len1][len2]

        