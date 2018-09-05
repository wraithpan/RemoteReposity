import requests
from bs4 import BeautifulSoup
import re
import os
import time
import winsound


monster={1:['風方太太','https://search.yahoo.co.jp/realtime/search?p=Lv50+%E3%83%86%E3%82%A3%E3%82%A2%E3%83%9E%E3%83%88&ei=UTF-8'],
         2:['土方太太','https://search.yahoo.co.jp/realtime/search?p=Lv60+%E3%83%A6%E3%82%B0%E3%83%89%E3%83%A9%E3%82%B7%E3%83%AB&ei=UTF-8'],
         3:['水方蛇蛇','https://search.yahoo.co.jp/realtime/search?p=Lv60+%E3%83%AA%E3%83%B4%E3%82%A1%E3%82%A4%E3%82%A2%E3%82%B5%E3%83%B3&ei=UTF-8'],
         4:['火方太太(?)','https://search.yahoo.co.jp/realtime/search?p=Lv70+%E3%82%B3%E3%83%AD%E3%83%83%E3%82%B5%E3%82%B9&ei=UTF-8'],
         5:['光方太太','https://search.yahoo.co.jp/realtime/search?p=Lv75+%E3%82%B7%E3%83%A5%E3%83%B4%E3%82%A1%E3%83%AA%E3%82%A8&ei=UTF-8'],
         6:['暗船太太','https://search.yahoo.co.jp/realtime/search?p=Lv75+%E3%82%BB%E3%83%AC%E3%82%B9%E3%83%88&ei=UTF-8'],
         7:['風方太太HL','https://search.yahoo.co.jp/realtime/search?p=Lv100%20%E3%83%86%E3%82%A3%E3%82%A2%E3%83%9E%E3%83%88'],
         8:['土方太太HL','https://search.yahoo.co.jp/realtime/search?p=Lv100%20%E3%83%A6%E3%82%B0%E3%83%89%E3%83%A9%E3%82%B7%E3%83%AB'],
         9:['水方蛇蛇HL','https://search.yahoo.co.jp/realtime/search?p=Lv100%20%E3%83%AA%E3%83%B4%E3%82%A1%E3%82%A4%E3%82%A2%E3%82%B5%E3%83%B3'],
         10:['火方太太(?)HL','https://search.yahoo.co.jp/realtime/search?p=Lv100%20%E3%82%B3%E3%83%AD%E3%83%83%E3%82%B5%E3%82%B9'],
         11:['光方太太HL','https://search.yahoo.co.jp/realtime/search?p=Lv100%20%E3%82%B7%E3%83%A5%E3%83%B4%E3%82%A1%E3%83%AA%E3%82%A8'],
         12:['暗船太太HL','https://search.yahoo.co.jp/realtime/search?p=Lv100%20%E3%82%BB%E3%83%AC%E3%82%B9%E3%83%88'],
         13:['軍神','https://search.yahoo.co.jp/realtime/search?p=Lv120+%E3%82%B0%E3%83%AA%E3%83%BC%E3%83%A0%E3%83%8B%E3%83%AB&ei=UTF-8'],
         14:['神盾','https://search.yahoo.co.jp/realtime/search?p=Lv120+%E3%82%B4%E3%83%83%E3%83%89%E3%82%AC%E3%83%BC%E3%83%89%E3%83%BB%E3%83%96%E3%83%AD%E3%83%BC%E3%83%87%E3%82%A3%E3%82%A2&ei=UTF-8'],
         15:['歐羅巴','https://search.yahoo.co.jp/realtime/search?p=Lv120+%E3%82%A8%E3%82%A6%E3%83%AD%E3%83%9A&ei=UTF-8'],
         16:['濕婆','https://search.yahoo.co.jp/realtime/search?p=Lv120+%E3%82%B7%E3%83%B4%E3%82%A1&ei=UTF-8'],
         17:['梅塔特隆','https://search.yahoo.co.jp/realtime/search?p=Lv120+%E3%83%A1%E3%82%BF%E3%83%88%E3%83%AD%E3%83%B3&ei=UTF-8'],
         18:['化身','https://search.yahoo.co.jp/realtime/search?p=Lv120+%E3%82%A2%E3%83%90%E3%82%BF%E3%83%BC&ei=UTF-8'],
         19:['哪吒','https://search.yahoo.co.jp/realtime/search?p=Lv100%20%E3%83%8A%E3%82%BF%E3%82%AF&ei=UTF-8'],
         20:['迦樓羅','https://search.yahoo.co.jp/realtime/search?p=Lv100+%E3%82%AC%E3%83%AB%E3%83%BC%E3%83%80&ei=UTF-8'],
         21:['黑肉太太','https://search.yahoo.co.jp/realtime/search?p=Lv100%20%E3%83%95%E3%83%A9%E3%83%A0'],
         22:['小娜娜','https://search.yahoo.co.jp/realtime/search?p=LV100+%E3%82%A2%E3%83%86%E3%83%8A&ei=UTF-8'],
         23:['瑪裘太太','https://search.yahoo.co.jp/realtime/search?p=Lv100%20%E3%83%9E%E3%82%AD%E3%83%A5%E3%83%A9'],
         24:['格拉尼','https://search.yahoo.co.jp/realtime/search?p=Lv100+%E3%82%B0%E3%83%A9%E3%83%8B'],
         25:['小美','https://search.yahoo.co.jp/realtime/search?p=Lv100+%E3%83%A1%E3%83%89%E3%82%A5%E3%83%BC%E3%82%B5&ei=UTF-8'],
         26:['巴爾','https://search.yahoo.co.jp/realtime/search?p=Lv100%20%E3%83%90%E3%82%A2%E3%83%AB&ei=UTF-8'],
         27:['小P孩','https://search.yahoo.co.jp/realtime/search?p=Lv100+%E3%82%A2%E3%83%9D%E3%83%AD%E3%83%B3&ei=UTF-8'],
         28:['D天太太','https://search.yahoo.co.jp/realtime/search?p=Lv100%20D%E3%82%A8%E3%83%B3%E3%82%B8%E3%82%A7%E3%83%AB'],
         29:['哪吒HL','https://search.yahoo.co.jp/realtime/search?p=Lv120%20%E3%83%8A%E3%82%BF%E3%82%AF&ei=UTF-8'],
         30:['BBA','https://search.yahoo.co.jp/realtime/search?p=Lv110%20%E3%83%AD%E3%83%BC%E3%82%BA%E3%82%AF%E3%82%A4%E3%83%BC%E3%83%B3'],
         31:['黑肉太太HL','https://search.yahoo.co.jp/realtime/search?p=Lv120%20%E3%83%95%E3%83%A9%E3%83%A0'],
         32:['瑪裘太太HL','https://search.yahoo.co.jp/realtime/search?p=Lv120%20%E3%83%9E%E3%82%AD%E3%83%A5%E3%83%A9&ei=UTF-8'],
         33:['小梅HL','https://search.yahoo.co.jp/realtime/search?p=Lv120%20%E3%83%A1%E3%83%89%E3%82%A5%E3%83%BC%E3%82%B5'],
         34:['小屁孩HL','https://search.yahoo.co.jp/realtime/search?p=Lv120%20%E3%82%A2%E3%83%9D%E3%83%AD%E3%83%B3'],
         35:['D天太太HL','https://search.yahoo.co.jp/realtime/search?p=Lv120%20D%E3%82%A8%E3%83%B3%E3%82%B8%E3%82%A7%E3%83%AB&ei=UTF-8'],
         36:['小巴巴','https://search.yahoo.co.jp/realtime/search?p=Lv100+%E3%83%97%E3%83%AD%E3%83%88%E3%83%90%E3%83%8F%E3%83%A0%E3%83%BC%E3%83%88&ei=UTF-8'],
         37:['大巴巴','https://search.yahoo.co.jp/realtime/search?p=Lv150+%E3%83%97%E3%83%AD%E3%83%88%E3%83%90%E3%83%8F%E3%83%A0%E3%83%BC%E3%83%88&ei=UTF-8'],
         38:['丁丁','https://search.yahoo.co.jp/realtime/search?p=Lv100+%E3%82%B8&ei=UTF-8'],
         39:['黑70','https://search.yahoo.co.jp/realtime/search?p=Lv100+%E9%BB%92%E9%BA%92%E9%BA%9F&ei=UTF-8'],
	 40:['黃70','https://search.yahoo.co.jp/realtime/search?p=Lv100%20%E9%BB%84%E9%BE%8D'],
         41:['米迦勒','https://search.yahoo.co.jp/realtime/search?p=Lv100%20%E3%83%9F%E3%82%AB%E3%82%A8%E3%83%AB'],
         42:['加百醬','https://search.yahoo.co.jp/realtime/search?p=Lv100%20%E3%82%AC%E3%83%96%E3%83%AA%E3%82%A8%E3%83%AB'],
         43:['烏列爾','https://search.yahoo.co.jp/realtime/search?p=Lv100%20%E3%82%A6%E3%83%AA%E3%82%A8%E3%83%AB'],
         44:['HRT','https://search.yahoo.co.jp/realtime/search?p=Lv100%20%E3%83%A9%E3%83%95%E3%82%A1%E3%82%A8%E3%83%AB'],
         50:['古戰EX','https://search.yahoo.co.jp/realtime/search?p=Lv75+%E3%83%86%E3%82%A3%E3%83%A9%E3%83%8E%E3%82%B9'],
         101:['朱雀','https://search.yahoo.co.jp/realtime/search?p=Lv60+%E6%9C%B1%E9%9B%80&ei=UTF-8'],     
         102:['玄武','https://search.yahoo.co.jp/realtime/search?p=Lv60+%E7%8E%84%E6%AD%A6&ei=UTF-8'],     
         103:['白虎','https://search.yahoo.co.jp/realtime/search?p=Lv60+%E7%99%BD%E8%99%8E&ei=UTF-8'],   
         104:['青龍','https://search.yahoo.co.jp/realtime/search?p=Lv60+%E9%9D%92%E7%AB%9C&ei=UTF-8'],     
         105:['阿格尼','https://search.yahoo.co.jp/realtime/search?p=Lv90+%E3%82%A2%E3%82%B0%E3%83%8B%E3%82%B9&ei=UTF-8'],     
         106:['尼普頓太太','https://search.yahoo.co.jp/realtime/search?p=Lv90+%E3%83%8D%E3%83%97%E3%83%81%E3%83%A5%E3%83%BC%E3%83%B3&ei=UTF-8'],     
         107:['泰坦','https://search.yahoo.co.jp/realtime/search?p=Lv90+%E3%83%86%E3%82%A3%E3%82%BF%E3%83%BC%E3%83%B3&ei=UTF-8'],	     
         108:['狗男女','https://search.yahoo.co.jp/realtime/search?p=Lv90+%E3%82%BC%E3%83%94%E3%83%A5%E3%83%AD%E3%82%B9&ei=UTF-8']}	 
