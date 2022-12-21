import pygame as pg
import sys
import ctypes
import random as r
user32 = ctypes.windll.user32

pg.init()
win = pg.display.set_mode((user32.GetSystemMetrics(0),user32.GetSystemMetrics(1)-60))
win.fill((0,0,0))

pr = True

pressed = False
cl = pg.time.Clock()

while pr:
	pos = pg.mouse.get_pos()
	cl.tick(50)
	for ev in pg.event.get():
		if ev.type == pg.QUIT:
			pr = False
			pg.quit()
			sys.exit()
	pr = pg.mouse.get_pressed()
	if pr[0]:
		p = pg.mouse.get_pos()
		x = pos[0]
		y = pos[1]
		pg.draw.line(win,(0,255,0),(x,y),p,1)
	if pr[2]:
		p = pg.mouse.get_pos()
		x = pos[0]
		y = pos[1]
		pg.draw.rect(win,(0,0,0),(x-50,y-50,100,100))
	pg.display.update()
