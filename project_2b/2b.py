import pygame

# -----------------------------
# Connect 4 settings
# -----------------------------
ROWS = 6
COLUMNS = 7
CELL_SIZE = 80

WIDTH = COLUMNS * CELL_SIZE
TOP_SPACE = 150
BOTTOM_SPACE = 100
HEIGHT = TOP_SPACE + ROWS * CELL_SIZE + BOTTOM_SPACE

# Colors
BACKGROUND = (238, 242, 255)
BOARD_BLUE = (29, 78, 216)
DARK_BLUE = (23, 37, 84)
RED = (239, 68, 68)
YELLOW = (250, 204, 21)
WHITE = (255, 255, 255)
GRAY = (100, 116, 139)
LIGHT_GRAY = (226, 232, 240)
GREEN = (22, 163, 74)


# -----------------------------
# Create a new empty 6 x 7 board
# -----------------------------
def create_board():
    return [[" " for column in range(COLUMNS)] for row in range(ROWS)]


# -----------------------------
# Place a piece in the lowest
# available space in a column
# -----------------------------
def drop_piece(board, column, piece):
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == " ":
            board[row][column] = piece
            return True

    return False


# -----------------------------
# Check all possible directions
# for four matching pieces
# -----------------------------
def check_winner(board, piece):

    # Horizontal
    for row in range(ROWS):
        for column in range(COLUMNS - 3):
            if (
                board[row][column] == piece
                and board[row][column + 1] == piece
                and board[row][column + 2] == piece
                and board[row][column + 3] == piece
            ):
                return True

    # Vertical
    for row in range(ROWS - 3):
        for column in range(COLUMNS):
            if (
                board[row][column] == piece
                and board[row + 1][column] == piece
                and board[row + 2][column] == piece
                and board[row + 3][column] == piece
            ):
                return True

    # Diagonal down-right
    for row in range(ROWS - 3):
        for column in range(COLUMNS - 3):
            if (
                board[row][column] == piece
                and board[row + 1][column + 1] == piece
                and board[row + 2][column + 2] == piece
                and board[row + 3][column + 3] == piece
            ):
                return True

    # Diagonal up-right
    for row in range(3, ROWS):
        for column in range(COLUMNS - 3):
            if (
                board[row][column] == piece
                and board[row - 1][column + 1] == piece
                and board[row - 2][column + 2] == piece
                and board[row - 3][column + 3] == piece
            ):
                return True

    return False


# -----------------------------
# Check whether every column
# is full
# -----------------------------
def board_full(board):
    for column in range(COLUMNS):
        if board[0][column] == " ":
            return False

    return True


