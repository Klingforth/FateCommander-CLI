import shlex, os, sys, subprocess, shutil 

ROOT = os.path.dirname(os.path.abspath(__file__))
currentPath = ROOT
copyFile = None
copyName = None

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def title():
    print("""
                                                                                     
         ███████╗ █████╗ ████████╗███████╗                                          
         ██╔════╝██╔══██╗╚══██╔══╝██╔════╝                                           
         █████╗  ███████║   ██║   █████╗                                             
         ██╔══╝  ██╔══██║   ██║   ██╔══╝                                             
         ██║     ██║  ██║   ██║   ███████╗                                           
         ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚══════╝      
                                                                       Powered by: Patrick Klingforth                                                                                                 
                   ██████╗ ██████╗ ███╗   ███╗███╗   ███╗ █████╗ ███╗   ██╗██████╗   
                  ██╔════╝██╔═══██╗████╗ ████║████╗ ████║██╔══██╗████╗  ██║██╔══██╗ 
                  ██║     ██║   ██║██╔████╔██║██╔████╔██║███████║██╔██╗ ██║██║  ██║  
                  ██║     ██║   ██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██║╚██╗██║██║  ██║  
                  ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║██████╔╝  
                   ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝""")                              
    
def info():
    clear()
    title()

    print("")
    print("__________________________________________________________")
    print("INFO          Zeigt alle Befehle an")
    print("GO            Wechsle in Unterordner")
    print("BACK          Gehe einen Ordner zurück")
    print("MAKE          Erstellt einen neuen Ordner")
    print("RENAME        Ändert den name eines Ordners")
    print("DEL           Löscht den angegebenen Ordner oder Datei")
    print("COPY/PAST     Kopiert ein verzeichniss mit unterverzeichnissen")
    print("CS            Zeige Zwischenspeicher")
    print("LS            Zeige Verzeichniss")
    print("  -o            Zeigt nur Ordner an")
    print("  -d            Zeigt nur Datein an")
    print("  -a            Zeigt nur Datein und unterordner an")
    print("START         Öffne Datei mit Standardprogramm")
    print("EXIT          Beendet das Tool")
    print("__________________________________________________________")

def entrydir(*args): 
    # Ohne Rich Table werden die Einträge einfach untereinander aufgelistet
    for entry in os.listdir(currentPath):
        fullPath = os.path.join(currentPath, entry)
        if not args:
            print(entry)
        elif args[0] == "-d":
            if os.path.isfile(os.path.join(currentPath, entry)):
                print(entry)
        elif args[0] == "-o":
            if os.path.isdir(fullPath):
                print(entry)
        elif args[0] == "-a":
            if os.path.isdir(fullPath):
                print(f"[DIR] {entry}")
                goTo(entry)
                for en in os.listdir(currentPath):
                    UnderPath = os.path.join(currentPath, en)
                    if os.path.isdir(UnderPath):
                        print(f"  +{en}")
                    if os.path.isfile(UnderPath):
                        print(f"  -{en}")
                goBack()

def goTo(Path):
    global currentPath
    newPath = os.path.join(currentPath, Path)
    if os.path.isdir(newPath):
        currentPath = os.path.abspath(newPath)
    else:
        print(newPath)

def goBack(seitLimit=1):
    global currentPath
    for _ in range(int(seitLimit)):
        currentPath = os.path.abspath(os.path.join(currentPath, ".."))

def goHome():
    global currentPath
    currentPath = ROOT
    clear()
    title()

def copy(File):
    global currentPath
    global copyFile
    global copyName
    copyFile = os.path.join(currentPath, File)
    copyName = File
    print(f"{File} wurde in den Zwischenspeicher gespeichert")

def past():
    global currentPath
    global copyFile
    global copyName
    shutil.copytree(copyFile, currentPath, dirs_exist_ok=True)
    print(f"{copyName} wurde in das Aktuelle verzeichniss kopiert")
    
def showCache():
    global copyFile
    if copyFile == None:
        print("Es befindet sich nichts im Zwischenspeicher")
    else:
        print(f"{copyName}")
        print(f"{copyFile}")

def pyStart(programm, file):
    filePath = os.path.join(currentPath,file)
    subprocess.run([programm, filePath])

def reName(file, newFile):
    global currentPath
    reFile = os.path.join(currentPath, file)
    reNewFile = os.path.join(currentPath, newFile)
    os.renames(reFile, reNewFile)
    print(f"Old: {file} New: {reNewFile}")

def makeNew(file):
    global currentPath
    newFile = os.path.join(currentPath,file)
    os.makedirs(newFile)

def fileDelete(file):
    global currentPath
    delFile = os.path.join(currentPath, file)
    ask = input(f"Willst du Die angegebene Datei {file} wirklich löschen? Y/N  ")
    match ask:
        case "Y" | "y" | "ja" | "Ja" | "yes" | "Yes":
            os.removedirs(delFile)
            print(f"{file} wurde gelöscht")
        case "N" | "n" | "nein" | "Nein" | "no" | "No":
            print("Löschen wurde abgebrochen")
        case _:
            print("Löschen wurde abgebrochen")

clear()
def main():
    title()

    while True:
        # Ersetzt Panel-Input durch Standard-Input
        cmd = input(f"{currentPath}> ")
        tokens = shlex.split(cmd)

        if not tokens:
            print("Unbekannter Befehl")
            print("'info' für mehr Informationen")
            continue

        command = tokens[0]
        args = tokens[1:]

        match command:
            case "exit":
                sys.exit(0)
            case "go":
                if len(args) == 0:
                    print("Bitte Ordner wählen")
                    continue
                else:
                    goTo(args[0])
            case "back":
                if args:
                    goBack(args[0])
                else:
                    goBack()
            case "home":
                goHome()
            case "start":
                pyStart(args[0],args[1])
            case "rename":
                reName(args[0], args[1])
            case "make":
                makeNew(args[0])
            case "del":
                fileDelete(args[0])
            case "ls":
                if len(args) == 0:
                    entrydir()
                else:
                    entrydir(args[0])
            case "copy":
                copy(args[0])
            case "past":
                past()
            case "sc":
                showCache()
            case "info":
                info()
            case _:
                print(f"Unbekannter Befehl:{command}")
                print("'info' für mehr Informationen")
    clear()

if __name__ == "__main__":
    main()