matchid = 'nonevalue'

def choose():
    try:
        global choice_i
        print("--------------------------方陣--------------------------")
        print("1.風方EX 2.土方EX 3.水方EX 4.火方EX 5.光方EX 6.暗方EX\n7.風方HL 8.土方HL 9.水方HL 10.火方HL 11.光方HL 12.暗方HL\n13.風方120 14.土方120 15.水方120 16.火方120 17.光方120 18.暗方120")
        print("-------------------------召喚石-------------------------")
        print("19.哪吒 20.迦樓羅 21.弗拉姆 22.雅典那 23.瑪裘拉 24.格拉尼 25.梅杜莎 26.巴爾 27.阿波羅 28.D天")
        print("----------------------召喚石6人HL-----------------------")
        print("29.哪吒HL 30.JK 31.弗拉姆HL 32.瑪裘拉HL 33.梅杜莎HL 34.阿波羅HL 35.D天HL")
        print("--------------------------其他--------------------------")             
        print("36.小巴 37.大巴 38.格蘭丁 39.黑麒麟 40.黃龍\n41.米迦勒(火天使) 42.加百列(水天使) 43.烏列爾(土天使) 44.拉斐爾(風天使)")
        print("--------------------------四象--------------------------")        
        print("101.朱雀 102.玄武 103.白虎 104.青龍 105.阿格尼斯 106.尼普頓 107.泰坦 108.澤費洛斯")
        
        choice_i = int(input('請選擇需偵測的任務 : '))
    except :
        choice_i = 'error'
        pass
