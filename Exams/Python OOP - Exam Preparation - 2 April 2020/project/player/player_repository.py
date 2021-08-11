from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count: int = 0
        self.players = []

    def add(self, player: Player):
        player_name = player.username
        # names = list(map(lambda x: x.username, self.players))
        names = [p.username for p in self.players]
        if player_name in names:
            raise ValueError(f"Player {player_name} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player_name: str):
        if player_name == "":
            raise ValueError("Player cannot be an empty string!")
        # names = [p.username for p in self.players]
        # player_to_remove = list(map(lambda x: x.username == player_name, self.players))[0]
        # player_to_remove = [p for p in self.players if p.username == player_name][0]
        player_to_remove = self.find(player_name)
        self.players.remove(player_to_remove)
        self.count -= 1

    def find(self, username: str):
        player = [p for p in self.players if p.username == username][0]
        return player

    # @property
    # def count(self):
    #     return len(self.players)
