def validate_board(board):
    if not type(board) is list:
        return False
    sum_1=0;
    sum_2=0;
    if len(board)==3:
        for line in board:
            if len(line) == 3:
                sum_1= sum_1 + line.count(1)
                sum_2 =sum_2 + line.count(2)
                for n in line:
                    if n not in [0, 1, 2]:
                        return False
            else:
                return False
        if 0 <= sum_1-sum_2 <= 1:
            return True
    return False

def game_finished(board):
    if not validate_board(board):
        return -1

    sum_0 = 0;

    if (board[0][0]==board[1][1]==board[2][2]==1) or (board[0][2]==board[1][1]==board[2][0]==1):
        return 1
    if (board[0][0]==board[1][1]==board[2][2]==2) or (board[0][2]==board[1][1]==board[2][0]==2):
        return 2

    if (board[0][0] == board[1][0] == board[2][0] == 1) or (board[0][1] == board[1][1] == board[2][1] == 1) or (board[0][2] == board[1][2] == board[2][2] == 1):
        return 1
    if (board[0][0] == board[1][0] == board[2][0] == 2) or (board[0][1] == board[1][1] == board[2][1] == 2) or (board[0][2] == board[1][2] == board[2][2] == 2):
        return 2

    for line in board:
        if line.count(1)== 3:
            return 1
        if line.count(2)== 3:
            return 2
        sum_0 = sum_0 + line.count(0)
    if sum_0 <= 0:
        return -1
    return 0


def render_board(board):
   html='<table>'
   for line in board:
       html=html+'<tr>'
       for l in line:
           if l == 1:
               html=html+'<td>X</td>'
           elif l==2:
               html=html+'<td>O</td>'
           else:
               html = html + '<td>&nbsp;</td>'
       html = html + "</tr>"
   return html + '</table>'

