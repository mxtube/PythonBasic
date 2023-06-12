"""
Футбольная команда
12.06.2023 @ Kirill Kuznetsov

Вам нужно вычислить очки, набранные футбольной командой ⚽️.
Команда выиграла 18 матчей и 7 завершила вничью.
Победа приносит 3 очка, ничья - 1.
"""

SCORE_WIN = 3
SCORE_DRAW = 1

team_win = int(input('Введите кол-во побед: '))
team_draw = int(input('Введите кол-во ничьи: '))

win_score = int(team_win * SCORE_WIN)
draw_score = int(team_draw * SCORE_DRAW)

score = win_score + draw_score
print('Кол-во очков у команды:', score)
print('Кол-во очков за выйгранные матчи', win_score)
print('Кол-во очков за ничьи', draw_score)
