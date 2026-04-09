class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
             # cur: current list [] 
             # i: start index 
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if total > target:
                return

                # Recursion of dfs, 
                # j will control the start index, so won't happend dulicate set
            for j in range(i, len(nums)):
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()
        
        dfs(0, [], 0)

        return res


        