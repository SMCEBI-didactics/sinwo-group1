from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax

class runTic(TwoPlayerGame):
    """ Klasa odpowiadająca za gre kółko i krzyżyk.

        Numeracja pozycji:
        1 2 3
        4 5 6
        7 8 9

        Attributes:
            players : Informacje o graczach
            board list: deklaracja planszy
            current_player int: informacja o tym, który gracz zaczyna

    """

    def __init__(self, players):
        self.players = players
        self.board = [0 for i in range(9)]
        self.current_player = 1 

    def possible_moves(self):
        """ Funkcja sprawdzająca jakie ruchy są dostępne.

            Parameters:
                None

            Returns:
                list: lista dostępnych ruchów
        
        """
        return [i + 1 for i, e in enumerate(self.board) if e == 0]

    def make_move(self, move):
        """ Funkcja odpowiadająca za poruszanie się

            Parameters:
                move int: Wybór ruchu

            Returns:
                None
        
        """
        self.board[int(move) - 1] = self.current_player

    WIN_LINES = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],  # horiz.
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],  # vertical
        [1, 5, 9],
        [3, 5, 7],  # diagonal
    ]

    def lose(self, who=None):
        """ Funkcja sprawdzająca, czy ktoś wygrał.

            Parameters:
                who int: Gracz

            Returns:
                any(wins)
        """
        if who is None:
            who = self.opponent_index
        wins = [
            all([(self.board[c - 1] == who) for c in line]) for line in self.WIN_LINES
        ]
        return any(wins)

    def is_over(self):
        """ Funkcja sprawdzająca, czy gra dobiegła końca.

            Parameters:
                None

            Returns:

        """
        return (
            (self.possible_moves() == [])
            or self.lose()
            or self.lose(who=self.current_player)
        )

    def show(self):
        """ Funkcja printująca planszę.

            Parameters:
                None

            Returns: 
                None
        """
        print(
            "\n"
            + "\n".join(
                [
                    " ".join([[".", "O", "X"][self.board[3 * j + i]] for i in range(3)])
                    for j in range(3)
                ]
            )
        )

    def spot_string(self, i, j):
        """ Funkcja 

        """
        return ["_", "O", "X"][self.board[3 * j + i]]

    def scoring(self):
        opp_won = self.lose()
        i_won = self.lose(who=self.current_player)
        if opp_won and not i_won:
            return -100
        if i_won and not opp_won:
            return 100
        return 0

    def winner(self):
        """ Funkcja odpowiedzialna za zwracanie wygranego.

            Parameters:
                None

            Returns:
                String: Zwycięzca.
        """
        if self.lose(who=2):
            return "AI Wins"
        return "Tie"

ai = Negamax(6)

def play_game(game_board, var):
    """ Funkcja obsługująca grę w kółko i krzyżyk.

        Parameters:
            game_board String: Plansza.
            var String: Wybór.

        Returns:
            ttt String: Wykonany ruch.
            msg String: Wiadomość dotycząca ruchu/wyniku gry.
    
    """
    ttt = runTic([Human_Player(), AI_Player(ai)])
    game_cookie = game_board
    if game_cookie:
        ttt.board = [int(x) for x in game_cookie.split(",")]
    if "choice" in var:
        ttt.play_move(var["choice"])
        if not ttt.is_over():
            ai_move = ttt.get_move()
            ttt.play_move(ai_move)
    if "reset" in var:
        ttt.board = [0 for i in range(9)]
    if ttt.is_over():
        msg = ttt.winner()
    else:
        msg = "play move"

    return ttt, msg