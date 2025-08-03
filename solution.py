class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """Определяет является ли строка s подстрокой t.
        
        Подстрока строки - это строка, которая образована из исходной строки
        путем удаления некоторых (может быть ни одного) символов без нарушения
        относительных позиций оставшихся символов.
        
        Использует метод двух указателей.
        
        Временная сложность O(n) - в худшем случае проходим t строку полностью
        n - длинна строки t.
        пространственная сложность O(1) - выделяем память только на указатели.

        Args:
            s (str): _description_
            t (str): _description_

        Returns:
            bool: _description_
        """               
        s_pointer = 0
        t_pointer = 0
        
        while s_pointer < len(s) and t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                t_pointer += 1
            
            else:
                while t_pointer < len(t) and s[s_pointer] != t[t_pointer]:
                    t_pointer += 1
        
        if s_pointer == len(s):
            return True
        else:
            return False