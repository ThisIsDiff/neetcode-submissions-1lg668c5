class Twitter:
    recent_feed = []
    following = []
    timer = 0


    def __init__(self):
        self.recent_feed = []
        heapq.heapify(self.recent_feed)
        self.following = [set() for _ in range(101)] 
        self.timer = -1
        return


    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.recent_feed, (self.timer,userId,tweetId))
        self.timer -= 1
        return


    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        following = self.following[userId]
        rm_posts = []
        # for x in range(len(self.recent_feed)):
        #     _ , uid, post = self.recent_feed[x]
        #     if uid == userId or uid in following :
        #         feed.append(post)
        #     if len(feed) == 10:
        #         break

        while self.recent_feed and len(feed) < 10:
            t, uid, post = heapq.heappop(self.recent_feed)

            if uid == userId or uid in following:
                feed.append(post)

            rm_posts.append((t, uid, post))

        for r in rm_posts:
            heapq.heappush(self.recent_feed, r)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        return