def choose2():    
    if choice_i in monster.keys():
        print("開始偵測%s\n按ctrl+c以暫停或更改搜尋選項"%monster[choice_i][0])
        global url
        url = monster[choice_i][1]
        loopparse()
    else:
        print("賣鬧")
        pass

def loopparse():
    try:
        while True:
            YAHOOpar()
            time.sleep(3)
    except KeyboardInterrupt:
        pass           
    
def addToClipBoard(text):
	command = 'echo ' + text.strip() + '| clip'
	os.system(command)
        

def YAHOOpar():
    
    try:
        res=requests.get(url)       
        restext=res.text
        
        bs=BeautifulSoup(restext, "html.parser")
        msg=bs.findAll("div",{'class':'cnt cf'})
        
        timedict=dict()
        for i in msg:
            commenttime=i.get_text().split('\n')[9]
            if '秒前' in commenttime:
                pid=re.findall(r'[A-Z0-9]{8}',i.get_text().split('\n')[2])[0]
                if pid in timedict.keys() and int(re.sub("[^0-9]","",timedict[pid])) < int(re.sub("[^0-9]","",commenttime)):
                    pass
                else:
                    timedict[pid]=commenttime

        mintime=7
        
        for i in timedict.keys() :
            if int(re.sub("[^0-9]","",timedict[i]))<7:
                matchtime=int(re.sub("[^0-9]","",timedict[i]))
                if matchtime < mintime:
                    mintime=matchtime
                    matchid=i
                    now=time.localtime()
                    print("發現{}\n{:0>2}:{:0>2}:{:0>2}    {}".format(monster[choice_i][0],str(now.tm_hour),str(now.tm_min),str(now.tm_sec),matchid))
                    addToClipBoard(matchid)
                    winsound.PlaySound('alert.wav', winsound.SND_FILENAME)
                else:
                    pass

        
    except PermissionError:
        print('未發現目標')
        

while True:
    choose()
    choose2()
    print("\n")

