import win32com.client as client, time
time.sleep(2)
wsh = client.Dispatch('WScript.Shell')
wsh.AppActivate("gta_sa.exe")
while True:
    wsh.SendKeys('w')
    time.sleep(.1)
