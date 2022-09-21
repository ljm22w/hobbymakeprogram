import tkinter
import time
import os

print ('파이알람 윈도우 버전에 오신걸 환영합니다.')
print ('환영합니다. 몇 시간 뒤에 알람을 울릴까요? (알람이 울리기 전 까지는 이 프로그램을 종료하지 마세요.)')
hour = int(input ())

print ('몇 분 뒤에 알람을 울릴까요?')
mn = int(input())

print ('몇 초 뒤에 알람을 울릴까요?')
sc = int(input())


time1 = (hour * 3600) + (mn * 60) + sc

os.system('cls')

print ('알람이 시작되었습니다.')
time.sleep(time1)

os.system('echo msgbox "알람이 종료되었습니다.",64,"알람 종료!" > fkjajfkdfkasfiojapdfjakjdkfjadkfakl.vbs & start /wait fkjajfkdfkasfiojapdfjakjdkfjadkfakl.vbs & del fkjajfkdfkasfiojapdfjakjdkfjadkfakl.vbs')
