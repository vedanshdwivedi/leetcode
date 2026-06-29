class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        result = 0
        for top in range(rows ):
            compressedArr = [0] * (cols)
            for bottom in range(top, rows):
                for col in range(cols):
                    compressedArr[col] += matrix[bottom][col]

                prefix = 0
                seen = defaultdict(int)
                seen[0] = 1

                for num in compressedArr: 
                    prefix += num 
                    result += seen[prefix - target] 
                    seen[prefix] += 1 
        return result



        