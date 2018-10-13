from os import listdir, remove
from os.path import isfile, join
from time import sleep, time

time1 = time()

mypath = 'C:/Users/hidan/Downloads'
ext = ['.torrent', '.exe', '.msi']
cont = 0
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for file in onlyfiles:
    if file.endswith(tuple(ext)):
        print(file)
        cont = cont+1
        remove(mypath+'/'+file)


time2 = time()

print("Tempo de execução: "+str(time2 - time1))
print(str(len(onlyfiles)) + " arquivos encontrados")
print(str(cont) + " arquivos excluidos com as extensões escolhidas")
print("Encenrrando...")
sleep(5)