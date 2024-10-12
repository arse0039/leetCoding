# Leetcode - Design Twitter Feed - Medium
import time, heapq
from collections import deque

class Twitter:

    def __init__(self):
        self.users = {}
        self.time = -1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.checkValidUser(userId)
        self.users[userId]["tweets"].append((self.time, tweetId))
        self.time -= 1
            
    def getNewsFeed(self, userId: int) -> list[int]:
        recentTweets = deque([])
        allTweets = [tweet for tweet in self.users[userId]["tweets"]]
        for followee in self.users[userId]["following"]:
            for tweet in self.users[followee]["tweets"]:
                allTweets.append(tweet)

        heapq.heapify(allTweets)
        count = 10
        while count > 0 and allTweets:
            recentTweets.appendleft(heapq.heappop(allTweets)[1])
            count -= 1
        
        return list(recentTweets)        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.checkValidUser(followeeId)
        self.checkValidUser(followerId)
        if followeeId != followerId:
            self.users[followerId]["following"].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.checkValidUser(followeeId)
        self.checkValidUser(followerId)
        if followeeId != followerId:
            self.users[followerId]["following"].remove(followeeId)
    
    def createUser(self, userId:int) -> None:
        self.users[userId] = {
                "tweets": [],
                "following": set()
            }
        
    def checkValidUser(self, userId:int) -> None:
        if userId not in self.users:
            self.createUser(userId)

test = Twitter()
for i in range(1, 12):
    test.postTweet(1, i)

print(test.getNewsFeed(1))
test.follow(1, 2)
print(test.getNewsFeed(1))
