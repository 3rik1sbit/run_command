import os
commands = []
commands_path = "/home/erik/Projects/python/run_command/commands"
f = open(commands_path, "r")
for line in f:
    commands.append(line)
f.close()
f = open(commands_path, "w")
f.write("")
for command in commands:
    os.system(command)
