# Chad Czilli 06/15/2017
# dxfTransfer (A little program to cut and paste our dxf files for toolpath)
import pyautogui, time, sys, os, winsound

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

autocad_program = r"S:\Yachts\Drawings\Finished CadFiles\_CNC DATA\_RENEST\dxf_transfer_master_file.dwg"


move_to_x = 17
move_to_y = 242
sheet_count = 1


number_of_sheets = input('Enter the number of sheets to transfer:')
file_name = input('Enter the name of your project:')

try:
    
    os.startfile(autocad_program)
    
    time.sleep(5)

except:
    print("An error occured")
    


for i in range(int(number_of_sheets)):
    pyautogui.moveTo(move_to_x, move_to_y)
    pyautogui.dragRel(110, 80)  # drag mouse relative to its current position
    time.sleep(1)

    pyautogui.click()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'x')
    time.sleep(1)
    os.startfile(r"C:\Users\cczilli\AppData\Local\Autodesk\AutoCAD LT 2012 - English\R17\enu\Template\dxf_blank.dwt")
    pyautogui.click()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.typewrite("0,0")
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'shift', 's')
    pyautogui.typewrite('{} Sheet {} of {}'.format(file_name, sheet_count, number_of_sheets))
    pyautogui.press('enter')
    pyautogui.click(1881, 194)
    pyautogui.press('enter')
    time.sleep(1)
    
    sheet_count += 1
    move_to_x += 135.5

    if sheet_count == 15:
        move_to_x = 17
        move_to_y = 318
    elif sheet_count == 29:
        move_to_x = 17
        move_to_y = 400
    elif sheet_count == 43:
        move_to_x = 17
        move_to_y = 482
    elif sheet_count == 57:
        move_to_x = 17
        move_to_y = 560
    elif sheet_count == 71:
        move_to_x = 17
        move_to_y = 644
    elif sheet_count == 85:
        move_to_x = 17
        move_to_y = 723
    elif sheet_count == 99:
        move_to_x = 17
        move_to_y = 804

for i in range(5):
    time.sleep(3)
    winsound.PlaySound(r"S:\Product Development\Software Development\Python Programs\DXF Transfer to TP File\ready.wav", winsound.SND_FILENAME)



