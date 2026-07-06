class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        
        need = Counter(s1)
        window = Counter()
        
        for i in range(len(s2)):
            window[s2[i]] += 1
            
            if i >= len(s1):
                if window[s2[i - len(s1)]] == 1:
                    del window[s2[i - len(s1)]]
                else:
                    window[s2[i - len(s1)]] -= 1
            
            if window == need:
                return True
        
        return False
        