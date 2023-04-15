# MCPyScripts
Python Scripts to manage a MC Server with mcrcon.
This is an automation project that uses [mcrcon](https://pypi.org/project/mcrcon/) to allow server administrators to remotely execute Minecraft commands. This was made in mind to handle vanilla and modded servers without having to add extra mods or plugins.  Included in the project are: auto_reboot scripts for both windows and unix servers, countdown reboot scripts and other scripts later on.


## Getting Started
To get started, you would need to enable RCON on your server. You would need to secure it to prevent unauthorized access to your server.
1. Access your server files: `server.properties` and locate `enable-rcon` section and change the value to `true`.
2. Restart server to enable RCON on your server.
3. Find the `rcon.port` line and change the port number to an available port. 25575 is usually the default port number.
4. For the `rcon.password` line change the password of your choice. Make sure to keep this secret!
5. Save the server file and restart your server.
6. On this repository, find the file `.env` in the `src` folder to add in values of`rcon.port` and `rcon.password` to `PORT` and `SEC_KEY`.


## Requirements
- `mcrcon <https://pypi.org/project/mcrcon/>`_
- `python-dotenv <https://pypi.org/project/python-dotenv/>`_


Using ``pip install -r requirements.txt`` should cover everything.


## License
This project is licensed under the GNU v3 License.
