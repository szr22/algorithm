#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#
from typing import List
from collections import defaultdict
# @lc code=start
import time
from queue import PriorityQueue
class Twitter:
    def __init__(self):
        self.capacity = 10
        self.friends_map = defaultdict(set)
        self.tweets_map = defaultdict(list)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follow(userId, userId)
        self.tweets_map[userId].append((
            time.time_ns(),
            tweetId
        ))


    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        pq = PriorityQueue()
        for f_id in self.friends_map[userId]:
            for t_info in self.tweets_map[f_id]:
                if pq.qsize()>0 and pq.queue[0][0]<t_info[0] and pq.qsize()>self.capacity:
                    break
                pq.put(t_info)
                if pq.qsize()>self.capacity:
                    pq.get()
        while pq.queue:
            res.insert(0, pq.get()[1])

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.friends_map[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (
            followerId!=followeeId
            and followerId in self.friends_map
            and followeeId in self.friends_map[followerId]
        ):
            self.friends_map[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

