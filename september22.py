#A simulation for a car game 
command = ""
started = False
while True :
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
            started = True 
            print("Car started")
    elif command == "stop":
        if not started:
         print("Car is not started")
        else:
         started = False
         print("car stopped")
    elif command == "help":
        print(''' 
stop- stop the game
start - start the game 
quit - to quit the game 
              ''')
    elif command == "quit":
        break
    else:
        print("can't understand you")