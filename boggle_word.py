#https://www.codewars.com/kata/57680d0128ed87c94f000bfd
moves = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]


def step(board, word,i,j):
    if len(word) == 0:
        return True
    for move in moves:
        if board[i+move[0]][j+move[1]] == word[0]:
            board[i+move[0]][j+move[1]] = ''
            if step(board, word[1:], i+move[0],j+move[1]):
                return True
            board[i + move[0]][j + move[1]] = word[0]
    return False


def find_word(board, word):
    if len(board) == 0:
        return False
    if len(board[0]) == 0:
        return
    wboard = [row[:] for row in board]
    for i in range(len(wboard)):
        wboard[i].append('')
        wboard[i].insert(0,'')
    wboard.insert(0,['' for x in range(len(wboard[0]))])
    wboard.append(wboard[0])

    for i in range(len(wboard)):
        for j in range(len(wboard[0])):
            if wboard[i][j]==word[0]:
                wboard[i][j]=''
                if step(wboard,word[1:],i,j):
                    return True
                wboard[i][j]=word[0]
    return False
