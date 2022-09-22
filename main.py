import sys
import tictactoe as ttt
import gui_tictactoe as gt

game = ttt.TicTacToe()
screen = gt.GuiTicTacToe()

screen.draw_board()
player = 1
game_over = False

while True:
    for event in gt.pygame.event.get():
        if event.type == gt.pygame.QUIT:
            sys.exit()
        if event.type == gt.pygame.KEYDOWN:
            if event.key == gt.pygame.K_ESCAPE:
                gt.pygame.quit()
                sys.exit()

        if event.type == gt.pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            clicked_row = int(mouse_y // 200)
            clicked_col = int(mouse_x // 200)
            if game.available_spot(clicked_row, clicked_col):
                if player == 1:
                    game.movement(clicked_row, clicked_col, 1)
                    if game.check_winner(player):
                        screen.draw_victory(clicked_col, clicked_row, player, game.winning_mode)
                        screen.game_won_text(player)
                        game_over = True
                    elif game.is_board_full() and not game.check_winner(player):
                        screen.game_draw_text()
                        game_over = True
                    player = 2

                elif player == 2:
                    game.movement(clicked_row, clicked_col, 2)
                    if game.check_winner(player):
                        screen.draw_victory(clicked_col, clicked_row, player, game.winning_mode)
                        screen.game_won_text(player)
                        game_over = True
                    elif game.is_board_full() and not game.check_winner(player):
                        screen.game_draw_text()
                        game_over = True
                    player = 1
                screen.draw_markers(clicked_row, clicked_col, game.board)

        if event.type == gt.pygame.KEYDOWN:
            if event.key == gt.pygame.K_RETURN:
                screen.restart()
                game.reset_board()
                player = 1
                game_over = False

    gt.pygame.display.update()
