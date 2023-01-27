# File-Integrity-Monitor

The goal of this project is to get a better understanding of how hash values work and their use with respects to IT. 

The target of this project is to demonstrate one of axis of CIA triad, Integrity. 

I have made a very simple integrity monitor to demonstrate a basic use of hash values and how we could leverage hash digests to monitor the integrity of our files.

## Libraries used

- hashlib
  - To grab hash digest of files
- os
  - To iterate through *nix files
- time
  - To vary the frequency of integrity checking
- datetime
  - To add timestamps to our logs
- logging 
  - To log the changes to the files


## Disclaimer

This project is intended for educational and testing purposes. Any misuse or misconfiguration of this code should not be held liable against me.
While this program can not directly affect your files, it could cause potential issues with some testing environment if other integrity monitor systems are ative. Use at your own discretion.


# Quick Demo

https://user-images.githubusercontent.com/118489496/215223851-6e5aa737-5d90-43b5-b916-45ab78c328db.mp4

# Console Output of The Log File
![Captu2re](https://user-images.githubusercontent.com/118489496/215224004-90c18758-44af-4e77-956e-21e32e7b3e86.PNG)

# Text Editor Output of The Log File
![Capture](https://user-images.githubusercontent.com/118489496/215223998-faeb03c0-53c7-4e39-84d7-8dcaec745f55.PNG)
