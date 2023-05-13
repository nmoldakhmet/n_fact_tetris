from settings import *
from tetris import Tetris, Text
import sys
import pathlib
from os import path

class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pg.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		pos = pg.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pg.mouse.get_pressed()[0] == 0:
			self.clicked = False
		surface.blit(self.image, (self.rect.x, self.rect.y))
		return action



class App:
    def __init__(self):
        pg.init()
        pg.mixer.music.load(MUSIC_PATH)
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(0.2)
        pg.display.set_caption('Tetris')
        self.screen = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.set_timer()
        self.images = self.load_images()
        self.tetris = Tetris(self)
        self.text = Text(self)
        self.mixer = pg.mixer
 


    def load_images(self):
        files = [item for item in pathlib.Path(SPRITE_DIR_PATH).rglob('*.png') if item.is_file()]
        images = [pg.image.load(file).convert_alpha() for file in files]
        images = [pg.transform.scale(image, (TILE_SIZE, TILE_SIZE)) for image in images]
        return images

    def set_timer(self):
        self.user_event = pg.USEREVENT + 0
        self.fast_user_event = pg.USEREVENT + 1
        self.anim_trigger = False
        self.fast_anim_trigger = False
        pg.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)
        pg.time.set_timer(self.fast_user_event, FAST_ANIM_TIME_INTERVAL)

    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(color=BG_COLOR)
        self.screen.fill(color=FIELD_COLOR, rect=(0, 0, *FIELD_RES))
        self.tetris.draw()
        self.text.draw()
        pg.display.flip()

    def check_events(self):
        self.anim_trigger = False
        self.fast_anim_trigger = False
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.game_pause()
            elif event.type == pg.QUIT:
                pg.quit()
                sys.exit()                    
            elif event.type == pg.KEYDOWN:
                self.tetris.control(pressed_key=event.key)
            elif event.type == self.user_event:
                self.anim_trigger = True
            elif event.type == self.fast_user_event:
                self.fast_anim_trigger = True

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

    def game_pause(self):
        pause = True
        while pause:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE: 
                    pause = False
                    app.run()
                elif self.text.quit_button.draw(self.screen):
                    pause = False
                    pg.quit()
                    sys.exit()                                          
            self.screen.fill('black')
            self.text.draw_paused()              
            self.clock.tick(15)

    def main_menu(self):
        main_menu = True
        self.screen.fill('black')
        self.text.draw_main_menu()
        self.text.font.render_to(self.screen, (WIN_W * 0.32, WIN_H * 0.02), text='TETRIS', fgcolor=self.text.get_color(), size=TILE_SIZE * 1.65, bgcolor='black')
        self.text.font.render_to(self.screen, (WIN_W * 0.15, WIN_H * 0.8), text='Click SPACE to START the game', fgcolor=self.text.get_color(), size=TILE_SIZE // 1.5, bgcolor='black')
        self.text.font_two.render_to(self.screen, (WIN_W * 0.1, WIN_H * 0.2), text="Last score: " + f'{self.tetris.score}', fgcolor=self.text.get_color(), size=TILE_SIZE * 1.3, bgcolor='black')
        self.text.font_two.render_to(self.screen, (WIN_W * 0.1, WIN_H * 0.3), text='Highest Score: ' + str(self.tetris.high_score), fgcolor=self.text.get_color(), size=TILE_SIZE * 1.3, bgcolor='black')
        pg.display.flip()    
        while main_menu:
           for event in pg.event.get():  
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:  
                    main_menu = False
                    app = App()
                    app.run()
                elif event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif self.text.quit_button.draw(self.screen):
                    pg.quit()
                    sys.exit()         
        pg.display.flip() 



if __name__ == '__main__':
    app = App()
    app.main_menu()
