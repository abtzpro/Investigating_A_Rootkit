# BlackCatScan_Prototype

This is still very much a work in progress and has yet to be tested in a production environment. 
The scanner was whipped up as a baseline with automation on the fly while
investigating the existence of a BlackCat module within the HS environment.

This is a scanner built using python to scan for blackcat signatures within a system.

it uses a list of signatures (one per line) titled signatures.txt and outputs a txt logfile of the files found matching and their locations on the 
system as well as a good bit of details of the system and scan time etc.

this can easily be adapted to provide the scanner user the specific variant information of BlackCat installed & 
auto remediation features as well as a baseline security patch automation process following the 
initial scan function. Creating a scan and patch style script.

This could also be adapted to be used to recognize a pattern of network traffic with the known pulses and dumps of data surrounding around blackcat

using the known attack flow it could also work alongside spot analysis and APT hunting kits. 


## thanks to 

(Thanks to @rivitna2 Andrey Zhdanov for the signature list
 
Thanks to Donovan Kerns for the extended security insights into Blackat threat actor methodologies

 Thanks to Hello Security LLC for the digital footwork

) 
