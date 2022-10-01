import sys,os,time
import CMD_LIST

from rich.console import Console

console = Console()
ranGood = False

bashCmdRanGood = 0

MCSH_VER = "0.1.7"

def main():
    global bashCmdRanGood
    while True:
        ranGood = False
        
        print("\n")
        if bashCmdRanGood != 0:
            command = str(console.input("[red b i reverse] "+os.getcwd()+" [/] >"))
        else:
            command = str(console.input("[green b i reverse] "+os.getcwd()+" [/] >"))

        bashCmdRanGood = 0

        for terms in CMD_LIST.echo:
            if command.split(" ")[0] == terms:
                print(command.split(" ")[1])
                ranGood = True
                pass
            pass
        pass
        
        for terms in CMD_LIST.exit:
            if command.split(" ")[0] == terms:
                try:
                    sys.exit(command.split(" ")[1])
                    anGood = True
                except IndexError:
                    sys.exit()
                    ranGood = True
                except Exception as e:
                    print("an unknown error as occurs\n\n\n",e)
                pass
            pass


        for terms in CMD_LIST.mkdir:
            if command.split(" ")[0] == terms:
                dirname = command.split(" ")[1]
                dirname = "mkdir " + dirname
                os.system(dirname)
                ranGood = True
                pass
            pass
        pass

        for terms in CMD_LIST.touch:
            if command.split(" ")[0] == terms:
                filename = command.split(" ")[1]
                filename = "touch " + filename
                os.system(filename)
                ranGood = True
                pass
            pass

        for terms in CMD_LIST.help:
            if command.split(" ")[0] == terms:
                print(CMD_LIST.CMD_LIST_DEFINE_NONDICT)
                ranGood = True
                pass
            pass
        
        for terms in CMD_LIST.ls:
            if command.split(" ")[0] == terms:
                os.system("ls")
                ranGood = True
        
        for terms in CMD_LIST.cd:
            if command.split(" ")[0] == terms:
                try:
                    print(command.split(" ")[1])
                    os.chdir(command.split(" ")[1])
                    ranGood = True
                except:
                    print("Current Directory:")
                    os.system("pwd")
                    ranGood = True
        
        for terms in CMD_LIST.clear:
            if command.split(" ")[0] == terms:
                os.system("clear")
                ranGood = True
        
        if command.split(" ")[0] == "b":
            os.system(command.split(" ")[1])
            ranGood = True
        
        if ranGood == False:
            bashCmdRanGood = os.system(command)
            ranGood = True
        
        if bashCmdRanGood != 0:
            console.print("[blink bold white on red i]Invalid Command[/]: " + command, style="bold white on blue")

        




    pass

if __name__ == '__main__':
    console.print("NaRSH (Not a Real Shell), built on top of BASH\nVersion: ",MCSH_VER, style="bold white on blue", justify="center")
    main()
