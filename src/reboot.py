from mcrcon import MCRcon
import os
import time

SERVER_IP = os.environ.get('MC_Server_IP', None)                        # Server IP address
SEC_KEY = os.environ.get('MCRCON_PSWD', None)                           # Rcon password set in the 'server.properties' file
PORT = os.environ.get('MCRCON_PORT', 25575)                             # 25575 is the default RCON port for Minecraft

if SERVER_IP is None or SEC_KEY is None:
    raise Exception("Either Server IP or Rcon Password is set to None. Check your environmental variables or manually change it in the code.")

with MCRcon(SERVER_IP, SEC_KEY, PORT) as mcr:
    def start_cnt_down():
        seconds = [30,45,55]                                            # 30, 15, 10 seconds left
        for i in range(3):
            t = 60 - seconds[i]
            time.sleep(t)
            mcr.command("/say Rebooting in "+ str(t)+" seconds ...")
            
        for i in range(5,0,-1):                                         # Last 5 Seconds
            mcr.command("/say Rebooting in "+ str(i)+" seconds ...")
            time.sleep(1)

    mcr.connect()
    mcr.command("/say Scheduled Reboot in 1 minute ...")    
    start_cnt_down()
    mcr.command("/say Rebooting Now ... See you later!")
    mcr.command("/stop")
    mcr.disconnect()