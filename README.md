# Random IP Checker 
 
## Overview 
**Random IP Checker** is a simple Python script that generates random IP addresses and checks if they are reachable on port 80. The script continues to generate and check IP addresses until it finds one that is reachable, printing the IP address to the console. 
 
## Features 
- Generates random IPv4 addresses. 
- Excludes private and reserved IP ranges. 
- Checks the reachability of generated IP addresses on port 80. 
- Continuously runs until a reachable IP address is found. 
 
## How It Works 
1. **Random IP Generation**: The script generates a random IP address by creating four octets, each ranging from 0 to 255. It then assembles these octets into a standard IPv4 address format. 
2. **Filtering Private IPs**: Before checking the reachability, the script ensures that the generated IP is not in any reserved or private ranges \(e.g., 127.x.x.x, 10.x.x.x, 172.16.x.x - 172.31.x.x, 192.168.x.x\). 
3. **Reachability Check**: The script attempts to establish a connection to the generated IP on port 80 \(HTTP\). If the connection is successful, the IP address is printed to the console. 
4. **Looping**: The script continues this process indefinitely, generating and checking IP addresses until a valid, reachable IP is found. 
 
## Prerequisites 
- Python 3.x 
- A working internet connection 
 
## Installation 
1. **Clone the repository**: 
```bash 
git clone https://github.com/nomadsdev/darknet-sentry.git 
``` 
2. **Navigate to the project directory**: 
```bash 
cd darknet-sentry
``` 
3. **Run the script**: 
```bash 
python darknet_sentry.py 
``` 
 
## Usage 
Once the script is running, it will continuously generate random IP addresses and check their reachability on port 80. If a reachable IP is found, it will be printed to the console. 
To stop the script, simply press `Ctrl + C`. 
 
## Example Output 
```bash 
192.0.2.1 
203.0.113.5 
198.51.100.10 
``` 
These IPs are examples of what the script might output when it finds reachable addresses. 
 
## Notes 
- The script is for educational purposes and should not be used for any malicious activity. 
- Checking random IP addresses on port 80 can result in connections to unintended servers. Use this script responsibly. 

## Contributing 
Contributions are welcome! If you find any issues or have ideas for improvements, feel free to open an issue or submit a pull request. 
