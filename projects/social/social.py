import random
import sys
sys.path.append('../graph')
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # # Add users

        # # Create friendships
        # for i in range(0, num_users):
        #     self.add_user(f'Fred{i + 1}')

        # # Generate all friendship combinations
        # possible_friendships = []
        
        # # Avoid duplicates by making sure first number is smaller
        # for user_id in self.users:
        #     for friend_id in range(user_id + 1, self.last_id + 1):
        #         possible_friendships.append((user_id, friend_id))

        # # Shuffle all possible friendships
        # random.shuffle(possible_friendships)

        # # Create for first X pairs
        # for i in range(num_users * avg_friendships // 2):
        #     friendship = possible_friendships[i]
        #     self.add_friendship(friendship[0], friendship[1])

        # Use add_user num_users times
        for i in range(num_users):
            self.add_user(f'User {i}')
        
        # Keep track of good friendships and collisions
        target_friendships = num_users * avg_friendships // 2
        total_friendships = 0
        collisions = 0

        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            if self.add_friendship(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1

        print(f"Total Collisions: {collisions}")
        

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        
        # Create queue
        qq = Queue()
        # Enqueue path to user_id
        qq.enqueue([user_id])

        # Very similar to previous assignments, just populate visited and return it
        while qq.size() > 0:
            path = qq.dequeue()
            vertex = path[-1]
            # If item not in list yet
            if vertex not in visited:
                visited[vertex] = path
            # Check all connections to last item
            for i in self.friendships[vertex]:
                copy_path = list(path)
                copy_path.append(i)
                if i not in visited:
                    qq.enqueue(copy_path)
                # elif len(copy_path) < len(visited[i]):
                #     visited[i] = copy_path
        return visited



if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 3)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

total_social_paths = 0
for user_id in connections:
    total_social_paths += len(connections[user_id])
print(f'Average length of social path is: {total_social_paths/len(connections)}')