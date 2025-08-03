from solution import Solution


if __name__ == "__main__":
    s = input()
    t = input()
    
    solution = Solution()
    is_subsequence = solution.isSubsequence(s, t)
    print(is_subsequence)
