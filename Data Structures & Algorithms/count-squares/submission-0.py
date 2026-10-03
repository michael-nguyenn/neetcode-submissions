class CountSquares:

    def __init__(self):
        self.points = collections.defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0

        keys = list(self.points.keys())
        for p in keys:
            x2, y2 = p

            if x1 == x2 and y1 != y2:
                dist = abs(y2 - y1)
                x3, x4 = x2 + dist, x2 - dist

                res += self.points[(x1,y2)] * self.points[(x3, y2)] * self.points[(x3, y1)]
                res += self.points[(x1,y2)] * self.points[(x4, y2)] * self.points[(x4,y1)]

        return res


        
        
