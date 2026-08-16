import sys

#check for args
if len(sys.argv) >= 2:
    #command = sys.argv[1]
    #print(f"Command: {command}")
    pass
else:
    print(f"No command given.")

#a function to check commands
def check_command(arg):
    arg = sys.argv[1]
    if arg == "add":
        #call add function
    elif arg == "update":
        #call update func
    elif arg == "delete":
        #call delete
    elif arg == "mark-in-progress":
        #call mark
    elif arg == "mark-done":
        #
    elif arg == "list":
        #show list
    else:
        print(f"unknown command")