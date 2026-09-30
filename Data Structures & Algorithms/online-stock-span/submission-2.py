class StockSpanner:

    def __init__(self):
        self.prices = []
         

    def next(self, price: int) -> int:
        days = 0

        self.prices.append(price)
        cur = len(self.prices) - 1

        while cur >= 0 and self.prices[cur] <= price:
            days += 1
            cur -= 1 
            
        return days


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)