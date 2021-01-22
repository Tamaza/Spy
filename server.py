import socket
from _thread import *
import pickle
import random
from game import Game




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'localhost'
port = 6666

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(3)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0

basic_pack = ["Airpot","Bar","Cafe","Cinema","Circus","Concert Hall","Construction Site",
              "Forest","Gallery","Garage","Hospital","Office","Park","Parking",
              "Airplane","Pool","Ship","Sports Ground","Theatre","Sea"]

player_count = 2

word_array = ["You are SPY!"]
word = random.choice(basic_pack)

for _ in range(0, player_count ):
    word_array.append(word)


txt1 = random.choice(word_array)

word_array.remove(txt1)
print(word_array)

txt2 = word_array[0]

def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))


    while True:
        try:
            data = conn.recv(4096).decode()
            print(data)


            if gameId in games:
                game = games[gameId]


                if not data:
                    break
                else:


                    if data == "timer":

                        game.timer = True
                    if data == "words":


                        game.p1_card = txt1
                        game.p2_card = txt2
                    if data == "vote":
                        game.pressed = True


                    if data == "player 1 got card":
                        game.p1_got_card = True
                    if data == "player 2 got card":
                        game.p2_got_card = True



                    conn.sendall(pickle.dumps(game))

            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1


    start_new_thread(threaded_client, (conn, p, gameId))