import pygame as pg

vec = pg.math.Vector2

FPS = 60
FIELD_COLOR = (48, 39, 32)
BG_COLOR = (0, 0, 0)

SPRITE_DIR_PATH = 'n_fact_tetris/assets/blocks'
FONT_PATH_ONE = 'n_fact_tetris/assets/fonts/FiraMono-Medium.ttf'
FONT_PATH_TWO = 'n_fact_tetris/assets/fonts/FiraSans-Bold.ttf'

SOUND_PATH_FAST_DROP = 'n_fact_tetris/assets/sounds/Drop.wav'
SOUND_PATH_GAMEOVER = 'n_fact_tetris/assets/sounds/Gameover.wav'
SOUND_PATH_LINE_CLEAR = 'n_fact_tetris/assets/sounds/Lineclear.wav'
MUSIC_PATH = 'n_fact_tetris/assets/sounds/9SPADES - sci-fi house.mp3'

HIGH_SCORE_FILE = 'n_fact_tetris/assets/high_score.txt'

QUIT_IMAGE_PATH = 'n_fact_tetris/assets/images/button_quit.png'

ANIM_TIME_INTERVAL = 150  # milliseconds
FAST_ANIM_TIME_INTERVAL = 15

TILE_SIZE = 50
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

FIELD_SCALE_W, FIELD_SCALE_H = 1.7, 1.0
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0)
NEXT_POS_OFFSET = vec(FIELD_W * 1.3, FIELD_H * 0.45)
MOVE_DIRECTIONS = {'left': vec(-1, 0), 'right': vec(1, 0), 'down': vec(0, 1)}

TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}
