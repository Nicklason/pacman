""" Leaderboard / scoreboard klasse """

import requests

class Leaderboard():
    """ Initialisere klassen """
    def __init__(self, game):
        self.host = "https://api.nicklas.io"
        self.game = game

    def get_scores(self):
        """ Får alle scores for et spil """
        # Søg efter navnet på spillet
        params = dict(
            game=self.game
        )

        # Lav kald til API
        r = requests.get(url=self.host, params=params)
        # Smid en fejl hvis kaldet ikke var succesfuldt
        # r.raise_for_status()
        if r.ok:
            data = r.json()
            return data

        return None

    def save_score(self, user, score):
        """ Laver en ny score for et spil """

        json = dict(
            game=self.game,
            user=user,
            score=score
        )

        r = requests.post(url=self.host, json=params)

        if r.ok:
            data = r.json()
            return data

        return None
