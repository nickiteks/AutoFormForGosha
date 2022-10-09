import pyautogui
import keyboard
import time

room_number = 4
pasport = '1111 11111'
name = 'nnnn'
addres = 'ajhwbdjawhbd'
periud = '05.10.2022 12:30 - 05.10.2023 04:30'
pasport_given = '03.10.2022'
born_date = '18.10.1974'
podr_rey = '456446'


while True:
        try: 
            if keyboard.is_pressed('1'):
                time.sleep(1)
                pyautogui.press('backspace')
                pyautogui.write(str(room_number+1))
                room_number +=1
                pyautogui.press('tab')

                pyautogui.write(pasport)
                pyautogui.press('tab')

                pyautogui.write(name)
                pyautogui.press('tab')

                pyautogui.write(name)
                pyautogui.press('tab')

                pyautogui.write(name)
                pyautogui.press('tab')

                pyautogui.write(addres)
                pyautogui.press('tab')


                pyautogui.write(periud)
                pyautogui.press('tab')

                pyautogui.write(pasport_given)
                pyautogui.press('tab')

                pyautogui.write(born_date)
                pyautogui.press('tab')

                pyautogui.write(podr_rey)


            if keyboard.is_pressed('2'):  
                pyautogui.press('backspace')
                break
        except:
            break