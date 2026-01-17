"""
Create a class (you pick the name) that has
at least 5 methods.
3 of the methods must call other methods within them (using self.method name)
Run at least one method automatically in __init__ so it will run at start up

Demonstrate your methods work by creating an instance and running all the methods
"""

class Anime:
    def __init__(self, title, genre, episodes, year):
        self.title = title
        self.genre = genre
        self.episodes = episodes
        self.year = year
        self.watched_episodes = 0
        self.start_show()

    def start_show(self):
        print(f"Starting the anime: {self.title}")
        self.watch_episode()

    def watch_episode(self):
        if self.watched_episodes < self.episodes:
            self.watched_episodes += 1
            print(f"Watched episode {self.watched_episodes} of {self.title}")
            self.check_completion()
        else:
            print(f"You have already completed {self.title}!")

    def check_completion(self):
        if self.watched_episodes == self.episodes:
            print(f"Congratulations! You have completed watching {self.title}.")
        else:
            print(f"{self.title} has {self.episodes - self.watched_episodes} episodes left to watch.")

    def binge_watch(self, count):
        for _ in range(count):
            self.watch_episode()
            
my_anime = Anime("Hunter x Hunter", "Adventure", 148, 2011)
my_anime.binge_watch(5)
my_anime.binge_watch(148)