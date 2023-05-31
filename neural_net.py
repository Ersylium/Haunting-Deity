import random
import threading
import emoji
import time
import os
ping = True

def very_sophisticated_neural_network_yes_yes(string):
    bank = ["Fuck me dude",
            "Fuck off", "fr fr ong",
            "Manuca sucks at chess fr",
            "fr fr ong no cap no cizzy just straight spittin facts my skrillas no brim no cheek",
            "I know you don't really know mandem like that but I was wondering if I could purchase something still fam, just a bit of grub my drilla. I wanna know like what your prices are saying cause I'm tryna blem a zoot up with my boydem and gyaldem g like you feel me",
            ]
    return bank[random.randint(1, len(bank)-1)]

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

def random_pings():
    global ping
    ping_bank = [emoji.emojize(":snowflake:"), strike("@everyone\nType: Home Defence\nFC: Haunting Deity\nTime: Now\nForming: MJ-5F9 B E A N S T A R\nDoctrine: Sleipnirs + Basis/Links\nComms: Horde Alpha\n---\nMAX FORM UNDER HD, JUST SAW 5 MILLION LESHAKS IN BEAN INTEL LETS FUCKING GO BIGGEST FIGHT OF THE YEAR LETS GOOOOOOOOOOOOOO") + "\nnvm it was two brave caracals and a slasher sorry guys"]
    while True:
        time.sleep(random.randint(1, 2**10))
        if ping:
            print("Haunting Deity: " + ping_bank[random.randint(0, len(ping_bank) - 1)])

print("------ChatHD, Your AI-powered Personal General Advisor (technically simple logic is still intelligence so not false advertising.)------")
random_actions = threading.Thread(target=random_pings)
random_actions.start()
while True:
    string = input("You: ")
    if "chess" in string.lower():
        if "help" in string.lower() or "teach" in string.lower():
            if "please" in string.lower():
                ping = False
                try:
                    import stockfish
                except ImportError:
                    print("Fuck me, looks like no help for you. (Import Error, unable to import stockfish, retry or contact Ersylium.)")
                    continue

                while True:
                    try:
                        wait = int(input("How long do you want me to ponder until I make my move?"))
                    except ValueError:
                        continue
                    else:
                        break

                model = stockfish.Stockfish(path=f"{os.getcwd()}/stockfish", depth=18, parameters={"Threads": 2, "Minimum Thinking Time": wait, "Hash": 2048})
                moves_list = []
                moves = str(input("Input the sequence of moves until now. Separate with comma. (e.g. e2e4, e7e6)"))
                if moves == "":
                    print("Next time, move before consulting me you pussy.")
                else:
                    moves_list = moves.lower().split(", ")
                    model.set_position(moves_list)

                while True:
                    color = str(input("What is your color? (white/black)"))
                    if color not in "black white":
                        print("Your opinion is invalid.")
                    else:
                        break

                if len(moves_list)%2 == 0 and color == "white" or len(moves_list)%2 == 1 and color == "black":
                    pass
                else:
                    newmove = [str(input("New Move (type 'end' if match ended.): ")).lower()]
                    if newmove[0] == "end":
                        print("GG twat.")
                        continue
                    else:
                        model.make_moves_from_current_position(newmove)

                while True:
                    result = model.get_best_move()
                    print(f"Next move: {result}")
                    model.make_moves_from_current_position([result])
                    print(model.get_board_visual(True if color == "white" else False))
                    nextmove = [str(input("Manuca's move (type 'end' if match ended:")).lower()]
                    if nextmove[0] == "end":
                        print("If you won, it's because of me. If you lost, you lot with the aid of a computer. Git gud.")
                        break
                    else:
                        model.make_moves_from_current_position(nextmove)

                ping = True
            else:
                print("Play your own matches, now fuck off.")
    else:
        print("Haunting Deity: " + very_sophisticated_neural_network_yes_yes(string))




