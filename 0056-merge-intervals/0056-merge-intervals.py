class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            prevInterval = result.pop(-1)
            curInterval = intervals[i]

            if prevInterval[1] >= curInterval[0]:
                if prevInterval[1] < curInterval[1]:
                    prevInterval[1] = curInterval[1]
                result.append(prevInterval)
            else:
                result.append(prevInterval)
                result.append(curInterval)

        return result
        