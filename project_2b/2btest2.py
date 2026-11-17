# Connect 4 - Pygame Version
# Project 2B
# Two players take turns clicking a column to drop their piece.
# First to get 4 in a row (across, up/down, or diagonal) wins.
# The game keeps track of wins and ties, and you can play again
# by clicking the "Play Again" button (no need to press Run again).

import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"   # hides pygame's hello message so nothing prints to the console
import pygame

pygame.init()

# ---------- settings ----------
ROWS = 6
COLS = 7
CELL = 90                      # size of each square on the board
TOP_BAR = 130                  # space at the top for the scoreboard/messages
BOTTOM_BAR = 80                # space at the bottom for the button
WIDTH = COLS * CELL
HEIGHT = TOP_BAR + ROWS * CELL + BOTTOM_BAR
RADIUS = CELL // 2 - 8

# colors
BLUE = (30, 70, 200)
BLACK = (20, 20, 20)
WHITE = (255, 255, 255)
RED = (220, 40, 40)
YELLOW = (240, 210, 30)
GRAY = (150, 150, 150)
GREEN = (40, 170, 70)

EMPTY = 0
PLAYER1 = 1   # red
PLAYER2 = 2   # yellow

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect 4")
big_font = pygame.font.SysFont("arial", 36, bold=True)
small_font = pygame.font.SysFont("arial", 24)

# the Play Again button (only shows up after a game ends)
button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT - BOTTOM_BAR + 15, 200, 50)


# ---------- board functions ----------
def make_board():
    """Makes a new empty board (a list of rows)."""
    board = []
    for r in range(ROWS):
        board.append([EMPTY] * COLS)
    return board


def column_is_open(board, col):
    """Returns True if the column still has room at the top."""
    return board[0][col] == EMPTY


def drop_piece(board, col, player):
    """Drops the player's piece into the lowest empty spot in the column.
    Returns the row it landed in."""
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == EMPTY:
            board[r][col] = player
            return r
    return -1


def check_win(board, player):
    """Checks every direction to see if the player has 4 in a row."""
    # horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c + i] == player for i in range(4)):
                return True
    # vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r + i][c] == player for i in range(4)):
                return True
    # diagonal going down-right
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == player for i in range(4)):
                return True
    # diagonal going up-right
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r - i][c + i] == player for i in range(4)):
                return True
    return False


def board_is_full(board):
    """If the top row has no empty spots, the board is full (tie)."""
    for c in range(COLS):
        if board[0][c] == EMPTY:
            return False
    return True


def get_column(mouse_x):
    """Turns the x position of the mouse into a column number."""
    return mouse_x // CELL


# ---------- drawing functions ----------
def player_color(player):
    if player == PLAYER1:
        return RED
    return YELLOW


def draw_text(text, font, color, center):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=center)
    screen.blit(surface, rect)


def draw_screen(board, turn, scores, message, game_over, hover_col):
    screen.fill(BLACK)

    # scoreboard
    score_text = "Red: " + str(scores[PLAYER1]) + "    Yellow: " + str(scores[PLAYER2]) + "    Ties: " + str(scores["ties"])
    draw_text(score_text, small_font, WHITE, (WIDTH // 2, 25))

    # message (whose turn, winner, tie, or invalid move)
    draw_text(message, big_font, WHITE, (WIDTH // 2, 65))

    # preview piece above the column the mouse is on
    if not game_over and hover_col is not None and 0 <= hover_col < COLS:
        x = hover_col * CELL + CELL // 2
        pygame.draw.circle(screen, player_color(turn), (x, TOP_BAR - 22), RADIUS // 2)

    # board
    pygame.draw.rect(screen, BLUE, (0, TOP_BAR, WIDTH, ROWS * CELL))
    for r in range(ROWS):
        for c in range(COLS):
            x = c * CELL + CELL // 2
            y = TOP_BAR + r * CELL + CELL // 2
            if board[r][c] == PLAYER1:
                color = RED
            elif board[r][c] == PLAYER2:
                color = YELLOW
            else:
                color = BLACK
            pygame.draw.circle(screen, color, (x, y), RADIUS)

    # play again button
    if game_over:
        pygame.draw.rect(screen, GREEN, button_rect, border_radius=10)
        draw_text("Play Again", small_font, WHITE, button_rect.center)
    else:
        draw_text("Click a column to drop your piece", small_font, GRAY, (WIDTH // 2, HEIGHT - BOTTOM_BAR // 2))

    pygame.display.flip()


def turn_message(turn):
    if turn == PLAYER1:
        return "Red's turn"
    return "Yellow's turn"


# ---------- main game ----------
def main():
    board = make_board()
    turn = PLAYER1
    scores = {PLAYER1: 0, PLAYER2: 0, "ties": 0}
    game_over = False
    message = turn_message(turn)
    hover_col = None
    starter = PLAYER1      # who goes first; switches every new game to be fair

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEMOTION:
                hover_col = get_column(event.pos[0])

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos

                if game_over:
                    # only the Play Again button does something after the game ends
                    if button_rect.collidepoint(x, y):
                        board = make_board()
                        if starter == PLAYER1:
                            starter = PLAYER2
                        else:
                            starter = PLAYER1
                        turn = starter
                        game_over = False
                        message = turn_message(turn)
                    continue

                # check for bad clicks
                if y < TOP_BAR or y > TOP_BAR + ROWS * CELL:
                    message = "Click on the board!"
                    continue

                col = get_column(x)
                if col < 0 or col >= COLS:
                    continue

                if not column_is_open(board, col):
                    message = "That column is full, pick another"
                    continue

                # valid move
                drop_piece(board, col, turn)

                if check_win(board, turn):
                    scores[turn] += 1
                    if turn == PLAYER1:
                        message = "Red wins!"
                    else:
                        message = "Yellow wins!"
                    game_over = True
                elif board_is_full(board):
                    scores["ties"] += 1
                    message = "It's a tie!"
                    game_over = True
                else:
                    # switch turns
                    if turn == PLAYER1:
                        turn = PLAYER2
                    else:
                        turn = PLAYER1
                    message = turn_message(turn)

        draw_screen(board, turn, scores, message, game_over, hover_col)
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()