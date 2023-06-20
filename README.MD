## Hello Security LLC DIsclosure report 6/20/2023


Between the dates of 6/17/2023 and 6/20/2023 Hello Security LLC Cyber Forensic Investigator Adam Rivers (Henceforth referred to as AR) began investigating a Hello Security LLC machine used for liesurely (hobby) development, liesure activities, and streaming within the Hello Security LLC environment. 
The machine in question seemed to be exhibiting symptoms of an APT bootkit.  
Between the listed dates, AR was able to remove a bit of the attackers hold on the system via Registry via avenue of HKEY 
currentcontrolset regentries by crossreferencing what should and should not be there. The reason for doing so was an observed bootkit style activity persisting through factory resets, ISO installs, 
and upgrades in place. The infection would traverse to USB installers,
CD ROM Windows ISO installer Discs and OEM usb installers, overwriting the install medias with a custom ISO resembling that of an Enterprise ISO. (Likely To perform further escalation and lateral movement) 
The infection would persist beyond nuke and boot tactics and much more. 
It showed signs of an APT. 

This sparked AR to assume a bootkit was present on the machine and begin working under this assumption. 
Some of the attack vectors observed where kernel level access and manipulation, network (DDoS activities) and file share functions for exfiltration and data offloading of stolen files and data.
Other vectors observed where the attacker's ability to persists and reinstall the framework of the exploitkit after a fresh reset, affect the winpeshl.exe file, create services andd inject DLLs, hide their
The ability to create activities on the system, add users and administrators, network traversial and manipulation, and much more. 

at 1:43 am CST 6/20/2023 AR used firefox browser on the infected machine (installed via powershell winget install Mozilla.Firefox to be cautious) in order to navigate to
http://gmer.net to install gmer.exe. The "gmer.exe" file was zipped as "gmer.zip" and was extracted to the downloads folder, and the moved to the desktop. 
running gmer.exe from desktop prompted windows smart screen to display gmer.exe as malicious and malware with a bright red display window.
AR then navigated to https://www.virustotal.com in order to upload and scan the gmer.exe file.
Virustotal reported the following

https://www.virustotal.com/gui/file/e8a3e804a96c716a3e9b69195db6ffb0d33e2433af871e4d4e1eab3097237173/details

MD5 e9dc058440d321aa17d0600b3ca0ab04
SHA-1 539c228b6b332f5aa523e5ce358c16647d8bbe57
SHA-256 e8a3e804a96c716a3e9b69195db6ffb0d33e2433af871e4d4e1eab3097237173
Vhash 03503e0f7d1bz6!z
Authentihash 91713e1c5d76a6b42f3287bfaba68f5a3150593e1cabd9206d2d63ba37b40460
Imphash e58ab46f2a279ded0846d81bf0fa21f7
Rich PE header hash 7aeb3c862114523b64cda33696abb1be
SSDEEP 6144:wW3dQfk45aQOVusKHL7G0FJ6KbJLor/XqNjHtBfLptTksD0c2PMM40:FgkOZHvNJ6KbJE/qNBJT/h2PM
TLSH T10F8422497916FBC2EE1E26B2047B0DD11024B9E199C3617BA71DE8CE6E716C878C7633
File type Win32 EXE
executable
windows
win32
pe
peexe
Magic PE32 executable (GUI) Intel 80386, for MS Windows, UPX compressed
TrID UPX compressed Win32 Executable (39.1%)   Win32 EXE Yoda's Crypter (38.3%)   Win16 NE executable (generic) (7.2%)   Win32 Executable (generic) (6.5%)   OS/2 Executable (generic) (2.9%)
DetectItEasy PE32   Packer: UPX (3.07) [NRV,brute]   Compiler: Microsoft Visual C/C++ (2008)   Linker: Microsoft Linker (9.0) [GUI32,admin]
File size 372.00 KB (380928 bytes)
PEiD packer UPX 2.90 [LZMA] -> Markus Oberhumer, Laszlo Molnar & John Reiser
F-PROT packer UPX 

AR then crossreferenced the SHA-256 signature of the file against OTX alienvault which provided this pulse 
https://otx.alienvault.com/indicator/file/e8a3e804a96c716a3e9b69195db6ffb0d33e2433af871e4d4e1eab3097237173

Noting explicitly from Alien Labs account *Direct from AlienVault Labs* an affiliation to Noberus ransomware aka BlackCat aka ALPHV ransomware.

Distributed by the Russian Ransomware gang BlackCat, LockBit, and the Black Basta Ransomware groups as a RaaS or Ransomware as a service. (pay as you go service - this one purchased on the darkweb)

At 6:30AM CST on 6/20/2023 AR's working theory is that the underlying issues described above where caused by a threat actor whom purchased access to the BlackCat
Ransomware framework via their darkweb store and very public facing webpages boasting a factor of fostering trust as malware and ransomware developers with their userbase,
and when AR began removing certain registry keys under HKEY\currentcontrolset, the threat actor began losing a foothold within the system. The blackcat ransomware framework
resembles a bootkit in the manner it operates as described in these articles 
https://news.sophos.com/en-us/2022/07/14/blackcat-ransomware-attacks-not-merely-a-byproduct-of-bad-luck/
https://www.salvagedata.com/alphv-blackcat-ransomware/
https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/noberus-blackcat-ransomware-ttps
https://www.sentinelone.com/labs/black-basta-ransomware-attacks-deploy-custom-edr-evasion-tools-tied-to-fin7-threat-actor/
https://news.sophos.com/en-us/2022/11/30/lockbit-3-0-black-attacks-and-leaks-reveal-wormable-capabilities-and-tooling/

As such, due to BlackCat resembling a bootkit, AR attemnpted a scan with gmer.exe as mentioned from the aforementioned source. 

Continuing with AR's working theory, 
This became the threat actor's new access vector to ensure persistence and access to the threat actor's backdoor on the Hello Security LLC machine.
("The attacker noted a loss of functionality and wanted to ensure they did not lose a foothold in the system thus the avenue of infection became gmer.exe" ` AR)

## IOC present on the machine

As IOC, the network traffic noted in both OTX and VirusTotal for the gmer.exe BlackCat Ransomware framework have been observed on the infected machine via NIDS logs for at least 3-4 weeks.
There are at least 75% of the files mentioned in each article above present on the machine, a custom built Asus MOBO, AMD CPU based machine running windows 10 home x64 official activated.
There is evident observation of the actions and activity of a user on the machine by the threat actor in the form of audio, visual, and text input logging. There are abuses of a meta redirect to 
direct a user no matter the browser used, to a malicious URL used for logging the users login credentials. (Unconfirmed but assuming the network traffic for this malicious login page matches IOC of BlackCat)

The framework seems to be part of a bigger framework that can also target android OS and iOS devices including the newest released iphone 14 pro. The same symptoms can be witnessed across devices as if
they where settings synced for an official service of microsoft device to device. There is also the possibility a larger framework would not be required as the blackcat framework is written in RUST
and can be deployed on quite a large variety of devices, thus with a few modifications, could easily be made to work for both. BlackCat encapsulates a few RAT (remote access terminals to ensure
the threatactor can interact with the infected devices in a direct and immediate manner in reaction to or retaliation to removal attempts and attempts to investigate the framework.

However blackcat is indeed a RaaS which can be purchased from their darkweb link 
(To Be Updated)
