CMD_LIST_DEFINE = {
    "echo|say|repeat|print" : "echo's what you put in",
    "exit|close|finish|goHome" : "exits the shell, put any number after for the exit code",
    "mkdir|make_directory|mkpath" : "makes a directory of the name you enter in",
    "touch|make_file|filecreate|FCRET" : "makes a file of the name you enter in, dont forget the file extension",
    "help|pleaseHelp|stuck|h|MCSH_HELP" : "brings you to this screen",
    "ls|list|dir" : "List the Dir"
}

CMD_LIST_DEFINE_NONDICT = "if you enter a command thats not in this library then it will run as a bash command\n\necho|say|repeat|print : echo's what you put in\nexit|close|finish|goHome : exits the shell, put any number after for the exit code\nmkdir|make_directory|mkpath : makes a directory of the name you enter in\ntouch|make_file|filecreate|FCRET : makes a file of the name you enter in, dont forget the file extension\nhelp|pleaseHelp|stuck|h|MCSH_HELP : brings you to this screen\nls|dir|list : brings up whats in that directory\ncd|ChangeDir : Changes the Directory that MCSH is in\n"

echo = {
    "echo",
    "say",
    "repeat",
    "print"
}

exit = {
    "exit",
    "close",
    "finish",
    "goHome",
    "e"
}

mkdir = {
    "mkdir",
    "make_directory",
    "mkpath"
}

touch = {
    "touch",
    "make_file"
    "filecreate",
    "FCRET"
}

help = {
    "help",
    "pleaseHelp",
    "stuck",
    "h",
    "MCSH_HELP"
}

ls = {
    "ls",
    "dir"
    "list"
}

cd = {
    "cd",
    "ChangeDir"
}

clear = {
    "cls",
    "clear"
}
