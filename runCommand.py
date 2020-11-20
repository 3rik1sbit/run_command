import os
commands = []
f = open("commands", "r")
for line in f:
    commands.append(line)
f.close()
f = open("commands", "w")
f.write("")
for command in commands:
    os.system(command)
