from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = Counter(tasks)
        counts = [count for count in task_counter.values()]
        heapq.heapify_max(counts)
        cooldown_q = deque() # (#tasks, min_schedule_time)
        time = 0

        while counts or cooldown_q:
            time += 1

            # if everything is on cooldown, we'll move our time
            # forward so that next round we can schedule it
            if not counts:
                time = cooldown_q[0][1]
            # Otherwise we have available schedulable tasks
            else:
                # -1 to consume the task
                count = heapq.heappop_max(counts) - 1

                # if we still have the task to schedule
                if count != 0:
                    # add it to the q with the cooldown period
                    cooldown_q.append((count, n + time))
            
            # At the end of each round check if any tasks
            # are done with their cooldown
            if cooldown_q and cooldown_q[0][1] == time:
                heapq.heappush_max(counts, cooldown_q.popleft()[0])
        
        return time



        
        