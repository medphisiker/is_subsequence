from solution import Solution

def test():
    # Пример 1 является подстрокой
    # подстрока
    #       p
    # ahbgdc

    #    p
    # abc
    s = "abc"
    t = "ahbgdc"
    solution = Solution()
    is_subsequence = solution.isSubsequence(s, t)
    assert is_subsequence
    
    # Пример 2 не является подстрокой
    # подстрока
    #      p
    # ahbgdc

    #  p
    # axc
    s = "axc"
    t = "ahbgdc"
    solution = Solution()
    is_subsequence = solution.isSubsequence(s, t)
    assert not is_subsequence
    
    # Тест s = ""
    # подстрока
    # p
    # ahbgdc

    # p
    # 
    s = ""
    t = "ahbgdc"
    solution = Solution()
    is_subsequence = solution.isSubsequence(s, t)
    assert is_subsequence
    
    # Тест t = ""
    # подстрока
    # p
    # 

    # p
    # abc
    s = "abc"
    t = ""
    solution = Solution()
    is_subsequence = solution.isSubsequence(s, t)
    assert not is_subsequence
    
    # Тест нет ни одной совпадающей буквы
    # подстрока
    #         p
    # zyzqwerty

    # p
    # abc
    s = "abc"
    t = "zyzqwerty"
    solution = Solution()
    is_subsequence = solution.isSubsequence(s, t)
    assert not is_subsequence
    
    # Тест подстрока в конце
    # подстрока
    #          p
    # zyzqweabc

    #    p
    # abc
    s = "abc"
    t = "zyzqweabc"
    solution = Solution()
    is_subsequence = solution.isSubsequence(s, t)
    assert is_subsequence
    
    # Тест подстрока разряженная
    # подстрока
    #          p
    # a000b000c00

    #    p
    # abc
    s = "abc"
    t = "a000b000c00"
    solution = Solution()
    is_subsequence = solution.isSubsequence(s, t)
    assert is_subsequence
    

if __name__ == "__main__":
    test()