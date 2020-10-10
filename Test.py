import requests

url = "https://www.fgnwct.com/getNps?showAll=false&search=&order=asc"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
    "Content-Type": "application/json",
    "Cookie": "userSession=liuyunhong@chengtay.com&&0UMtibgYeX2LZZ+u1xPmhA==; JSESSIONID=9855AC579D9CE9FB81FB5FC9BD21E331; Hm_lvt_e7a29f62e903f02ca46b3f22641eb1cd=1602295240,1602296238; Hm_lpvt_e7a29f62e903f02ca46b3f22641eb1cd=1602299161"
}
response = requests.get(url=url, headers=headers)
response.encoding = "utf-8"
result = response.json()[0].get('start').replace('npc.exe', './npc')
with open('C:\\Users\\shaojunshuai\\Desktop\\RecordedScript.vbs', 'w', encoding='utf-8') as f:
    f.writelines('#$language = "VBScript"\n')
    f.writelines('#$interface = "1.0"\n')
    f.writelines('crt.Screen.Synchronous = True\n')
    f.writelines('\' This automatically generated script may need to be\n')
    f.writelines('\' edited in order to work correctly.\n')
    f.writelines('Sub Main\n')
    f.writelines('crt.Screen.Send "cd /mnt/fgnwct/linux_amd64_client" & chr(13)\n')
    f.writelines('crt.Screen.WaitForString "[user@abs01 linux_amd64_client]$"\n')
    f.writelines('crt.Screen.Send"'+result+'"& chr(13)\n')
    f.writelines('End Sub')
    f.close()