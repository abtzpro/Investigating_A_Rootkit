## Hello Security LLC DIsclosure report 6/20/2023


Between the dates of 6/17/2023 and 6/20/2023 Hello Security LLC Cyber Forensic Investigator Adam Rivers (Henceforth referred to as AR) began investigating a Hello Security LLC machine used for liesurely (hobby) development, liesure activities, and streaming within the Hello Security LLC environment. 
The machine in question seemed to be exhibiting symptoms of an APT bootkit.  
Between the listed dates, AR was able to remove a bit of the attackers hold on the system via Registry via avenue of HKEY 
currentcontrolset reg entries by cross-referencing what should and should not be there manually entry by entry. The reason for doing so was an observed bootkit style activity persisting through factory resets, ISO installs, 
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

- https://news.sophos.com/en-us/2022/07/14/blackcat-ransomware-attacks-not-merely-a-byproduct-of-bad-luck/

- https://www.salvagedata.com/alphv-blackcat-ransomware/

- https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/noberus-blackcat-ransomware-ttps

- https://www.sentinelone.com/labs/black-basta-ransomware-attacks-deploy-custom-edr-evasion-tools-tied-to-fin7-threat-actor/

- https://news.sophos.com/en-us/2022/11/30/lockbit-3-0-black-attacks-and-leaks-reveal-wormable-capabilities-and-tooling/

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
and can be deployed on quite a large variety of devices, thus with a few modifications, could easily be made to work for both. BlackCat encapsulates a few RAT (remote access terminals) to ensure
the threatactor can interact with the infected devices in a direct and immediate manner in reaction to or retaliation to removal attempts and attempts to investigate the framework.

However blackcat is indeed a RaaS which can be purchased from their darkweb link 
(To Be Updated)


## Notes

The IOC has been cross referenced against VirusTotal, OTX, Sophos Security, and MITRE DB.

It seems to explicitely deliver further payloads andd malware when downloading repair and analysis software from well known sources such as bleeping computer, microsoft, and gmer.net

A common vector used in the past by a threat actor to deploy BlackCat ransomware/malware framework consists of an unsecured VPN and Firewall flaw. (AR began seeing symptoms on the machine
with Firewalla Gold box and Nord VPN in use for this liesure machine and environment setup) 
"This should emphasize the need to harden & patch a machine against as many publicly listed CVE's and vulnerabilities as possible. This was an old 2018 Vulnerability abused in the VPN & firewall killchain. " ~ AR 

threat actor abuses this path on the machine C:\ProgramData\Packages with the following packages within that path
Microsoft.549981C3F5F10_8wekyb3d8bbwe
Microsoft.DesktopAppInstaller_8wekyb3d8bbwe
Microsoft.Windows.Photos_8wekyb3d8bbwe
NVIDIACorp.NVIDIAControlPanel_56jybvy8sckqj
SpotifyAB.SpotifyMusic_zpdnekdrzrea0

Threat actor abuses this registry location to prevent network stack resets and keep persistence. The blackcat framework relies heavily on the local network for traversial
Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Nsi
on each reboot the "Everyone" role as well as the current user account will be denied access to this registry entry. If a startup script is scheduled a s a scheduled task to give the current user account
permissions over this key as the current user logs on or at boot time, the ransomware/malware framework will cause a bootlop in which the winpeshl.exe file is abused to reiterate a hold over the machine
the blackcat framework also creates new COM objects andd begins a new iteration of its install steps after each action performed by the attacker.

## More IOC

https://bleepingcomputer.com > download "hijackthis.exe" 
- for checking startup files, hijacked DLLs etc 

> scan it against VirusTotal > Get these results
https://www.virustotal.com/gui/file/9da5a899b9d55e1d43718ec0ad6368f9e9ef0242a4e88cd5ddb2cc6d7bfa5fb3
OTX has a single pulse listing the SHA-256 signature of hijackthis.exe as well listed as: UPX (like BlackCat)
https://otx.alienvault.com/indicator/file/9da5a899b9d55e1d43718ec0ad6368f9e9ef0242a4e88cd5ddb2cc6d7bfa5fb3 

- hijack this was downloaded as a means of troubleshooting the existing exhibited bootkit symptoms to determine if their was a Hijacker in place.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

https://bleepingcomputer.com > download "rkill.exe" 
- for killing malware associated processes and rogue processes in an attempt to free up a locked process preventing removal of a file.