# -----------------------------
# Draw text centered on screen
# -----------------------------
def draw_centered_text(screen, text, font, color, y):
    image = font.render(text, True, color)
    rect = image.get_rect(center=(WIDTH // 2, y))
    screen.blit(image, rect)


# -----------------------------
# Draw one button
# -----------------------------
def draw_button(screen, rect, text, font):
    pygame.draw.rect(screen, WHITE, rect, border_radius=8)
    pygame.draw.rect(screen, DARK_BLUE, rect, 2, border_radius=8)

    text_image = font.render(text, True, DARK_BLUE)
    text_rect = text_image.get_rect(center=rect.center)

    screen.blit(text_image, text_rect)


# -----------------------------
# Draw the Connect 4 board
# -----------------------------
def draw_board(screen, board):

    board_y = TOP_SPACE

    # Blue board background
    pygame.draw.rect(
        screen,
        BOARD_BLUE,
        (0, board_y, WIDTH, ROWS * CELL_SIZE)
    )

    for row in range(ROWS):
        for column in range(COLUMNS):

            center_x = column * CELL_SIZE + CELL_SIZE // 2
            center_y = board_y + row * CELL_SIZE + CELL_SIZE // 2

            piece = board[row][column]

            if piece == "X":
                color = RED
            elif piece == "O":
                color = YELLOW
            else:
                color = BACKGROUND

            pygame.draw.circle(
                screen,
                color,
                (center_x, center_y),
                CELL_SIZE // 2 - 8
            )

            pygame.draw.circle(
                screen,
                DARK_BLUE,
                (center_x, center_y),
                CELL_SIZE // 2 - 8,
                2
            )


# -----------------------------
# Main program
# -----------------------------
def main():

    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Connect 4 - Two Players")

    pygame.display.flip()

    # Tell the user in the terminal that the game is running.
    print("Connect 4 is running. A game window should be open.")
    print("Close it with the Quit button or press Ctrl+C here.")

    clock = pygame.time.Clock()

    title_font = pygame.font.Font(None, 44)
    normal_font = pygame.font.Font(None, 28)
    small_font = pygame.font.Font(None, 22)

    # Score totals stay between games
    player1_wins = 0
    player2_wins = 0

    # Current game information
    board = create_board()
    current_player = "X"
    game_over = False
    status = "Player 1 (X): click a column"

    # Buttons
    button_y = TOP_SPACE + ROWS * CELL_SIZE + 25

    play_again_button = pygame.Rect(
        20,
        button_y,
        150,
        45
    )

    reset_button = pygame.Rect(
        190,
        button_y,
        200,
        45
    )

    quit_button = pygame.Rect(
        410,
        button_y,
        130,
        45
    )

    running = True

    while running:

        # -----------------------------
        # Events / user input
        # -----------------------------
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_x, mouse_y = event.pos

                # -----------------------------
                # Play Again button
                # -----------------------------
                if play_again_button.collidepoint(event.pos):

                    board = create_board()
                    current_player = "X"
                    game_over = False
                    status = "Player 1 (X): click a column"

                # -----------------------------
                # Reset Scores button
                # -----------------------------
                elif reset_button.collidepoint(event.pos):

                    player1_wins = 0
                    player2_wins = 0

                    board = create_board()
                    current_player = "X"
                    game_over = False

                    status = "Scores reset. Player 1 (X) starts."

                # -----------------------------
                # Quit button
                # -----------------------------
                elif quit_button.collidepoint(event.pos):

                    running = False

                # -----------------------------
                # Board click
                # -----------------------------
                elif (
                    TOP_SPACE
                    <= mouse_y
                    < TOP_SPACE + ROWS * CELL_SIZE
                ):

                    if game_over:
                        status = "Game over. Click Play Again."

                    else:
                        column = mouse_x // CELL_SIZE

                        # Make sure the column is valid
                        if 0 <= column < COLUMNS:

                            move_successful = drop_piece(
                                board,
                                column,
                                current_player
                            )

                            # Column was full
                            if not move_successful:

                                status = (
                                    "That column is full. "
                                    "Choose another column."
                                )

                            else:

                                # Check for winner
                                if check_winner(
                                    board,
                                    current_player
                                ):

                                    game_over = True

                                    if current_player == "X":
                                        player1_wins += 1
                                        status = (
                                            "Player 1 (X) wins! "
                                            "Click Play Again."
                                        )

                                    else:
                                        player2_wins += 1
                                        status = (
                                            "Player 2 (O) wins! "
                                            "Click Play Again."
                                        )

                                # Check for tie
                                elif board_full(board):

                                    game_over = True
                                    status = (
                                        "The game is a tie! "
                                        "Click Play Again."
                                    )

                                # Switch players
                                else:

                                    if current_player == "X":
                                        current_player = "O"
                                        status = (
                                            "Player 2 (O): "
                                            "click a column"
                                        )

                                    else:
                                        current_player = "X"
                                        status = (
                                            "Player 1 (X): "
                                            "click a column"
                                        )

        # -----------------------------
        # Draw graphics
        # -----------------------------
        screen.fill(BACKGROUND)

        draw_centered_text(
            screen,
            "CONNECT 4",
            title_font,
            DARK_BLUE,
            32
        )

        draw_centered_text(
            screen,
            "Player 1: Red (X)   |   Player 2: Yellow (O)",
            small_font,
            DARK_BLUE,
            68
        )

        score_text = (
            "Player 1 (X): "
            + str(player1_wins)
            + "     |     Player 2 (O): "
            + str(player2_wins)
        )

        draw_centered_text(
            screen,
            score_text,
            normal_font,
            DARK_BLUE,
            98
        )

        # Status message
        if "wins" in status:
            status_color = GREEN
        elif "full" in status:
            status_color = RED
        else:
            status_color = DARK_BLUE

        draw_centered_text(
            screen,
            status,
            small_font,
            status_color,
            126
        )

        draw_board(screen, board)

        draw_button(
            screen,
            play_again_button,
            "Play Again",
            small_font
        )

        draw_button(
            screen,
            reset_button,
            "Reset Scores",
            small_font
        )

        draw_button(
            screen,
            quit_button,
            "Quit",
            small_font
        )

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


# -----------------------------
# Start program
# -----------------------------
main()
