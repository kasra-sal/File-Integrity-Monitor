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
