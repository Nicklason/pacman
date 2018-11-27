""" Leaderboard / scoreboard klasse """

import requests

class Leaderboard:
    """ Initialisere klassen """
    def __init__(self, game):
        self.game = game
        self.host = 'https://api.nicklas.io'

    """ Får alle scores for et spil """
    def get_scores(self):
        params = dict(
            game=self.game
        )

        r = requests.get(self.host, params=params)
        return r.json()

    """ Laver en ny score for et spil """
    def new_score(self, user, score):
        params = dict(
            game=self.game,
            user=user,
            score=score
        )

        r = requests.post(self.host, params=params)
        return r.json()
