# Problem: Get Watched Videos by Your Friends - https://leetcode.com/problems/get-watched-videos-by-your-friends/description/

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(friends)
        queue = deque([(id, 0)])
        visited = {id}
        
        level_friends = []
        
        while queue:
            current_id, current_level = queue.popleft()
            
            if current_level == level:
                level_friends.append(current_id)
                continue                
            if current_level > level:
                continue

            for friend_id in friends[current_id]:
                if friend_id not in visited:
                    visited.add(friend_id)
                    queue.append((friend_id, current_level + 1))

        all_videos = []
        for person_id in level_friends:
            all_videos.extend(watchedVideos[person_id])
            
        video_counts = Counter(all_videos)
        sorted_videos = sorted(video_counts.items(), key=lambda item: (item[1], item[0]))
        
        return [video for video, count in sorted_videos]
