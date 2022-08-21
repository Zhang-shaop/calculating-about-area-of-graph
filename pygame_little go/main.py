##这个程序的功能很完备了，只需要把每次的输出结果存入文件就可以了。然后就是尽量增加一个计时的功能。

import ctypes

import pygame

# 初始化 pygame
pygame.init()

# 定义颜色
blue = (78, 140, 243)
light_blue = (100, 100, 255)
red = (242, 89, 97)
light_red = (255, 100, 100)
dark_grey = (85, 85, 85)
light_grey = (100, 100, 100)
background_color = (225, 225, 225)

# 创建窗口
screen = pygame.display.set_mode((600, 650))
pygame.display.set_caption('井字棋小游戏')

# 游戏图片载入
crossImg = pygame.image.load('Images/crossImg.png') #这里的是深色的叉，落子的圆
crossImg_rect = crossImg.get_rect()  #获取图片的大小，并且规定中心位置
crossImg_rect.center = (200, 300)
circleImg = pygame.image.load('Images/circleImg.png')
circleImg_rect = crossImg.get_rect()
circleImg_rect.center = (400, 300)
previewCrossImg = pygame.image.load('Images/prev_crossImg.png')  #这是浅色的叉
previewCircleImg = pygame.image.load('Images/prev_circleImg.png')

# 按钮图片
restartImg = pygame.image.load('Images/restart.png')
restartHoveredImg = pygame.image.load('Images/restart_hovered.png') #每张图片都做两份，可以做出点击的动态效果

# 定义棋盘，使用空的二维数组来定义棋盘
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

# 定义计分板
score = {'X': 0, 'O': 0}
font = pygame.font.Font('freesansbold.ttf', 32)  #这是规定的一种字体。
X_score = pygame.image.load('Images/X_scoreImg.png')
O_score = pygame.image.load('Images/O_scoreImg.png')

# 菜单图片
buttom1 = pygame.image.load('Images/button1Img.png')
buttom1_rect = buttom1.get_rect()
buttom1_rect.center = (300, 312)
buttom2 = pygame.image.load('Images/button2Img.png')
buttom2_rect = buttom2.get_rect()
buttom2_rect.center = (300, 472)
logo = pygame.image.load('Images/logo.png')

# 选择菜单图片
chooseImg = pygame.image.load('Images/choose.png')

#构建一个菜单函数
def menu():
    running = True
    while running:    #菜单一直存在直到running改变。不断检测事件，
        screen.fill(background_color)
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttom1_rect.collidepoint((mx, my)):
                    hisfile.write('I choose to play with friends!\n')  # 我增加的功能，就是每次选择都把结果写入文件#
                    game(0, 'X')  ##这里有一个game函数，表示选择x
                elif buttom2_rect.collidepoint((mx, my)):
                    hisfile.write('I choose to play with AI!\n ')  # 我增加的功能，就是每次选择都把结果写入文件#
                    player = choose()   #这里有一个选择函数
                    if player is not None:
                        game(1, player)
        screen.blit(logo, (8, 25))    #因为pygame不支持内置组件，所以要么自己定义组件，要么用图片来代替。凡是文字的部分都有图片代替。
                                      #而点击效果，可以检测鼠标的点击事件的位置是否在图片区域，如果在图片区域，就可以用两张图片的切换来表达。
        screen.blit(buttom1, (100, 250))
        screen.blit(buttom2, (100, 410))
        pygame.display.update() #试试刷新display

