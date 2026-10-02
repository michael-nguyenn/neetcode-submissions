import heapq

class Leaderboard:

    def __init__(self):
        self.leader_board = {} # let's us update entries easily
        self.scores = []

    def addScore(self, playerId: int, score: int) -> None:
        new_score = self.leader_board.get(playerId, 0) + score
        self.leader_board[playerId] = new_score
        heapq.heappush_max(self.scores, (new_score, playerId))
        

    def top(self, K: int) -> int:
        total = 0
        temp = []
        visited = set()

        for _ in range(K):
            score, player_id = heapq.heappop_max(self.scores)

            # deals with stale entries
            while player_id not in self.leader_board or score != self.leader_board[player_id] or player_id in visited:
                score, player_id = heapq.heappop_max(self.scores)
            
            total += score
            temp.append((score, player_id))
            visited.add(player_id)

        for entry in temp:
            heapq.heappush_max(self.scores, entry)

        return total

    def reset(self, playerId: int) -> None:
        del self.leader_board[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
