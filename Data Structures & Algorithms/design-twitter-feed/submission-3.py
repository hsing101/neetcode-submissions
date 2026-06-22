class Twitter:

    def __init__(self):
        self.graph = defaultdict(set)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        latest = []
        for i in range(len(self.tweets) - 1, -1, -1):
            user, tweet = self.tweets[i]
            if user == userId or user in self.graph[userId]:
                latest.append(tweet) 
            if len(latest) == 10:
                break
        return latest


    def follow(self, followerId: int, followeeId: int) -> None:
        self.graph[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
         self.graph[followerId].discard(followeeId)
