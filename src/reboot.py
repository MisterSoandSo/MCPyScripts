from dotenv import dotenv_values
from mcrcon import MCRcon
import time

config = dotenv_values()
SERVER_IP = config.get("SERVER_IP")                   # Server IP address
SEC_KEY = config.get("SEC_KEY")                       # Rcon password set in the 'server.properties' file
PORT = config.get("PORT")                             # 25575 is the default RCON port for Minecraft


if SERVER_IP is None or SEC_KEY is None:
    raise Exception("Either Server IP or Rcon Password is set to None. Check your environmental variables or manually change it in the code.")

with MCRcon(SERVER_IP, SEC_KEY, int(PORT)) as mcr:
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
