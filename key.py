import webbrowser, pyperclip, pyautogui, time, subprocess
from colorama import Fore, Style
import pyperclip as pc
import pyperclip as pyc
from colorama import Fore, Style

elec = input(Fore.GREEN + "Marque (1.) Para borrar registros : " )
if elec=="1":
	print("borrando registros")
	subprocess.getoutput("echo '' > incorrectos.txt && echo ' ' > no_encontrados.txt && echo ' ' > vacios.txt")
	
eleccion = input(Fore.GREEN + "Introduzca tipo de documento: " )
documento = open('direcciones.txt')
documento = documento.read().split('\n')
pyautogui.moveTo(200, 1052)
pyautogui.click()
#subprocess.getoutput("gnome-terminal")
for ip in documento:
	time.sleep(3)		
	pyautogui.hotkey('ctrl', 'r')	
	time.sleep(3)
	pyperclip.copy(ip)
	pyautogui.press('tab')
	pyautogui.press('tab')		
	pyautogui.press("enter")
	time.sleep(3)
	for i in range(4):  
		pyautogui.press('tab')
	pyautogui.hotkey('ctrl', 'v', interval = 0.15)
	pyautogui.press('tab')
	time.sleep(9)
	pyautogui.press('tab')
	pyautogui.press('enter')
	time.sleep(2)
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.hotkey('ctrl', 'c')
	mihco = pyperclip.paste()
	subprocess.getoutput("echo '"+ mihco + "' > mihposa")
	vermih = subprocess.getoutput("""cat mihposa | awk '{for(i=1;i<=NF;i++)if($i=="encontrado") print$i}'| sed 's/ //g'""")
	vermih1 = subprocess.getoutput("""cat mihposa | awk '{for(i=1;i<=NF;i++)if($i=="corresponde") print$i}'| sed 's/ //g'""")

	confirmih = str(vermih)
	confirmih1 = str(vermih1)
	
	if confirmih == "nuevamente":
		subprocess.getoutput("echo '" + eleccion + ip + "' >> no_encontrados.txt")

	elif confirmih1 == "Serial":
		print(ip)
		pyautogui.press('tab')
		pyautogui.press('tab')
		pyautogui.press('tab')
		pyautogui.press('enter')
		time.sleep(3)
		pyautogui.moveTo(700, 210)
		pyautogui.doubleClick()
		pyautogui.hotkey('ctrl', 'a')
		pyautogui.write(eleccion + ip + '.pdf')
		pyautogui.press('enter')		

	else:
		subprocess.getoutput("echo '" + eleccion + ip + "' >> incorrectos.txt")	
		pyautogui.hotkey('ctrl', 'r')	
		time.sleep(3)