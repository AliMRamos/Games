import pygame


class GuiTicTacToe:

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.WIDTH, self.HEIGHT = 600, 600
        self.BKG = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.DARK_VIOLET = (40, 23, 72)
        self.ORANGE = (255, 128, 0)
        pygame.display.set_caption("Tic Tac Toe")
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen.fill(self.BKG)

    def draw_board(self):
        pygame.draw.line(self.screen, self.DARK_VIOLET, (0, 200), (600, 200), 10)
        pygame.draw.line(self.screen, self.DARK_VIOLET, (0, 400), (600, 400), 10)
        pygame.draw.line(self.screen, self.DARK_VIOLET, (200, 0), (200, 600), 10)
        pygame.draw.line(self.screen, self.DARK_VIOLET, (400, 0), (400, 600), 10)

    def draw_markers(self, row, col, board):
        if board[row][col] == 1:
            pygame.draw.circle(self.screen, self.RED, (int(col * 200 + 200 / 2), int(row * 200 + 200 / 2)), radius=60,
                               width=15)
        elif board[row][col] == 2:
            pygame.draw.line(self.screen, self.ORANGE, (col * 200 + 55, row * 200 + 200 - 55),
                             (col * 200 + 200 - 55, row * 200 + 55), 25)
            pygame.draw.line(self.screen, self.ORANGE, (col * 200 + 55, row * 200 + 55),
                             (col * 200 + 200 - 55, row * 200 + 200 - 55), 25)

    def draw_victory(self, col, row, player, winning_mode: str):
        if player == 1:
            color = self.RED
        elif player == 2:
            color = self.ORANGE

        if winning_mode == "HORIZONTAL":
            posY = row * 200 + 100
            pygame.draw.line(self.screen, color, (15, posY), (self.WIDTH - 15, posY), 15)
        elif winning_mode == "VERTICAL":
            posX = col * 200 + 200 // 2
            pygame.draw.line(self.screen, color, (posX, 15), (posX, self.HEIGHT - 15), 15)
        elif winning_mode == "ASC DIAGONAL":
            pygame.draw.line(self.screen, color, (15, self.HEIGHT - 15), (self.WIDTH - 15, 15), 15)
        elif winning_mode == "DESC DIAGONAL":
            pygame.draw.line(self.screen, color, (15, 15), (self.WIDTH - 15, self.HEIGHT - 15), 15)

    def game_draw_text(self):
        font = pygame.font.SysFont('Garamond', 30)
        text = font.render('Draw game. No winner!', False, self.ORANGE, self.RED)
        self.screen.blit(text, (180, 250))

    def game_won_text(self, player):
        font = pygame.font.SysFont('Garamond', 30)
        text = font.render("Player {} won!".format(player), False, self.ORANGE, self.RED)
        self.screen.blit(text, (235, 290))

    def restart(self):
        self.screen.fill(self.BKG)
        self.draw_board()
