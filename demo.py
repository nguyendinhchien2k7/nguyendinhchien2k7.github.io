import colorama
import pyttsx3
from colorama import Fore
from colorama import Style
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import codecs
print("              =================================================================================")
print(Fore.BLUE + Style.BRIGHT + "                                               Hưỡng Dẫn Làm Bài               " + Style.RESET_ALL)
print("                  Chọn đáp án từ bàn phím A,B,C,D")
print("                  Chọn đáp án đúng +1 điểm")
print("                  Chọn đáp án sai chương trình chuyển sang câu hỏi khác")
print("                  Sau khi trả lời hết các câu hỏi chương trình sẽ in ra số điểm bạn đạt được")
print("                  Facebook admin : https://www.facebook.com/ChienPc.xDeveloper")
print("                  Soure code ib Facebook : Nguyễn Đình Chiến")
print("              =================================================================================")
print()
while True:
    fin = open("CauHoi.INP","r",encoding='utf-8')
    a = fin.readlines()
    dapan = open("DapAn.INP","r",encoding='utf-8')
    b = dapan.readline().upper().split()
    abcd = open("ABCD.INP","r",encoding='utf-8')
    dem = 0
    x = 0
    themcau = 0
    while x <= len(b):
        while themcau <= len(a):
            if a[themcau] in a:
                print(Fore.BLUE + Style.BRIGHT + "Câu 1:",a[themcau] + Style.RESET_ALL)
                print(abcd.readline())
                print(abcd.readline())
                chon = input("    Chọn đáp án của bạn: " ).upper()
                if chon == "{}".format(b[x]):
                    print("    Câu trả lời chính xác")
                    engine = pyttsx3.init()
                    engine1 = pyttsx3.init()
                    engine.say("Very good")
                    engine1.say("Good luck")
                    engine.runAndWait()
                    engine1.runAndWait()
                    dem += 1 
                else:
                    print(Fore.RED + Style.BRIGHT + "    Câu trả lời sai." + Style.RESET_ALL)
                x += 1
                themcau += 1
            if a[themcau] in a:
                print(Fore.BLUE + Style.BRIGHT + "Câu 2:",a[themcau] + Style.RESET_ALL)
                print(abcd.readline())
                print(abcd.readline())
                chon = input("    Chọn đáp án của bạn: " ).upper()
                if chon == "{}".format(b[x]):
                    print("    Câu trả lời chính xác")
                    engine = pyttsx3.init()
                    engine.say("Very good")
                    engine.runAndWait()
                    dem += 1  
                else:
                    print(Fore.RED + Style.BRIGHT + "    Câu trả lời sai." + Style.RESET_ALL)
                x += 1
                themcau += 1
            if a[themcau] in a:
                print(Fore.BLUE + Style.BRIGHT + "Câu 3:",a[themcau] + Style.RESET_ALL)
                print(abcd.readline())
                print(abcd.readline())
                chon = input("    Chọn đáp án của bạn: " ).upper()
                if chon == "{}".format(b[x]):
                    print("    Câu trả lời chính xác")
                    engine = pyttsx3.init()
                    engine.say("Very good")
                    engine.runAndWait()
                    dem += 1  
                else:
                    print(Fore.RED + Style.BRIGHT + "    Câu trả lời sai." + Style.RESET_ALL)
                x += 1
                themcau += 1
            if a[themcau] in a:
                print(Fore.BLUE + Style.BRIGHT + "Câu 4:",a[themcau] + Style.RESET_ALL)
                print(abcd.readline())
                print(abcd.readline())
                chon = input("    Chọn đáp án của bạn: " ).upper()
                if chon == "{}".format(b[x]):
                    print("    Câu trả lời chính xác")
                    engine = pyttsx3.init()
                    engine.say("Very good")
                    engine.runAndWait()
                    dem += 1  
                else:
                    print(Fore.RED + Style.BRIGHT + "    Câu trả lời sai." + Style.RESET_ALL)
                x += 1
                themcau += 1
            if a[themcau] in a:
                print(Fore.BLUE + Style.BRIGHT + "Câu 5:",a[themcau] + Style.RESET_ALL)
                print(abcd.readline())
                print(abcd.readline())
                chon = input("    Chọn đáp án của bạn: " ).upper()
                if chon == "{}".format(b[x]):
                    print("    Câu trả lời chính xác")
                    engine = pyttsx3.init()
                    engine.say("Very good")
                    engine.runAndWait()
                    dem += 1  
                else:
                    print(Fore.RED + Style.BRIGHT + "    Câu trả lời sai." + Style.RESET_ALL)
                x += 1
                themcau += 1
            if a[themcau] in a:
                print(Fore.BLUE + Style.BRIGHT + "Câu 6:",a[themcau] + Style.RESET_ALL)
                print(abcd.readline())
                print(abcd.readline())
                chon = input("    Chọn đáp án của bạn: " ).upper()
                if chon == "{}".format(b[x]):
                    print("    Câu trả lời chính xác")
                    engine = pyttsx3.init()
                    engine.say("Very good")
                    engine.runAndWait()
                    dem += 1  
                else:
                    print(Fore.RED + Style.BRIGHT + "    Câu trả lời sai." + Style.RESET_ALL)
                x += 1
                themcau += 1
            if a[themcau] in a:
                print(Fore.BLUE + Style.BRIGHT + "Câu 7:",a[themcau] + Style.RESET_ALL)
                print(abcd.readline())
                print(abcd.readline()) 
                chon = input("    Chọn đáp án của bạn: " ).upper()
                if chon == "{}".format(b[x]):
                    print("    Câu trả lời chính xác")
                    engine = pyttsx3.init()
                    engine.say("Very good")
                    engine.runAndWait()
                    dem += 1  
                else:
                    print(Fore.RED + Style.BRIGHT + "    Câu trả lời sai." + Style.RESET_ALL)
                x += 1
                themcau += 1
            if a[themcau] in a:
                print(Fore.BLUE + Style.BRIGHT + "Câu 8:",a[themcau] + Style.RESET_ALL)
                print(abcd.readline())
                print(abcd.readline()) 
                chon = input("    Chọn đáp án của bạn: " ).upper()
                if chon == "{}".format(b[x]):
                    print("    Câu trả lời chính xác")
                    engine = pyttsx3.init()
                    engine.say("Very good")
                    engine.runAndWait()
                    dem += 1  
                else:
                    print(Fore.RED + Style.BRIGHT + "    Câu trả lời sai." + Style.RESET_ALL) 
                x += 1 
                themcau += 1   
            if a[themcau] in a:
                print(Fore.BLUE + Style.BRIGHT + "Câu 9:",a[themcau] + Style.RESET_ALL)
                print(abcd.readline())
                print(abcd.readline())  
                chon = input("    Chọn đáp án của bạn: " ).upper()
                if chon == "{}".format(b[x]):
                    print("    Câu trả lời chính xác")
                    engine = pyttsx3.init()
                    engine.say("Very good")
                    engine.runAndWait()
                    dem += 1  
                else:
                    print(Fore.RED + Style.BRIGHT + "    Câu trả lời sai." + Style.RESET_ALL)
                x += 1
                themcau += 1
            if a[themcau] in a:
                print(Fore.BLUE + Style.BRIGHT + "Câu 10:",a[themcau] + Style.RESET_ALL)
                print(abcd.readline())
                print(abcd.readline()) 
                chon = input("    Chọn đáp án của bạn: " ).upper()
                if chon == "{}".format(b[x]):
                    print("    Câu trả lời chính xác")
                    engine = pyttsx3.init()
                    engine.say("Very good")
                    engine.runAndWait()
                    dem += 1  
                else:
                    print(Fore.RED + Style.BRIGHT + "    Câu trả lời sai." + Style.RESET_ALL)
                x += 1
                themcau += 1
            if a[themcau] in a:
                print(Fore.BLUE + Style.BRIGHT + "Câu 11:",a[themcau] + Style.RESET_ALL)
                print(abcd.readline())
                print(abcd.readline()) 
                chon = input("    Chọn đáp án của bạn: " ).upper()
                if chon == "{}".format(b[x]):
                    print("    Câu trả lời chính xác")
                    engine = pyttsx3.init()
                    engine.say("Very good")
                    engine.runAndWait()
                    dem += 1  
                else:
                    print(Fore.RED + Style.BRIGHT + "    Câu trả lời sai." + Style.RESET_ALL)
                x += 1
                themcau += 1
            if a[themcau] in a:
                print(Fore.BLUE + Style.BRIGHT + "Câu 12:",a[themcau] + Style.RESET_ALL)
                print(abcd.readline())
                print(abcd.readline()) 
                chon = input("    Chọn đáp án của bạn: " ).upper()
                if chon == "{}".format(b[x]):
                    print("    Câu trả lời chính xác")
                    engine = pyttsx3.init()
                    engine.say("Very good")
                    engine.runAndWait()
                    dem += 1  
                else:
                    print(Fore.RED + Style.BRIGHT + "    Câu trả lời sai." + Style.RESET_ALL)
                x += 1
                themcau += 1
            if a[themcau] in a:
                print(Fore.BLUE + Style.BRIGHT + "Câu 13:",a[themcau] + Style.RESET_ALL)
                print(abcd.readline())
                print(abcd.readline())
                chon = input("    Chọn đáp án của bạn: " ).upper()
                if chon == "{}".format(b[x]):
                    print("    Câu trả lời chính xác")
                    engine = pyttsx3.init()
                    engine.say("Very good")
                    engine.runAndWait()
                    dem += 1  
                else:
                    print(Fore.RED + Style.BRIGHT + "    Câu trả lời sai." + Style.RESET_ALL)
                x += 1
                themcau += 1
            if a[themcau] in a:
                print(Fore.BLUE + Style.BRIGHT + "Câu 14:",a[themcau] + Style.RESET_ALL)
                print(abcd.readline())
                print(abcd.readline()) 
                chon = input("    Chọn đáp án của bạn: " ).upper()
                if chon == "{}".format(b[x]):
                    print("    Câu trả lời chính xác")
                    engine = pyttsx3.init()
                    engine.say("Very good")
                    engine.runAndWait()
                    dem += 1  
                else:
                    print(Fore.RED + Style.BRIGHT + "Câu trả lời sai." + Style.RESET_ALL)
                x += 1
                themcau += 1
            if a[themcau] in a:
                print(Fore.BLUE + Style.BRIGHT + "Câu 15:",a[themcau] + Style.RESET_ALL)
                print(abcd.readline())
                print(abcd.readline())
                chon = input("    Chọn đáp án của bạn: " ).upper()
                if chon == "{}".format(b[x]):
                    print("    Câu trả lời chính xác")
                    engine = pyttsx3.init()
                    engine2 = pyttsx3.init()
                    engine.say("Very good")
                    engine2.say("Good Bye")
                    engine.runAndWait()
                    engine2.runAndWait()
                    dem += 1  
                else:
                    print(Fore.RED + Style.BRIGHT + "    Câu trả lời sai." + Style.RESET_ALL)
                    print(Fore.YELLOW + Style.BRIGHT + "    Tổng số điểm của bạn là:"+ Style.RESET_ALL,dem)
                    break
                x += 1
                themcau += 1
            x += 1
            themcau += 1
            print(Fore.YELLOW + Style.BRIGHT + "    Tổng số câu đúng của bạn là:"+ Style.RESET_ALL,dem)
            print("    Tổng điểm của bạn:",round((10/len(a)*dem),2))
        if dem == 15:
            print()
            print(Fore.YELLOW + Style.BRIGHT + "                Chúc Mừng Bạn Là Người Chiến Thắng"+ Style.RESET_ALL)
            print(Fore.YELLOW + Style.BRIGHT + "Bạn Đã Trả Lời Được Đúng Hết Tất Cả Các Câu Hỏi Của Chưng Trình Chúng Tôi"+ Style.RESET_ALL)
            print()