#在菜单中用到了这个游戏函数
def game(gameMode, player):
    my = player
    player = 'X'
    running = True
    previewImg = previewCrossImg
    while running:
        mouse = pygame.mouse.get_pos()
        row, col = int(mouse[0] / 200), int(mouse[1] / 200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                resetGame()
                running = False
            elif isBoardFull():
                ctypes.windll.user32.MessageBoxW(0, '平局', '提示', 0)
                hisfile.write('draw \n ')
                resetBoard()
            elif gameMode == 1 and player != my:
                computerMove(player)
                drawBoard()


                pygame.display.update()
                if verifyWinner(player):
                    player = 'X'
                    previewImg = previewCrossImg
                else:
                    player, previewImg = updatePlayer(player)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if row < 3 and col < 3 and board[row][col] == '':
                    playerMove(player, row, col)
                    drawBoard()
                    hisfile.write('['+board[0][0]+','+board[0][1]+','+board[0][2]+']'+'\n')
                    hisfile.write('[' + board[1][0] + ',' + board[1][1] + ',' + board[1][2] + ']'+'\n')
                    hisfile.write('[' + board[2][0] + ',' + board[2][1] + ',' + board[2][2] + ']'+'\n')
                    hisfile.write('\n')
#####最重要的修改！
                    pygame.display.update()
                    if verifyWinner(player):
                        player = 'X'
                        previewImg = previewCrossImg
                    else:
                        player, previewImg = updatePlayer(player)
                elif 550 < mouse[0] < 582 and 610 < mouse[1] < 642:
                    resetGame()
        screen.fill(background_color)
        drawBoard()
        drawBottomMenu(mouse)
        if row < 3 and col < 3:
            visualizeMove(row, col, previewImg)
        pygame.display.update()


def choose():
    player = None
    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if crossImg_rect.collidepoint((mouse[0], mouse[1])):
                    player = 'X'
                    hisfile.write('I choose X\n')  #我增加的功能，就是每次选择都把结果写入文件#
                    running = False
                elif circleImg_rect.collidepoint((mouse[0], mouse[1])):
                    player = 'O'
                    hisfile.write('I choose O\n')  # 我增加的功能，就是每次选择都把结果写入文件#
                    running = False
        screen.blit(crossImg, (80, 300))
        screen.blit(circleImg, (340, 300))
        screen.blit(chooseImg, (8, 25))
        pygame.display.update()
    return player


def drawBoard():
    # 画棋子
    for row in range(3):
        for col in range(3):
            pos = (row * 200 + 12, col * 200 + 12)
            if board[row][col] == 'X':
                screen.blit(crossImg, pos)
            elif board[row][col] == 'O':
                screen.blit(circleImg, pos)


    # 画网格
    width = 10
    color = dark_grey
    pygame.draw.line(screen, color, (200, 0), (200, 600), width)
    pygame.draw.line(screen, color, (400, 0), (400, 600), width)
    pygame.draw.line(screen, color, (0, 200), (600, 200), width)
    pygame.draw.line(screen, color, (0, 400), (600, 400), width)
    # 画边框
    pygame.draw.rect(screen, color, (0, 0, 10, 600))
    pygame.draw.rect(screen, color, (0, 0, 600, 10))
    pygame.draw.rect(screen, color, (590, 0, 10, 600))


def drawBottomMenu(mouse):
    pygame.draw.rect(screen, dark_grey, (0, 600, 600, 100))
    pygame.draw.rect(screen, light_grey, (10, 610, 580, 80))
    screen.blit(restartImg, (550, 610))
    # Hover animation
    if 550 < mouse[0] < 582 and 610 < mouse[1] < 642:
        screen.blit(restartHoveredImg, (548, 608))
    screen.blit(X_score, (200, 610))
    screen.blit(O_score, (370, 610))
    scoreboard = font.render(': %d x %d :' % (score['X'], score['O']), True, background_color, light_grey)
    screen.blit(scoreboard, (244, 610))


def visualizeMove(row, col, previewImg):
    if board[row][col] == '':
        screen.blit(previewImg, (row * 200 + 12, col * 200 + 12))


def playerMove(player, row, col):
    board[row][col] = player


def computerMove(player):
    bestScore = float('inf')
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                board[row][col] = 'O'
                score = minimax(board, 'X')
                board[row][col] = ''
                if score < bestScore:
                    bestScore = score
                    bestMove = (row, col)
    board[bestMove[0]][bestMove[1]] = player


scores = {'X': 1, 'O': -1, 'tie': 0}


def minimax(board, cur_player):
    if isWinner('X'):
        return scores['X']
    elif isWinner('O'):
        return scores['O']
    elif isBoardFull():
        return scores['tie']
    if cur_player == 'X':
        bestScore = float('-inf')
        nextPlayer = 'O'
        minORmax = max
    else:
        bestScore = float('inf')
        nextPlayer = 'X'
        minORmax = min
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                board[row][col] = cur_player
                score = minimax(board, nextPlayer)
                board[row][col] = ''
                bestScore = minORmax(score, bestScore)
            if bestScore == scores[cur_player]:
                return bestScore
    return bestScore


def updatePlayer(player):
    if player == 'X':
        newPlayer = 'O'
        previewImg = previewCircleImg
    else:
        newPlayer = 'X'
        previewImg = previewCrossImg
    return newPlayer, previewImg



def isWinner(player):
    return ((board[0][0] == player and board[0][1] == player and board[0][2] == player) or
            (board[1][0] == player and board[1][1] == player and board[1][2] == player) or
            (board[2][0] == player and board[2][1] == player and board[2][2] == player) or
            (board[0][0] == player and board[1][0] == player and board[2][0] == player) or
            (board[0][1] == player and board[1][1] == player and board[2][1] == player) or
            (board[0][2] == player and board[1][2] == player and board[2][2] == player) or
            (board[0][0] == player and board[1][1] == player and board[2][2] == player) or
            (board[0][2] == player and board[1][1] == player and board[2][0] == player))


def verifyWinner(player):
    if isWinner(player):
        score[player] += 1
        ctypes.windll.user32.MessageBoxW(0, player + ' 获胜！', '提示', 0)
        hisfile.write(player+'  win!\n')  # 我增加的功能，就是每次选择都把结果写入文件#
        resetBoard()
        return True
    return False


def isBoardFull():
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                return False
    return True


def resetBoard():
    for i in range(3):
        for j in range(3):
            board[i][j] = ''


def resetGame():
    resetBoard()
    score['X'] = 0
    score['O'] = 0
    hisfile.write('reset!\n\n')  # 我增加的功能，就是每次选择都把结果写入文件#

hisfile=open('history', 'w')  # 以写入权限加入文件#####
hisfile.write('['+ ' '+','+' '+','+' '+']'+'\n'
               '['+ ' '+','+' '+','+' '+']'+'\n'
              '['+ ' '+','+' '+','+' '+']'+'\n')
hisfile.write('The data is below:\n')
menu()
hisfile.close()