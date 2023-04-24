import random
import threading
import emoji
import time


def very_sophisticated_neural_network_yes_yes(string):
    bank = ["Fuck me dude", "Fuck off", "fr fr ong", "Manuca sucks at chess fr"]
    return bank[random.randint(1, len(bank)-1)]

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

def random_pings():
    ping_bank = [emoji.emojize(":snowflake:"), strike("@everyone\nType: Home Defence\nFC: Haunting Deity\nTime: Now\nForming: MJ-5F9 B E A N S T A R\nDoctrine: Sleipnirs + Basis/Links\nComms: Horde Alpha\n---\nMAX FORM UNDER HD, JUST SAW 5 MILLION LESHAKS IN BEAN INTEL LETS FUCKING GO BIGGEST FIGHT OF THE YEAR LETS GOOOOOOOOOOOOOO") + "\nnvm it was two brave caracals and a slasher sorry guys"]
    while True:
        time.sleep(random.randint(1, 2**10))
        print("Haunting Deity: " + ping_bank[random.randint(1, len(ping_bank)-1)])

print("------ChatHD, Your AI-powered Personal General Advisor (technically simple logic is still intelligence so not false advertising.)------")
random_actions = threading.Thread(target=random_pings)
random_actions.start()
while True:
    string = input("You: ")
    print("Haunting Deity: " + very_sophisticated_neural_network_yes_yes(string))
