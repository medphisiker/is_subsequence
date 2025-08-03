from solution import Solution


def test():
    # Пример 1 является подпоследовательностью
    #         p
    # t: ahbgdc
    #
    #       p
    # s: abc
    s = "abc"
    t = "ahbgdc"
    solution = Solution()
    is_subsequence = solution.isSubsequence(s, t)
    assert is_subsequence
    
    # Пример 2 не является подпоследовательностью
    #         p
    # t: ahbgdc
    #
    #     p
    # s: axc
    s = "axc"
    t = "ahbgdc"
    solution = Solution()
    is_subsequence = solution.isSubsequence(s, t)
    assert not is_subsequence
    
    # Тест s = ""
    #    p
    # t: ahbgdc
    #
    #    p
    # s: 
    s = ""
    t = "ahbgdc"
    solution = Solution()
    is_subsequence = solution.isSubsequence(s, t)
    assert is_subsequence
    
    # Тест t = ""
    #    p
    # t: 
    #
    #    p
    # s: abc
    s = "abc"
    t = ""
    solution = Solution()
    is_subsequence = solution.isSubsequence(s, t)
    assert not is_subsequence
    
    # Тест когда обе строки пустые
    #    p
    # t: 
    #
    #    p
    # s: 
    s = ""
    t = ""
    solution = Solution()
    is_subsequence = solution.isSubsequence(s, t)
    assert is_subsequence
    
    # Тест нет ни одной совпадающей буквы
    #    p
    # t: zyzqwerty
    #
    #    p
    # s: abc
    s = "abc"
    t = "zyzqwerty"
    solution = Solution()
    is_subsequence = solution.isSubsequence(s, t)
    assert not is_subsequence
    
    # Тест подпоследовательность в конце
    #            p
    # t: zyzqweabc
    #
    #       p
    # s: abc
    s = "abc"
    t = "zyzqweabc"
    solution = Solution()
    is_subsequence = solution.isSubsequence(s, t)
    assert is_subsequence
    
    # Тест подпоследовательность разряженная
    #             p
    # t: a000b000c00
    #
    #       p
    # s: abc
    s = "abc"
    t = "a000b000c00"
    solution = Solution()
    is_subsequence = solution.isSubsequence(s, t)
    assert is_subsequence
    
    # Тест когда s длиннее t
    #    p
    # t: ab
    #
    #    p
    # s: abc
    s = "abc"
    t = "ab"
    solution = Solution()
    is_subsequence = solution.isSubsequence(s, t)
    assert not is_subsequence
    
    # Тест когда s и t одинаковые
    #      p
    # t: abc
    #
    #       p
    # s: abc
    s = "abc"
    t = "abc"
    solution = Solution()
    is_subsequence = solution.isSubsequence(s, t)
    assert is_subsequence
    
    # Тест с повторяющимися символами
    #        p
    # t: aabbcc
    #
    #       p
    # s: abc
    s = "abc"
    t = "aabbcc"
    solution = Solution()
    is_subsequence = solution.isSubsequence(s, t)
    assert is_subsequence


if __name__ == "__main__":
    test()