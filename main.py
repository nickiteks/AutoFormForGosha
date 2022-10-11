import pyautogui
import keyboard
import time
import pyperclip

room_number = 4
list_of_fields = {  
    'pasport':'1111 11111',
    'name1':'ИТкуб',
    'name2':'ИТкуб',
    'name3':'ИТкуб',
    'addres': 'Адрес на русском',
    'periud': '05.10.2022 12:30 - 05.10.2023 04:30',
    'pasport_given':'10',
    'born_date':'18.10.1974',
    'podr_rey':'456446'
}

while True:
        try: 
            if keyboard.is_pressed('1'):
                time.sleep(1)
                pyautogui.press('backspace')
                pyautogui.write(str(room_number+1))
                room_number +=1
                pyautogui.press('tab')
                
                for i in list_of_fields:
                    pyperclip.copy(list_of_fields[i])
                    time.sleep(0.1)
                    pyautogui.hotkey('ctrl', 'v')
                    pyautogui.press('tab')


            if keyboard.is_pressed('2'):  
                pyautogui.press('backspace')
                break
        except:
            break