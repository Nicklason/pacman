import requests

class Leaderboard:
    def __init__(self, game):
        self.game = game
        self.host = 'https://api.nicklas.io'
    
    def get_scores(self):
        params = dict(
            game=self.game
        )

        r = requests.get(self.host, params=params)
        return r.json()
    
    def new_score(self, user, score):
        prams = dict(
            game=self.game,
            user=user,
            score=score
        )

        r = requests.post(self.host, params=params)
        return r.json()