> Scan "rkill.exe" against VirusTotal > get these results >
https://www.virustotal.com/gui/file/d4ac5b3c525a5fd94019d80ff81b552e73b19b1bd0a554b9609cdd5e1b00955a
checking the SHA-256 signature of "rkill.exe" against OTX gives these results
https://otx.alienvault.com/indicator/file/d4ac5b3c525a5fd94019d80ff81b552e73b19b1bd0a554b9609cdd5e1b00955a
OTX lists it as an IOC for QakBot, a delivery and deployment methodology of BlackCat aka Noberus, aka ALPHV Ransomware framework.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Downloading "Loki" (to be used as an APT hunting framework assistant) from the official github source > Scanning the resultant Loki.zip file against VirusTotal > get these results
https://www.virustotal.com/gui/file/32d340d982b91616bd966da8a5807d4eac7febb1d0e87da1acee7cd8c9d295ae
OTX has no listing for the SHA-256hash of the Loki zip. (this could potentially be a false positive but Zenbox sandbox flagged it as MALWARE RANSOM TROJAN EVADER RAT)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Downloading "GrantPerms64" from https://bleepingcomputer.com official site 
- used for giving and taking permissions on files in the hopes of freeing up some file access issues

Scan the resultant GrantPerms64.zip against VirusTotal > Get these results >
https://www.virustotal.com/gui/file/662e5f8ca897ef38ba6d7bd65c298795949abfa7990482826cd4186052d8ec44
listed as a Trojan.Malware.300983.susgen by Acronis (Static ML)
OTX had no listing for the SHA-256 signature of "GrantPerms64.zip"

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

C:\Users\REDACTED\Cookies\ESE\container.dat (android-cts-7.1_r6-linux_x86-arm.zip)
VT scan results >
https://www.virustotal.com/gui/file/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
The sandbox C2AE flags this file as: STEALER
The sandbox ReaQta-Hive flags this file as: MALWARE
OTX of the SHA-256 signature provided by VT scan shows these results
https://otx.alienvault.com/indicator/file/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
Marked as  honeypot , telnet , cowrie , ssh

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

C:\ProgramData\Packages\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe\REDACTED\SystemAppData\Helium\cache contains a5e24e12fd376cc9.dat, a5e24e12fd376cc9_COM15.dat, a5e24e12fd376cc9_COM15.dat.LOG1, and 
a5e24e12fd376cc9_COM15.dat.LOG2. Checking basic google search shows mention of the path for an app called Desktop Bridge https://stackoverflow.com/questions/65849063/after-the-desktop-bridge-app-is-uninstalled-programdata-packages-appname-stil and here https://learn.microsoft.com/en-us/answers/questions/241923/after-the-desktop-bridge-app-is-uninstalled-progra
Following the attack flow of Blackcat by abusing a valid app or service to further the attacker's privilige and hold over the infected machine.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

C:\ProgramData\NVIDIA Corporation\Drs\nvdrswr.lk (android-cts-7.1_r6-linux_x86-arm.zip)
nvdrswr.lk scanned against VT gives these results
https://www.virustotal.com/gui/file/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
The sandbox C2AE flags this file as: STEALER
The sandbox ReaQta-Hive flags this file as: MALWARE

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

checking nvdrswr.lk aginst OTX gives these results
https://otx.alienvault.com/indicator/file/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
Listed as a honeypot, telnet, cowrie, and ssh
(ensure you read the comments specifically one posted by user TELEMACH1)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

C:\ProgramData\NVIDIA\NGX\models\dlss\versions\131357\files\160_B9F5618.bin "160_B9F5618.bin" (CL 29016210)
scanned against VT >
https://www.virustotal.com/gui/file/cb195979de6ab5cdf1d54e03326aa5006279ce6fa8642bcce3f23a7db7c20444
listed as matching a Yara rule INDICATOR_KB_CERT_62e745e92165213c971f5c490aea12a5 
Ruleset: indicator_knownbad_certs
https://github.com/ditekshen/detection - Detects executables signed with stolen, revoked or invalid certificates
(flagged for bad certificates)
OTX had no listing for the SHA-256 signature cb195979de6ab5cdf1d54e03326aa5006279ce6fa8642bcce3f23a7db7c20444

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

C:\ProgramData\NVIDIA\NGX\models\dlss\versions\131356\files\160_F7361DC.bin "160_F7361DC.bin" (CL 29016210)
VT report >
https://www.virustotal.com/gui/file/3afadd4778f94bfbbc10dceb91173299faaabe01feaca3aeb1a16b50b9aa1a1b
Matches rule INDICATOR_KB_CERT_62e745e92165213c971f5c490aea12a5 by ditekSHen from ruleset indicator_knownbad_certs at https://github.com/ditekshen/detection Detects executables signed with stolen, 
revoked or invalid certificates 
Matches rule User with Privileges Logon by frack113 at Sigma Integrated Rule Set (GitHub) Detects logon with "Special groups" and "Special Privileges" can be thought of as Administrator groups or privileges. 
OTX had no listing for SHA-256 signature 3afadd4778f94bfbbc10dceb91173299faaabe01feaca3aeb1a16b50b9aa1a1b

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
