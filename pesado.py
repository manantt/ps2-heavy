import win32api, win32con, time
from PIL import ImageGrab
from PIL import Image
from playsound import playsound
from win32api import GetKeyState



escudoX = 1703
escudoY = 1027
escudoW = 155

#for x in range(0,60):
#	time.sleep(1)
#	img = ImageGrab.grab((escudoX, escudoY, escudoX+escudoW, escudoY+1))
#	img.save(str(x)+"a.png")
#	print(str(x))

value = (255, 250, 250, 1)
shieldX = 828
shieldY = 837
shieldW = 258

#indica si un pixel es rojo
def esAzul(rgb):
	if rgb[0] < 100:
		return False
	if rgb[1] < 180:
		return False
	if rgb[2] < 190:
		return False
	return True

def activarEscudo():
	f = 0x46
	win32api.keybd_event(f,0,0,0)
	time.sleep(0.1)
	win32api.keybd_event(f,0,win32con.KEYEVENTF_KEYUP,0)
	playsound('alert.wav', False)
	
def keyIsDown(key):
	keystate = GetKeyState(key)
	if (keystate != 0) and (keystate != 1):
		return True
	else:
		return False

def checkActivar():
	if keyIsDown(0x78):
		playsound('on.wav', False)
		time.sleep(1)
		return True
	return False

def checkDesactivar():
	if keyIsDown(0x78):
		playsound('off.wav', False)
		time.sleep(1)
		return True
	return False

activo = False
while True:
	time.sleep(0.1)
	if activo == True:
		while activo:
			im = ImageGrab.grab((escudoX+1, escudoY, escudoX+2, escudoY+1))
			pix = im.load()
			contador = 0
			if not esAzul(pix[0,0]):
				activarEscudo()
				time.sleep(12)
			else:
				print("else")
			activo = not checkDesactivar()
	else:
		activo = checkActivar()

#im.save('aaa.png')  # Save the modified pixels as .png


