import numpy as np
import pygame
import math

ROWS = 3
COLUMNS = 3

# Kích thước cửa sổ trò chơi
W_WINDOW = 600
H_WINDOW = 600
SIZE = (W_WINDOW, H_WINDOW)

# Một số màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)  # Màu cho X
BLUE = (0, 0, 255)  # Màu cho O

# Tạo bảng trò chơi
board = np.zeros((ROWS, COLUMNS))


# Kiểm tra ô có trống không
def is_valid_mark(row, col):
    return board[row][col] == 0


# Điền ô được chọn
def mark(row, col, player):
    board[row][col] = player


# Kiểm tra bảng đã đầy hay chưa
def is_board_full():
    for r in range(ROWS):
        for c in range(COLUMNS):
            if board[r][c] == 0:
                return False
    return True


# Vẽ các đường chia ô
def draw_line():
    pygame.draw.line(window, BLACK, (200, 0), (200, 600), 10)
    pygame.draw.line(window, BLACK, (400, 0), (400, 600), 10)
    pygame.draw.line(window, BLACK, (0, 200), (600, 200), 10)
    pygame.draw.line(window, BLACK, (0, 400), (600, 400), 10)


# Hàm vẽ X và O dựa trên nội dung của board
def draw_figures():
    for r in range(ROWS):
        for c in range(COLUMNS):
            if board[r][c] == 1:
                # Vẽ X: vẽ hai đường chéo
                start_desc = (c * 200 + 50, r * 200 + 50)
                end_desc = ((c + 1) * 200 - 50, (r + 1) * 200 - 50)
                pygame.draw.line(window, RED, start_desc, end_desc, 15)

                start_asc = (c * 200 + 50, (r + 1) * 200 - 50)
                end_asc = ((c + 1) * 200 - 50, r * 200 + 50)
                pygame.draw.line(window, RED, start_asc, end_asc, 15)
            elif board[r][c] == 2:
                # Vẽ O: vẽ hình tròn
                center = (int(c * 200 + 200 / 2), int(r * 200 + 200 / 2))
                radius = 70
                pygame.draw.circle(window, BLUE, center, radius, 15)


# Kiểm tra thắng cuộc
def is_winning_move(player):
    annoucement = "Player 1 won" if player == 1 else "Player 2 won"

    # Kiểm tra hàng ngang
    for r in range(ROWS):
        if board[r][0] == player and board[r][1] == player and board[r][2] == player:
            print(annoucement)
            return True

    # Kiểm tra hàng dọc
    for c in range(COLUMNS):
        if board[0][c] == player and board[1][c] == player and board[2][c] == player:
            print(annoucement)
            return True

    # Kiểm tra đường chéo chính
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        print(annoucement)
        return True

    # Kiểm tra đường chéo phụ
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        print(annoucement)
        return True

    return False


game_over = False
Turn = 0

# Khởi tạo giao diện
pygame.init()
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Tic Tac Toe 3x3")
window.fill(WHITE)
draw_line()
pygame.display.update()
pygame.time.wait(500)

# Vòng lặp chính của trò chơi
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            row = math.floor(pos[1] / 200)
            col = math.floor(pos[0] / 200)

            if is_valid_mark(row, col):
                player = 1 if Turn % 2 == 0 else 2
                mark(row, col, player)
                draw_figures()  # Vẽ lại X hoặc O ngay sau khi đánh dấu
                pygame.display.update()

                if is_winning_move(player):
                    game_over = True
                    break
                if is_board_full():
                    game_over = True
                    break
                Turn += 1
            else:
                # Nếu ô đã được đánh, không tăng lượt người chơi
                print("Ô đã được chọn, hãy chọn ô khác.")

    if game_over:
        print("Game Over")
