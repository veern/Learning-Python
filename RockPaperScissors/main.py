import UI


SCORE_LIMIT = 3


def main():
    player1, player2, scoreboard = UI.generate_players_and_scoreboard(UI.start_and_choose_player_amount())
    while max(scoreboard.players_scores.values()) < SCORE_LIMIT:
        player1.make_choice()
        player2.make_choice()
        UI.who_won_round(player1, player2, scoreboard)
    scoreboard.display_scores()


if __name__ == "__main__":
    main()
