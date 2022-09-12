import sys,os,time
import CMD_LIST

MCSH_VER = "0.1.2"


def main():
    while True:
        command = str(input("MCSH >"))
        for terms in CMD_LIST.echo:
            if command.split(" ")[0] == terms:
                print(command.split(" ")[1])
                pass
            pass
        pass
        
        for terms in CMD_LIST.exit:
            if command.split(" ")[0] == terms:
                try:
                    sys.exit(command.split(" ")[1])
                except IndexError:
                    sys.exit()
                except Exception as e:
                    print("an unknown error as occurs\n\n\n",e)
                pass
            pass

        for terms in CMD_LIST.mkdir:
            if command.split(" ")[0] == terms:
                dirname = command.split(" ")[1]
                dirname = "mkdir " + dirname
                os.system(dirname)
                pass
            pass
        pass

        for terms in CMD_LIST.touch:
            if command.split(" ")[0] == terms:
                filename = command.split(" ")[1]
                filename = "touch " + filename
                os.system(filename)
                pass
            pass
        for terms in CMD_LIST.help:
            if command.split(" ")[0] == terms:
                print(CMD_LIST.CMD_LIST_DEFINE_NONDICT)
                pass

    pass

if __name__ == '__main__':
    print("MessyCode Shell (C) 2022 9/9/22\nVersion: ",MCSH_VER)
    main()