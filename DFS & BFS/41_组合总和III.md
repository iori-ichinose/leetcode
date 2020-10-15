# 41. 组合总和III

> ~~三次了，三次了啊~~  
> ~~影流leetcode~~  
> ~~难道这就是你超时的借口~~

## [原题](https://leetcode-cn.com/problems/combination-sum-iii)

找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

+ 所有数字都是正整数。
+ 解集不能包含重复的组合。

## 解题思路

和前两道题十分类似，依然是采用DFS+回溯的思路。只是本题中数组限制在`[1,2,3,4,5,6,7,8,9]`，且不含有其他元素。解题步骤也很相似，对于某个元素只存在选或者不选的情况，如果选择了则将其加入一个`list`，如果最后`list`长度满足`k`且总和为`n`，则那个列表添加到最终答案。如果列表不符合要求，则回溯。

## 代码实现

```Python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def dfs(cur: int, remain: int, sol: int):
            # 找到了一个满足条件的序列
            if remain == 0 and len(sol) == k:
                ans.append(sol[:])
                return

            # 不满足题意，返回
            if cur == 10 or remain < 0 or len(sol) > k:
                return

            # 选择了当前元素，进行下一个
            dfs(cur + 1, remain - cur, sol + [cur])
            # 跳过了当前元素，进行下一个
            dfs(cur + 1, remain, sol)

        dfs(1, n, [])
        return ans
```
