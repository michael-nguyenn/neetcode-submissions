"""
Problem
- Users can post, follow/unfollow, view 10 most recent tweets in their own feed
- Users and tweets are unique by int IDs

Design
Twitter()
- {} id -> following set (for getNewsFeed)
- How do we store tweets? 
- if we store all tweets in a single array
    - we have tweets in chronological order then we can loop backwards thru it
    - we can return the proper ones
    - this would cost O(1) to post a tweet
    - O(n) when getNewsFeed gets called
- if we general unique insertions and store a max heap for each user
    - each user needs to store their own tweets (uuid, Tweet)
    - log(n) per pop
    
postTweet
- when you post a Tweet it will get stored in a max heap of your own tweets
getNewsFeed
- fetches at most 10 most recent tweet IDs.
- items are either posted by users who they're following or by themselves
- go thru all their following list, and find the 10 most recent tweets
follow
- followerID follows foloweeID (prolly a set)
- need to do users[followerID].following[followeeID]
unfollow
- followerID unfollows foloweeID
- need to do del users[followerID].following[followeeID]
"""

import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.uuid = 0
        self.following = defaultdict(set) # id -> following
        self.tweets = defaultdict(list) # id -> tweets
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.uuid, tweetId))
        self.uuid += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        h = []

        self.following[userId].add(userId)
        for followee in self.following[userId]:
            if followee in self.tweets:
                index = len(self.tweets[followee]) - 1
                uuid, tweetId = self.tweets[followee][index]
                h.append((uuid, followee, tweetId, index-1))

        heapq.heapify_max(h)

        while h and len(res) < 10:
            uuid, followee, tweetId, index = heapq.heappop_max(h)
            res.append(tweetId)
            
            if index >= 0:
                uuid, tweetId = self.tweets[followee][index]
                heapq.heappush_max(h, (uuid, followee, tweetId, index-1))

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
