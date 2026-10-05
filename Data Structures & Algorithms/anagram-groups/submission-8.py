class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for st in strs:
            arr = [0] * 26
            for char in st:
                index = ord(char) - ord('a')
                arr[index] += 1
            res = tuple(arr)
            map[res].append(st)
        
        return [value for key, value in map.items()]