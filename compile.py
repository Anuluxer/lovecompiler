import os
import zipfile

FOLDERNAME = "compile"
OUTPUTFILE = "game"

zip = zipfile.ZipFile(OUTPUTFILE + ".love", "w")
p = os.getcwd()
os.chdir(p + "\\" + FOLDERNAME)
for i in os.listdir(os.getcwd()):
    zip.write(i)
zip.close()
os.chdir(p)
print('copy /b "C:\\Program Files\\LOVE\\love.exe"+' + OUTPUTFILE + ".love" + OUTPUTFILE + ".exe")
os.system('copy /b "C:\\Program Files\\LOVE\\love.exe"+' + OUTPUTFILE + ".love " + OUTPUTFILE + ".exe")
os.remove(os.getcwd() + "\\" + OUTPUTFILE + ".love")
