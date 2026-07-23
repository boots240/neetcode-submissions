from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        result = []

        for s in strs:
            sorteds = tuple(sorted(s))
            hashmap[sorteds].append(s)

        for value in hashmap.values():
            result.append(value)

        return result


    


 


    




        
        
     

        
        
        
        
        

        