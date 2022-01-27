from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax

class runTic(TwoPlayerGame):
    """ Klasa odpowiadająca za gre kółko i krzyżyk.

        Numeracja pozycji:  
        1 2 3  
        4 5 6  
        7 8 9  

        Attributes:
            players (list): Informacje o graczach.
            board (list): deklaracja planszy.
            current_player (int): informacja o tym, który gracz zaczyna.

    """

    def __init__(self, players):
        self.players = players
        self.board = [0 for i in range(9)]
        print(type(players))
        print(type(self.board))
        self.current_player = 1 

    def possible_moves(self):
        """ Funkcja sprawdzająca jakie ruchy są dostępne.

            Returns:
                list: lista dostępnych ruchów.
        
        """
        return [i + 1 for i, e in enumerate(self.board) if e == 0]

    def make_move(self, move):
        """ Funkcja odpowiadająca za poruszanie się.

            Args:
                move (int): Wybór ruchu.
        
        """
        self.board[int(move) - 1] = self.current_player

    # Zmienna klasy trzymająca linie, które oznaczają wygraną
    WIN_LINES = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7],
    ]

    def lose(self, who=None):
        """ Funkcja sprawdzająca, czy ktoś wygrał.

            Args:
                who (int): Gracz.

            Returns:
                bool: Zwraca True lub False.
        """
        if who is None:
            who = self.opponent_index
        wins = [
            all([(self.board[c - 1] == who) for c in line]) for line in self.WIN_LINES
        ]
        return any(wins)

    def is_over(self):
        """ Funkcja sprawdzająca, czy gra dobiegła końca.

            Returns:
                bool: Zwraca True lub False.
        """
        return (
            (self.possible_moves() == [])
            or self.lose()
            or self.lose(who=self.current_player)
        )

    def show(self):
        """ Funkcja printująca planszę.
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
        """ Funkcja sprawdzająca planszę.

            Args:
                i (int): Wiersze planszy.
                j (int): Kolumny planszy.

            Returns:
                str: zwraca coś tam.

        """
        return ["_", "O", "X"][self.board[3 * j + i]]

    def scoring(self):
        """ Funkcja odpowiedzialna za zwracanie wyniku.

            Returns:
                int: zwraca -100 lub 0 lub 100
        """
        opp_won = self.lose()
        i_won = self.lose(who=self.current_player)
        if opp_won and not i_won:
            return -100
        if i_won and not opp_won:
            return 100
        return 0

    def winner(self):
        """ Funkcja odpowiedzialna za zwracanie wygranego.

            Returns:
                String: Zwraca wygranego.
        """
        if self.lose(who=2):
            return "AI Wygrywa"
        return "Remis"

ai = Negamax(6)

def play_game(game_board, var):
    """ Funkcja obsługująca grę w kółko i krzyżyk.

        Args:
            game_board (str): Aktualna plansza.
            var (ImmutableMultiDict): Dokonany wybór.

        Returns:
            runTic: Obiekt klasy runTic.
            str: Wiadomość dotycząca ruchu/wyniku gry.
    
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
        msg = "Wykonaj ruch"
    return ttt, msg