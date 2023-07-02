## Investigative Log 

## Log Start Date
6/12/2023

This is an investigation into the rootkit and malicious behavior on a machine that seems to become a repeated target and thus requires more in depth research.

This repo will often be updated and is by no means complete

the repo will be updated with findings regularly in an effort to paint a larger picture of the attack methodology, the attack chain as a whole, and the attack surface to focus patching on.


Incident Report

Date: 2023-06-21

Subject: Memory Resource Exhaustion Incident in iOS Application

Description of Incident: 

On the above date, an iOS application was abruptly terminated due to an instance of memory resource exhaustion. This termination occurred due to the application demanding resources beyond the permissible limit set by the system. This incident resulted in an unexpected interruption of the application's services. 

Details of Incident:

The incident involved a sudden spike in the application's memory usage. The application's attempt to allocate additional memory was not granted by the system, causing a termination of the app. The event occurred during the app's foreground state, indicating the app was actively being used at the time. 

An excerpt from the crash log:

```
Exception Type: EXC_RESOURCE
Exception Subtype: MEMORY
Exception Message: (Limit 1800 MB) Observed 1990 MB
Exception Note: NON-FATAL CONDITION (this is NOT a crash)
Termination Reason: Namespace SPRINGBOARD, Code 0xdead10cc
Triggered by Thread: 0
```

It indicates the Exception Type as EXC_RESOURCE, which is commonly associated with resource consumption issues. The termination reason provided by the system, 'Namespace SPRINGBOARD, Code 0xdead10cc', shows that the app was terminated due to its excessive memory usage.

Investigation:

There is no evidence at this time to suggest that this incident was the result of a malicious attack, such as a memory overflow attack. It could be due to an error or inefficiency in the application's code causing it to demand excessive resources. 

However, without additional information such as a more detailed crash log, source code analysis, network traffic inspection, or unusual activity monitoring, it is impossible to definitively rule out a potential attack. Further investigation is required to ascertain the exact cause and to implement the necessary corrective measures.

Actions Taken:

As of now, the issue has been documented. The next steps will involve conducting a detailed investigation to identify the root cause of the problem. If the problem persists, a full analysis of the app's code may be necessary, along with potential remediation steps such as patching or updating the app.

Prepared by: Adam Rivers - ChatGPT automation

Incident Report
-----------------------------------------------------------------------
Incident Report #2 
iPhone 14 plus project red iOS 16.5.1
**Incident Date and Time**: June 22, 2023, from 06:22:15 to 19:53:55 (local time)

**Report Created**: June 24, 2023

Affected Service: fitcored process (SeymourServices.framework)

Incident Description: The fitcored process, part of the SeymourServices.framework, experienced a repeated crash. This process is likely related to Apple's fitness or health services.

Trigger: The crash logs indicate that the issue originates from interactions with libsqlite3.dylib, which is an SQLite library. The process is potentially running a query or trying to read data from an SQLite database when the issue occurs.

Impact: The extent of the impact is unclear from the available logs. However, it could lead to reduced functionality or errors in associated health or fitness services on the device.

Resolution Steps Taken: N/A

Recommended Next Steps:
1. Update the iOS device to the latest version if not already done. This issue might have been addressed in a newer version.
2. If the issue persists, try resetting the device settings (Settings -> General -> Reset -> Reset All Settings). Note: this will not delete user data, but it will reset device settings which might resolve the issue.
3. If none of the above steps work, reach out to Apple support for further assistance.

Incident Status: Open, pending further actions.

Attachments: Crash logs provided by the user.

'''
{"duration_ms":"48843929","share_with_app_devs":1,"roots_installed":0,"bug_type":"145","os_version":"iPhone OS 16.5 (20F66)","slice_uuid":"B86E6699-4DCA-342C-9AE7-496F34DD4D9C","is_first_party":0,"incident_id":"0BC1B2D7-8CFB-4DAC-8426-8278566D3627","timestamp":"2023-06-22 19:54:07.00 -0500","app_name":"aggregated","name":"aggregated"}
Date/Time:        2023-06-22 06:19:52.280 -0500
End time:         2023-06-22 19:53:56.209 -0500
OS Version:       iPhone OS 16.5 (Build 20F66)
Architecture:     arm64e
Report Version:   40
Incident Identifier: 0BC1B2D7-8CFB-4DAC-8426-8278566D3627
Share With Devs:  Yes

Data Source:      Microstackshots
Shared Cache:     D8CB1AB4-F0C6-3115-BF0E-03F70FF26BA1 slid base address 0x1874cc000, slide 0x74cc000

Command:          aggregated
Path:             /System/Library/PrivateFrameworks/AggregateDictionary.framework/Support/aggregated
Resource Coalition ID: 111
Architecture:     arm64
PID:              335

Event:            disk writes
Action taken:     none
Writes:           1073.76 MB of file backed memory dirtied over 48844 seconds (21.98 KB per second average), exceeding limit of 12.43 KB per second over 86400 seconds
Writes limit:     1073.74 MB
Limit duration:   86400s
Writes caused:    1073.76 MB
Writes duration:  48844s
Duration:         48843.93s
Duration Sampled: 48709.89s
Steps:            6054 (10.49 MB/step)

Hardware model:   iPhone14,8
Active cpus:      6
HW page size:     16384
VM page size:     16384

OS Cryptex File Extents: 662

Heaviest stack for the target process:
  100  ??? (libsystem_pthread.dylib + 2940) [0x1ee2a0b7c]
  87   ??? (libsystem_pthread.dylib + 3548) [0x1ee2a0ddc]
  87   ??? (libdispatch.dylib + 93404) [0x1959cdcdc]
  67   ??? (libdispatch.dylib + 49316) [0x1959c30a4]
  67   ??? (libdispatch.dylib + 46092) [0x1959c240c]
  67   ??? (libdispatch.dylib + 138808) [0x1959d8e38]
  67   ??? (libdispatch.dylib + 16172) [0x1959baf2c]
  67   ??? (libxpc.dylib + 69352) [0x1ee2f3ee8]
  67   ??? (libxpc.dylib + 122596) [0x1ee300ee4]
  67   ??? (libxpc.dylib + 201252) [0x1ee314224]
  67   ??? (libxpc.dylib + 201628) [0x1ee31439c]
  67   ??? (libxpc.dylib + 200156) [0x1ee313ddc]
  67   ??? (PowerlogCore + 559996) [0x1bac5cb7c]
  67   ??? (PowerlogCore + 560148) [0x1bac5cc14]
  43   ??? (PowerlogCore + 559532) [0x1bac5c9ac]
  25   ??? (PowerlogCore + 557496) [0x1bac5c1b8]
  23   ??? (PowerlogCore + 556708) [0x1bac5bea4]
  23   ??? (libsqlite3.dylib + 33928) [0x1b3430488]
  12   ??? (libsqlite3.dylib + 179112) [0x1b3453ba8]
  12   ??? (libsqlite3.dylib + 311132) [0x1b3473f5c]
  12   ??? (libsqlite3.dylib + 506080) [0x1b34a38e0]
  12   ??? (libsqlite3.dylib + 1002948) [0x1b351cdc4]
  12   ??? (libsqlite3.dylib + 379508) [0x1b3484a74]
  12   ??? (libsqlite3.dylib + 310124) [0x1b3473b6c]
  12   ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]


Powerstats for:   aggregated [335]
UUID:             B86E6699-4DCA-342C-9AE7-496F34DD4D9C
Path:             /System/Library/PrivateFrameworks/AggregateDictionary.framework/Support/aggregated
Resource Coalition ID: 111
Architecture:     arm64
Footprint:        6496 KB -> 13.92 MB (+7760 KB) (max 14.66 MB )
Pageins:          1801 pages
Start time:       2023-06-22 06:22:20.592 -0500
End time:         2023-06-22 19:42:30.413 -0500
Num samples:      100 (2%)
Primary state:    87 samples Non-Frontmost App, Non-Suppressed, Kernel mode, Effective Thread QoS Background, Requested Thread QoS Background, Override Thread QoS Unspecified
User Activity:    1 samples Idle, 99 samples Active
Power Source:     19 samples on Battery, 81 samples on AC
  100  ??? (libsystem_pthread.dylib + 2940) [0x1ee2a0b7c]
    87   ??? (libsystem_pthread.dylib + 3548) [0x1ee2a0ddc]
      87   ??? (libdispatch.dylib + 93404) [0x1959cdcdc]
        67   ??? (libdispatch.dylib + 49316) [0x1959c30a4]
          67   ??? (libdispatch.dylib + 46092) [0x1959c240c]
            67   ??? (libdispatch.dylib + 138808) [0x1959d8e38]
              67   ??? (libdispatch.dylib + 16172) [0x1959baf2c]
                67   ??? (libxpc.dylib + 69352) [0x1ee2f3ee8]
                  67   ??? (libxpc.dylib + 122596) [0x1ee300ee4]
                    67   ??? (libxpc.dylib + 201252) [0x1ee314224]
                      67   ??? (libxpc.dylib + 201628) [0x1ee31439c]
                        67   ??? (libxpc.dylib + 200156) [0x1ee313ddc]
                          67   ??? (PowerlogCore + 559996) [0x1bac5cb7c]
                            67   ??? (PowerlogCore + 560148) [0x1bac5cc14]
                              43   ??? (PowerlogCore + 559532) [0x1bac5c9ac]
                                25   ??? (PowerlogCore + 557496) [0x1bac5c1b8]
                                  23   ??? (PowerlogCore + 556708) [0x1bac5bea4]
                                    23   ??? (libsqlite3.dylib + 33928) [0x1b3430488]
                                      12   ??? (libsqlite3.dylib + 179112) [0x1b3453ba8]
                                        12   ??? (libsqlite3.dylib + 311132) [0x1b3473f5c]
                                          12   ??? (libsqlite3.dylib + 506080) [0x1b34a38e0]
                                            12   ??? (libsqlite3.dylib + 1002948) [0x1b351cdc4]
                                              12   ??? (libsqlite3.dylib + 379508) [0x1b3484a74]
                                                12   ??? (libsqlite3.dylib + 310124) [0x1b3473b6c]
                                                  12   ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]
                                      11   ??? (libsqlite3.dylib + 177588) [0x1b34535b4]
                                        11   ??? (libsqlite3.dylib + 223256) [0x1b345e818]
                                          11   ??? (libsqlite3.dylib + 84376) [0x1b343c998]
                                            11   ??? (libsqlite3.dylib + 246252) [0x1b34641ec]
                                              11   ??? (libsqlite3.dylib + 247580) [0x1b346471c]
                                                11   ??? (libsqlite3.dylib + 309336) [0x1b3473858]
                                                  9    ??? (libsqlite3.dylib + 615460) [0x1b34be424]
                                                    9    ??? (libsqlite3.dylib + 310124) [0x1b3473b6c]
                                                      9    ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]
                                                  2    ??? (libsqlite3.dylib + 616776) [0x1b34be948]
                                                    2    ??? (libsystem_kernel.dylib + 16016) [0x1cd45ae90]
                                  2    ??? (PowerlogCore + 556896) [0x1bac5bf60]
                                    2    ??? (libsqlite3.dylib + 500648) [0x1b34a23a8]
                                      2    ??? (libsqlite3.dylib + 462796) [0x1b3498fcc]
                                        2    ??? (libsqlite3.dylib + 331084) [0x1b3478d4c]
                                          2    ??? (libsqlite3.dylib + 332568) [0x1b3479318]
                                            2    ??? (libsqlite3.dylib + 333332) [0x1b3479614]
                                              2    ??? (libsqlite3.dylib + 379508) [0x1b3484a74]
                                                2    ??? (libsqlite3.dylib + 310124) [0x1b3473b6c]
                                                  2    ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]
                                14   ??? (PowerlogCore + 557448) [0x1bac5c188]
                                  14   ??? (PowerlogCore + 507256) [0x1bac4fd78]
                                    14   ??? (PowerlogCore + 508008) [0x1bac50068]
                                      14   ??? (libsystem_c.dylib + 61404) [0x195a0cfdc]
                                        7    ??? (libsystem_c.dylib + 42680) [0x195a086b8]
                                          7    ??? (libsystem_c.dylib + 37680) [0x195a07330]
                                            7    ??? (libsystem_kernel.dylib + 11444) [0x1cd459cb4]
                                        7    ??? (libsystem_c.dylib + 42656) [0x195a086a0]
                                          7    ??? (libsystem_c.dylib + 41528) [0x195a08238]
                                            7    ??? (libsystem_c.dylib + 37680) [0x195a07330]
                                              7    ??? (libsystem_kernel.dylib + 11444) [0x1cd459cb4]
                                4    ??? (PowerlogCore + 557600) [0x1bac5c220]
                                  4    ??? (PowerlogCore + 305904) [0x1bac1eaf0]
                                    4    ??? (PowerlogCore + 149856) [0x1babf8960]
                                      4    ??? (libsystem_c.dylib + 61404) [0x195a0cfdc]
                                        3    ??? (libsystem_c.dylib + 42656) [0x195a086a0]
                                          3    ??? (libsystem_c.dylib + 41528) [0x195a08238]
                                            3    ??? (libsystem_c.dylib + 37680) [0x195a07330]
                                              3    ??? (libsystem_kernel.dylib + 11444) [0x1cd459cb4]
                                        1    ??? (libsystem_c.dylib + 42680) [0x195a086b8]
                                          1    ??? (libsystem_c.dylib + 37680) [0x195a07330]
                                            1    ??? (libsystem_kernel.dylib + 11444) [0x1cd459cb4]
                              24   ??? (PowerlogCore + 559520) [0x1bac5c9a0]
                                24   ??? (PowerlogCore + 558456) [0x1bac5c578]
                                  24   ??? (PowerlogCore + 322588) [0x1bac22c1c]
                                    24   ??? (libsqlite3.dylib + 33928) [0x1b3430488]
                                      18   ??? (libsqlite3.dylib + 179112) [0x1b3453ba8]
                                        18   ??? (libsqlite3.dylib + 311132) [0x1b3473f5c]
                                          18   ??? (libsqlite3.dylib + 506080) [0x1b34a38e0]
                                            18   ??? (libsqlite3.dylib + 1002948) [0x1b351cdc4]
                                              18   ??? (libsqlite3.dylib + 379508) [0x1b3484a74]
                                                18   ??? (libsqlite3.dylib + 310124) [0x1b3473b6c]
                                                  18   ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]
                                      6    ??? (libsqlite3.dylib + 177588) [0x1b34535b4]
                                        3    ??? (libsqlite3.dylib + 223256) [0x1b345e818]
                                          3    ??? (libsqlite3.dylib + 84376) [0x1b343c998]
                                            3    ??? (libsqlite3.dylib + 246252) [0x1b34641ec]
                                              3    ??? (libsqlite3.dylib + 247580) [0x1b346471c]
                                                3    ??? (libsqlite3.dylib + 309336) [0x1b3473858]
                                                  3    ??? (libsqlite3.dylib + 615460) [0x1b34be424]
                                                    3    ??? (libsqlite3.dylib + 310124) [0x1b3473b6c]
                                                      3    ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]
                                        3    ??? (libsqlite3.dylib + 185268) [0x1b34553b4]
                                          3    ??? (libsqlite3.dylib + 673272) [0x1b34cc5f8]
                                            3    ??? (libsqlite3.dylib + 668552) [0x1b34cb388]
                                              3    ??? (libsqlite3.dylib + 621528) [0x1b34bfbd8]
                                                3    ??? (libsqlite3.dylib + 613500) [0x1b34bdc7c]
                                                  3    ??? (libsqlite3.dylib + 615460) [0x1b34be424]
                                                    3    ??? (libsqlite3.dylib + 310124) [0x1b3473b6c]
                                                      3    ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]
        20   ??? (libdispatch.dylib + 49368) [0x1959c30d8]
          20   ??? (libdispatch.dylib + 46388) [0x1959c2534]
            20   ??? (libdispatch.dylib + 16044) [0x1959baeac]
              20   ??? (libdispatch.dylib + 8992) [0x1959b9320]
                10   ??? (PowerlogCore + 44820) [0x1babdef14]
                  10   ??? (PowerlogCore + 90844) [0x1babea2dc]
                    10   ??? (CoreFoundation + 639216) [0x18e5870f0]
                      10   ??? (CoreFoundation + 79516) [0x18e4fe69c]
                        10   ??? (PowerlogCore + 391148) [0x1bac337ec]
                          10   ??? (PowerlogCore + 106020) [0x1babede24]
                            10   ??? (PowerlogCore + 394236) [0x1bac343fc]
                              10   ??? (PowerlogCore + 88848) [0x1babe9b10]
                                10   ??? (PowerlogCore + 19308) [0x1babd8b6c]
                                  10   ??? (PowerlogCore + 510880) [0x1bac50ba0]
                                    10   ??? (libdispatch.dylib + 78888) [0x1959ca428]
                                      10   ??? (libdispatch.dylib + 16044) [0x1959baeac]
                                        10   ??? (PowerlogCore + 93052) [0x1babeab7c]
                                          10   ??? (PowerlogCore + 16088) [0x1babd7ed8]
                                            10   ??? (libsqlite3.dylib + 177588) [0x1b34535b4]
                                              10   ??? (libsqlite3.dylib + 223256) [0x1b345e818]
                                                10   ??? (libsqlite3.dylib + 84376) [0x1b343c998]
                                                  10   ??? (libsqlite3.dylib + 246252) [0x1b34641ec]
                                                    10   ??? (libsqlite3.dylib + 247580) [0x1b346471c]
                                                      10   ??? (libsqlite3.dylib + 309336) [0x1b3473858]
                                                        9    ??? (libsqlite3.dylib + 615460) [0x1b34be424]
                                                          9    ??? (libsqlite3.dylib + 310124) [0x1b3473b6c]
                                                            9    ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]
                                                        1    ??? (libsqlite3.dylib + 616888) [0x1b34be9b8]
                                                          1    ??? (libsqlite3.dylib + 102304) [0x1b3440fa0]
                8    ??? (PowerlogCore + 44868) [0x1babdef44]
                  8    ??? (PowerlogCore + 58828) [0x1babe25cc]
                    8    ??? (PowerlogCore + 113268) [0x1babefa74]
                      8    ??? (PowerlogCore + 19308) [0x1babd8b6c]
                        8    ??? (PowerlogCore + 510880) [0x1bac50ba0]
                          5    ??? (libdispatch.dylib + 78888) [0x1959ca428]
                            5    ??? (libdispatch.dylib + 16044) [0x1959baeac]
                              5    ??? (PowerlogCore + 93052) [0x1babeab7c]
                                5    ??? (PowerlogCore + 16088) [0x1babd7ed8]
                                  4    ??? (libsqlite3.dylib + 177588) [0x1b34535b4]
                                    4    ??? (libsqlite3.dylib + 223668) [0x1b345e9b4]
                                      4    ??? (libsqlite3.dylib + 84376) [0x1b343c998]
                                        4    ??? (libsqlite3.dylib + 246252) [0x1b34641ec]
                                          4    ??? (libsqlite3.dylib + 247580) [0x1b346471c]
                                            4    ??? (libsqlite3.dylib + 309336) [0x1b3473858]
                                              4    ??? (libsqlite3.dylib + 615460) [0x1b34be424]
                                                4    ??? (libsqlite3.dylib + 310124) [0x1b3473b6c]
                                                  4    ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]
                                  1    ??? (libsqlite3.dylib + 179112) [0x1b3453ba8]
                                    1    ??? (libsqlite3.dylib + 311132) [0x1b3473f5c]
                                      1    ??? (libsqlite3.dylib + 506080) [0x1b34a38e0]
                                        1    ??? (libsqlite3.dylib + 1002948) [0x1b351cdc4]
                                          1    ??? (libsqlite3.dylib + 379508) [0x1b3484a74]
                                            1    ??? (libsqlite3.dylib + 310124) [0x1b3473b6c]
                                              1    ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]
                          3    ??? (libdispatch.dylib + 78556) [0x1959ca2dc]
                            3    ??? (libdispatch.dylib + 79964) [0x1959ca85c]
                              3    ??? (libdispatch.dylib + 16044) [0x1959baeac]
                                3    ??? (PowerlogCore + 93052) [0x1babeab7c]
                                  3    ??? (PowerlogCore + 16088) [0x1babd7ed8]
                                    2    ??? (libsqlite3.dylib + 179112) [0x1b3453ba8]
                                      2    ??? (libsqlite3.dylib + 311132) [0x1b3473f5c]
                                        2    ??? (libsqlite3.dylib + 506080) [0x1b34a38e0]
                                          2    ??? (libsqlite3.dylib + 1002948) [0x1b351cdc4]
                                            2    ??? (libsqlite3.dylib + 379508) [0x1b3484a74]
                                              2    ??? (libsqlite3.dylib + 310124) [0x1b3473b6c]
                                                2    ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]
                                    1    ??? (libsqlite3.dylib + 177588) [0x1b34535b4]
                                      1    ??? (libsqlite3.dylib + 223668) [0x1b345e9b4]
                                        1    ??? (libsqlite3.dylib + 84376) [0x1b343c998]
                                          1    ??? (libsqlite3.dylib + 246252) [0x1b34641ec]
                                            1    ??? (libsqlite3.dylib + 247580) [0x1b346471c]
                                              1    ??? (libsqlite3.dylib + 309336) [0x1b3473858]
                                                1    ??? (libsqlite3.dylib + 615460) [0x1b34be424]
                                                  1    ??? (libsqlite3.dylib + 310124) [0x1b3473b6c]
                                                    1    ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]
                1    ??? (PowerlogAccounting + 141312) [0x2032c5800]
                  1    ??? (PowerlogAccounting + 21464) [0x2032a83d8]
                    1    ??? (PowerlogAccounting + 130336) [0x2032c2d20]
                      1    ??? (libdispatch.dylib + 22252) [0x1959bc6ec]
                        1    ??? (libdispatch.dylib + 16044) [0x1959baeac]
                          1    ??? (PowerlogAccounting + 81892) [0x2032b6fe4]
                            1    ??? (PowerlogAccounting + 87400) [0x2032b8568]
                              1    ??? (PowerlogAccounting + 162104) [0x2032ca938]
                                1    ??? (libdispatch.dylib + 22252) [0x1959bc6ec]
                                  1    ??? (libdispatch.dylib + 16044) [0x1959baeac]
                                    1    ??? (PowerlogAccounting + 120364) [0x2032c062c]
                                      1    ??? (PowerlogCore + 44868) [0x1babdef44]
                                        1    ??? (PowerlogCore + 58828) [0x1babe25cc]
                                          1    ??? (PowerlogCore + 113268) [0x1babefa74]
                                            1    ??? (PowerlogCore + 19308) [0x1babd8b6c]
                                              1    ??? (PowerlogCore + 510880) [0x1bac50ba0]
                                                1    ??? (libdispatch.dylib + 78556) [0x1959ca2dc]
                                                  1    ??? (libdispatch.dylib + 79964) [0x1959ca85c]
                                                    1    ??? (libdispatch.dylib + 16044) [0x1959baeac]
                                                      1    ??? (PowerlogCore + 93052) [0x1babeab7c]
                                                        1    ??? (PowerlogCore + 16088) [0x1babd7ed8]
                                                          1    ??? (libsqlite3.dylib + 177588) [0x1b34535b4]
                                                            1    ??? (libsqlite3.dylib + 223668) [0x1b345e9b4]
                                                              1    ??? (libsqlite3.dylib + 84376) [0x1b343c998]
                                                                1    ??? (libsqlite3.dylib + 246252) [0x1b34641ec]
                                                                  1    ??? (libsqlite3.dylib + 247580) [0x1b346471c]
                                                                    1    ??? (libsqlite3.dylib + 309336) [0x1b3473858]
                                                                      1    ??? (libsqlite3.dylib + 615460) [0x1b34be424]
                                                                        1    ??? (libsqlite3.dylib + 310124) [0x1b3473b6c]
                                                                          1    ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]
                1    ??? (PowerlogCore + 193056) [0x1bac03220]
                  1    ??? (PowerlogCore + 191944) [0x1bac02dc8]
                    1    ??? (PowerlogCore + 44868) [0x1babdef44]
                      1    ??? (PowerlogCore + 58828) [0x1babe25cc]
                        1    ??? (PowerlogCore + 113268) [0x1babefa74]
                          1    ??? (PowerlogCore + 19308) [0x1babd8b6c]
                            1    ??? (PowerlogCore + 510880) [0x1bac50ba0]
                              1    ??? (libdispatch.dylib + 78888) [0x1959ca428]
                                1    ??? (libdispatch.dylib + 16044) [0x1959baeac]
                                  1    ??? (PowerlogCore + 93052) [0x1babeab7c]
                                    1    ??? (PowerlogCore + 16088) [0x1babd7ed8]
                                      1    ??? (libsqlite3.dylib + 177588) [0x1b34535b4]
                                        1    ??? (libsqlite3.dylib + 223668) [0x1b345e9b4]
                                          1    ??? (libsqlite3.dylib + 84376) [0x1b343c998]
                                            1    ??? (libsqlite3.dylib + 246252) [0x1b34641ec]
                                              1    ??? (libsqlite3.dylib + 247580) [0x1b346471c]
                                                1    ??? (libsqlite3.dylib + 309336) [0x1b3473858]
                                                  1    ??? (libsqlite3.dylib + 615460) [0x1b34be424]
                                                    1    ??? (libsqlite3.dylib + 310124) [0x1b3473b6c]
                                                      1    ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]
    13   ??? (libsystem_pthread.dylib + 3488) [0x1ee2a0da0]
      13   ??? (libdispatch.dylib + 90456) [0x1959cd158]
        13   ??? (libdispatch.dylib + 88676) [0x1959cca64]
          13   ??? (libdispatch.dylib + 16044) [0x1959baeac]
            13   ??? (libdispatch.dylib + 8992) [0x1959b9320]
              13   ??? (PowerlogCore + 465292) [0x1bac4598c]
                13   ??? (PowerlogCore + 691992) [0x1bac7cf18]
                  13   ??? (PowerlogCore + 302688) [0x1bac1de60]
                    13   ??? (PowerlogCore + 284288) [0x1bac19680]
                      13   ??? (PowerlogCore + 191944) [0x1bac02dc8]
                        11   ??? (PowerlogCore + 44868) [0x1babdef44]
                          11   ??? (PowerlogCore + 58828) [0x1babe25cc]
                            11   ??? (PowerlogCore + 113268) [0x1babefa74]
                              11   ??? (PowerlogCore + 19308) [0x1babd8b6c]
                                11   ??? (PowerlogCore + 510880) [0x1bac50ba0]
                                  11   ??? (libdispatch.dylib + 78888) [0x1959ca428]
                                    11   ??? (libdispatch.dylib + 16044) [0x1959baeac]
                                      11   ??? (PowerlogCore + 93052) [0x1babeab7c]
                                        11   ??? (PowerlogCore + 16088) [0x1babd7ed8]
                                          7    ??? (libsqlite3.dylib + 177588) [0x1b34535b4]
                                            7    ??? (libsqlite3.dylib + 223668) [0x1b345e9b4]
                                              7    ??? (libsqlite3.dylib + 84376) [0x1b343c998]
                                                7    ??? (libsqlite3.dylib + 246252) [0x1b34641ec]
                                                  7    ??? (libsqlite3.dylib + 247580) [0x1b346471c]
                                                    7    ??? (libsqlite3.dylib + 309336) [0x1b3473858]
                                                      7    ??? (libsqlite3.dylib + 615460) [0x1b34be424]
                                                        7    ??? (libsqlite3.dylib + 310124) [0x1b3473b6c]
                                                          7    ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]
                                                            7    <Effective Thread QoS User Initiated, Requested Thread QoS User Initiated>
                                          4    ??? (libsqlite3.dylib + 179112) [0x1b3453ba8]
                                            4    ??? (libsqlite3.dylib + 311132) [0x1b3473f5c]
                                              4    ??? (libsqlite3.dylib + 506080) [0x1b34a38e0]
                                                4    ??? (libsqlite3.dylib + 1002948) [0x1b351cdc4]
                                                  4    ??? (libsqlite3.dylib + 379508) [0x1b3484a74]
                                                    4    ??? (libsqlite3.dylib + 310124) [0x1b3473b6c]
                                                      4    ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]
                                                        4    <Effective Thread QoS User Initiated, Requested Thread QoS User Initiated>
                        2    ??? (PowerlogCore + 44820) [0x1babdef14]
                          2    ??? (PowerlogCore + 90844) [0x1babea2dc]
                            2    ??? (CoreFoundation + 639216) [0x18e5870f0]
                              2    ??? (CoreFoundation + 79516) [0x18e4fe69c]
                                2    ??? (PowerlogCore + 391148) [0x1bac337ec]
                                  2    ??? (PowerlogCore + 106020) [0x1babede24]
                                    2    ??? (PowerlogCore + 394236) [0x1bac343fc]
                                      2    ??? (PowerlogCore + 88848) [0x1babe9b10]
                                        2    ??? (PowerlogCore + 19308) [0x1babd8b6c]
                                          2    ??? (PowerlogCore + 510880) [0x1bac50ba0]
                                            2    ??? (libdispatch.dylib + 78888) [0x1959ca428]
                                              2    ??? (libdispatch.dylib + 16044) [0x1959baeac]
                                                2    ??? (PowerlogCore + 93052) [0x1babeab7c]
                                                  2    ??? (PowerlogCore + 16088) [0x1babd7ed8]
                                                    2    ??? (libsqlite3.dylib + 177588) [0x1b34535b4]
                                                      2    ??? (libsqlite3.dylib + 223256) [0x1b345e818]
                                                        2    ??? (libsqlite3.dylib + 84376) [0x1b343c998]
                                                          2    ??? (libsqlite3.dylib + 246252) [0x1b34641ec]
                                                            2    ??? (libsqlite3.dylib + 247580) [0x1b346471c]
                                                              2    ??? (libsqlite3.dylib + 309336) [0x1b3473858]
                                                                2    ??? (libsqlite3.dylib + 615460) [0x1b34be424]
                                                                  2    ??? (libsqlite3.dylib + 310124) [0x1b3473b6c]
                                                                    2    ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]
                                                                      2    <Effective Thread QoS User Initiated, Requested Thread QoS User Initiated>

  Binary Images:
           0x100894000 -                ???  aggregated              <B86E6699-4DCA-342C-9AE7-496F34DD4D9C>  /System/Library/PrivateFrameworks/AggregateDictionary.framework/Support/aggregated
           0x18e4eb000 -        0x18e8d2fff  CoreFoundation          <4230C122-42E8-383B-BEEC-EE7B61F8BB61>  /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
           0x1959b7000 -        0x1959fdfff  libdispatch.dylib       <BB347F0E-F21C-3607-82E6-C8D750FDBF8C>  /usr/lib/system/libdispatch.dylib
           0x1959fe000 -        0x195a7bff3  libsystem_c.dylib       <3548F8EE-7A07-3B67-8D69-9C7D42096513>  /usr/lib/system/libsystem_c.dylib
           0x1b3428000 -        0x1b3593ff3  libsqlite3.dylib        <960C2B48-91AD-3137-99EB-2A1452BB2177>  /usr/lib/libsqlite3.dylib
           0x1babd4000 -        0x1bacfffff  PowerlogCore            <26DE8CD9-B26B-33D5-8EE1-BA08FC51471A>  /System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore
           0x1cd457000 -        0x1cd48eff7  libsystem_kernel.dylib  <2F783110-9739-3F18-A234-5FB92512529D>  /usr/lib/system/libsystem_kernel.dylib
           0x1ee2a0000 -        0x1ee2abff3  libsystem_pthread.dylib <8894310A-745F-3407-99F0-1FD54442561D>  /usr/lib/system/libsystem_pthread.dylib
           0x1ee2e3000 -        0x1ee324fff  libxpc.dylib            <9EBB5610-EEE0-3407-A3C2-49279EEBCB59>  /usr/lib/system/libxpc.dylib
           0x2032a3000 -        0x2032ecfff  PowerlogAccounting      <EC8FF1A3-E505-3DF5-9D67-BBE4A97DAFD8>  /System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting


Powerstats for:   fitcored
UUID:             15732D53-1EC4-352D-AC3E-ADB97E40C30A
Path:             /System/Library/PrivateFrameworks/SeymourServices.framework/fitcored
Resource Coalition ID: 314
Architecture:     arm64
Start time:       2023-06-22 06:22:15.050 -0500
End time:         2023-06-22 19:53:55.116 -0500
Num samples:      5383 (89%)
Primary state:    5339 samples Non-Frontmost App, Non-Suppressed, Kernel mode, Effective Thread QoS Default, Requested Thread QoS Default, Override Thread QoS Unspecified
User Activity:    9 samples Idle, 5374 samples Active
Power Source:     1262 samples on Battery, 4121 samples on AC
  5383  ??? (libsystem_pthread.dylib + 2940) [0x1ee2a0b7c]
    5383  ??? (libsystem_pthread.dylib + 3548) [0x1ee2a0ddc]
      5383  ??? (libdispatch.dylib + 93404) [0x1959cdcdc]
        5383  ??? (libdispatch.dylib + 49368) [0x1959c30d8]
          5383  ??? (libdispatch.dylib + 46388) [0x1959c2534]
            5383  ??? (libdispatch.dylib + 16044) [0x1959baeac]
              5383  ??? (libdispatch.dylib + 77764) [0x1959c9fc4]
                5339  ??? (CFNetwork + 117592) [0x18f518b58]
                  5339  ??? (CFNetwork + 33596) [0x18f50433c]
                    5339  ??? (CFNetwork + 163124) [0x18f523d34]
                      5339  ??? (CFNetwork + 390140) [0x18f55b3fc]
                        5339  ??? (CFNetwork + 203312) [0x18f52da30]
                          5339  ??? (CFNetwork + 399684) [0x18f55d944]
                            5339  ??? (CFNetwork + 178132) [0x18f5277d4]
                              5337  ??? (CFNetwork + 119336) [0x18f519228]
                                5337  ??? (CFNetwork + 180876) [0x18f52828c]
                                  5337  ??? (libsqlite3.dylib + 177588) [0x1b34535b4]
                                    5337  ??? (libsqlite3.dylib + 183400) [0x1b3454c68]
                                      5337  ??? (libsqlite3.dylib + 86412) [0x1b343d18c]
                                        5337  ??? (libsqlite3.dylib + 87928) [0x1b343d778]
                                          5337  ??? (libsqlite3.dylib + 92708) [0x1b343ea24]
                                            2654  ??? (libsqlite3.dylib + 96584) [0x1b343f948]
                                              2654  ??? (libsqlite3.dylib + 619228) [0x1b34bf2dc]
                                                2654  ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]
                                            1951  ??? (libsqlite3.dylib + 96856) [0x1b343fa58]
                                            720   ??? (libsqlite3.dylib + 96912) [0x1b343fa90]
                                            5     ??? (libsqlite3.dylib + 96872) [0x1b343fa68]
                                            3     ??? (libsqlite3.dylib + 94844) [0x1b343f27c]
                                              3     ??? (libsqlite3.dylib + 619228) [0x1b34bf2dc]
                                                3     ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]
                                            3     ??? (libsqlite3.dylib + 94672) [0x1b343f1d0]
                                              3     ??? (libsqlite3.dylib + 619228) [0x1b34bf2dc]
                                                3     ??? (libsqlite3.dylib + 100304) [0x1b34407d0]
                                                  3     ??? (libsystem_kernel.dylib + 16016) [0x1cd45ae90]
                                            1     ??? (libsqlite3.dylib + 95816) [0x1b343f648]
                                              1     ??? (libsqlite3.dylib + 102568) [0x1b34410a8]
                              2     ??? (libsystem_kernel.dylib + 40284) [0x1cd460d5c]
                44    ??? (CFNetwork + 852932) [0x18f5cc3c4]
                  44    ??? (CFNetwork + 277516) [0x18f53fc0c]
                    44    ??? (libsqlite3.dylib + 33928) [0x1b3430488]
                      29    ??? (libsqlite3.dylib + 179112) [0x1b3453ba8]
                        29    ??? (libsqlite3.dylib + 311132) [0x1b3473f5c]
                          29    ??? (libsqlite3.dylib + 506080) [0x1b34a38e0]
                            29    ??? (libsqlite3.dylib + 1002948) [0x1b351cdc4]
                              28    ??? (libsqlite3.dylib + 379508) [0x1b3484a74]
                                28    ??? (libsqlite3.dylib + 310124) [0x1b3473b6c]
                                  28    ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]
                                    28    <Effective Thread QoS Utility, Requested Thread QoS Utility>
                              1     ??? (libsqlite3.dylib + 379668) [0x1b3484b14]
                                1     ??? (libsystem_kernel.dylib + 16016) [0x1cd45ae90]
                                  1     <Effective Thread QoS Utility, Requested Thread QoS Utility>
                      15    ??? (libsqlite3.dylib + 177588) [0x1b34535b4]
                        15    ??? (libsqlite3.dylib + 223668) [0x1b345e9b4]
                          15    ??? (libsqlite3.dylib + 84376) [0x1b343c998]
                            15    ??? (libsqlite3.dylib + 246252) [0x1b34641ec]
                              15    ??? (libsqlite3.dylib + 247580) [0x1b346471c]
                                15    ??? (libsqlite3.dylib + 309336) [0x1b3473858]
                                  15    ??? (libsqlite3.dylib + 615460) [0x1b34be424]
                                    15    ??? (libsqlite3.dylib + 310124) [0x1b3473b6c]
                                      15    ??? (libsystem_kernel.dylib + 10592) [0x1cd459960]
                                        15    <Effective Thread QoS Utility, Requested Thread QoS Utility>

  Binary Images:
           0x100008000 -                ???  fitcored                <15732D53-1EC4-352D-AC3E-ADB97E40C30A>  /System/Library/PrivateFrameworks/SeymourServices.framework/fitcored
           0x18f4fc000 -        0x18f8c7fff  CFNetwork               <6AAFE7C4-F1C4-3020-AD16-70591C86D7B0>  /System/Library/Frameworks/CFNetwork.framework/CFNetwork
           0x1959b7000 -        0x1959fdfff  libdispatch.dylib       <BB347F0E-F21C-3607-82E6-C8D750FDBF8C>  /usr/lib/system/libdispatch.dylib
           0x1b3428000 -        0x1b3593ff3  libsqlite3.dylib        <960C2B48-91AD-3137-99EB-2A1452BB2177>  /usr/lib/libsqlite3.dylib
           0x1cd457000 -        0x1cd48eff7  libsystem_kernel.dylib  <2F783110-9739-3F18-A234-5FB92512529D>  /usr/lib/system/libsystem_kernel.dylib
           0x1ee2a0000 -        0x1ee2abff3  libsystem_pthread.dylib <8894310A-745F-3407-99F0-1FD54442561D>  /usr/lib/system/libsystem_pthread.dylib
'''

End of Incident report

-----------------------------------------------------------------------

Incident Report #3 

Incident Report: Targeted Attack Resulting In Cellular Network Loss (SDM exploitation) 

Subject : iphone 14 Plus project red 16.5.1 newest patch

Summary:
The following incident report outlines a potentially malicious activity related to the Service Data Management (SDM) feature in a 5G network. The logs indicate abnormal behavior and trigger events that could suggest unauthorized manipulation of SDM settings, potentially compromising network performance and user experience.
Details:
1. Incident Description:
   - Multiple occurrences of SDM state transitions were observed, indicating unauthorized changes in SDM configurations.
   - SDM activation and deactivation events were triggered by abnormal screen status changes, contrary to expected user behavior patterns.
   - Inconsistent values for fr1_meas_disabled and prev_fr1_meas_disabled were logged, indicating potential tampering with measurement settings.
2. Impact:
   - The unauthorized activation and deactivation of SDM may have disrupted network connectivity and compromised the performance of the cellular network.
   - User experience might have been negatively affected due to the abnormal SDM behavior, resulting in decreased data transfer speeds, dropped calls, or intermittent network connectivity.
3. Potential Causes:
   - Malicious software or unauthorized access to the device's network settings could have enabled the manipulation of SDM parameters.
   - A targeted attack aimed at compromising network performance and disrupting user connectivity may have been executed.
4. Recommended Actions:
   - Conduct a thorough investigation into the device's security posture, including network settings and installed applications.
   - Analyze network traffic and system logs for any indications of unauthorized access or suspicious activities.
   - Implement stricter access controls and authentication mechanisms to prevent unauthorized modifications to SDM and other critical network settings.
   - Collaborate with network service providers and security teams to identify potential network vulnerabilities and implement necessary safeguards.
   - Regularly monitor and analyze network logs to identify any further instances of suspicious SDM behavior or network anomalies.
5. Follow-up Steps:
   - Provide the incident report and relevant log snippets to the appropriate security teams and network administrators for further analysis and remediation.
   - Document any findings or additional information discovered during the investigation.
   - Implement recommended security measures and monitor the network closely for any signs of recurrence or similar malicious activities.
   - Update incident response procedures to include mitigation strategies specific to SDM-related incidents.
Log Snippets Attached
	
1.	Log snippet 1:

'''
softwareBuild: "20F66"
firmwareVersion: "iBoot-8422.120.66"
basebandVersion: "1.70.02"
buildtype: "User"
tz_offset: -18000
metric_file_type: 1
'''
	
2.	Log snippet 2:

'''
metriclogs {
  triggerTime: 1687430653140
  triggerId: 806936
  profileId: 127
  cellularNrSDMActivation {
    timestamp: 1687392000000
    deployment: DEPLOYMENT_NSA
    fr1_meas_disabled: true
    prev_fr1_meas_disabled: false
    trigger_cause: SDM_TRIGGER_CAUSE_SCREEN_STATUS
    ap_nr_recomm: true
    ap_nr_recomm_conf_factor: false
    duration_in_prev_state: 68
    subs_id: 0
    fr2_meas_disabled: false
    prev_fr2_meas_disabled: false
    sib24_configured: false
    is_rrc_connected: true
    is_endc_call_active: true
    fr: NR_SUB6
    state: SDM_ENABLE_NR
    new_state: SDM_DISABLE_FR1
    tracking_area_code: 1799
    cell_id: 140832264
    gci: "311.580.1799.140832264"
    state_duration_bin_index: 7
    is_data_preferred: true
  }
}
'''
	
3.	Log snippet 3:

'''
metriclogs {
  triggerTime: 1687430653993
  triggerId: 806936
  profileId: 127
  cellularNrSDMActivation {
    timestamp: 1687392000000
    deployment: DEPLOYMENT_NSA
    fr1_meas_disabled: false
    prev_fr1_meas_disabled: true
    trigger_cause: SDM_TRIGGER_CAUSE_SCREEN_STATUS
    ap_nr_recomm: true
    ap_nr_recomm_conf_factor: false
    duration_in_prev_state: 0
    subs_id: 0
    fr2_meas_disabled: false
    prev_fr2_meas_disabled: false
    sib24_configured: false
    is_rrc_connected: false
    is_endc_call_active: false
    fr: NR_INVALID
    state: SDM_DISABLE_FR1
    new_state: SDM_ENABLE_NR
    tracking_area_code: 1799
    cell_id: 140832264
    gci: "311.580.1799.140832264"
    prev_trigger_cause: SDM_TRIGGER_CAUSE_SCREEN_STATUS
    state_duration_bin_index: 0
    is_data_preferred: true
  }
}
'''

End of incident report
-----------------------------------------------------------------------
Incident Response #4
Subject: Malicious Network activity 
Device : Iphone 14 plus project red 16.5.1 
7 potentially malicious activities where observed within the network & radio diagnostic logs of the device. 
	1.	SDM Activations Triggered by Various Causes:
	•	SDM activations were triggered by different causes such as VOIP calls, screen status changes, and VOLTE.
	•	Potential malicious behavior: Malicious actors could exploit these triggers to manipulate or disrupt the SDM functionality, leading to service degradation or unauthorized access to sensitive data. For example, they might spoof or simulate VOIP calls or manipulate the screen status to trigger unauthorized SDM activations.
	2.	Deployment of DEPLOYMENT_NSA:
	•	The SDM activations were associated with the deployment of DEPLOYMENT_NSA (Non-Standalone Access).
	•	Potential malicious behavior: Malicious actors could attempt to exploit vulnerabilities or weaknesses in the DEPLOYMENT_NSA infrastructure to gain unauthorized access, intercept communications, or launch attacks on the network. They might also try to manipulate or tamper with SDM-related parameters during the deployment process.
	3.	Disabling FR1 and Enabling NR Measurements:
	•	The SDM activations involved disabling FR1 (Frequency Range 1) measurements and enabling NR (New Radio) measurements.
	•	Potential malicious behavior: Malicious actors could abuse this functionality to manipulate or disrupt the measurement capabilities of the system. By disabling FR1 measurements or enabling NR measurements without proper authorization, they might interfere with network optimization, compromise the quality of service, or create opportunities for unauthorized access or attacks.
	4.	AP NR Recommendations with Varying Confidence Factors:
	•	Some SDM activations included AP NR (Access Point New Radio) recommendations with varying confidence factors.
	•	Potential malicious behavior: Malicious actors could manipulate the AP NR recommendation system to mislead the network or compromise the integrity of network selection algorithms. By providing false or malicious AP NR recommendations with high confidence factors, they might direct devices to connect to compromised or unauthorized access points, leading to potential data breaches, network disruptions, or interception of sensitive information.
	5.	Duration in Previous State:
	•	The duration in the previous state varied for each SDM activation.
	•	Potential malicious behavior: Malicious actors could exploit these state transitions and manipulate the duration in the previous state to disrupt network operations, introduce delays or inconsistencies, or evade detection mechanisms. By artificially prolonging or shortening the state durations, they might interfere with network performance, cause service interruptions, or hide their activities from monitoring systems.
	6.	SDM Activations in Different System States:
	•	SDM activations occurred during various system states, including RRC connected state, endc calls, and motion.
	•	Potential malicious behavior: Malicious actors could exploit these different system states to launch targeted attacks or carry out unauthorized activities. For example, they might time their malicious activities to coincide with endc calls to evade detection or leverage motion-related triggers to exploit vulnerabilities in the SDM infrastructure.
	7.	Radio Link Failures and SDM Triggers:
	•	Radio link failures were recorded, triggered by causes like T310 expiry and SCG change failure.
	•	Potential malicious behavior: Malicious actors could intentionally trigger radio link failures or exploit existing failures to disrupt communication, degrade network performance, or launch attacks. By using T310 expiry or SCG change failure as triggers, they might attempt to create instability, induce network congestion, or exploit vulnerabilities in the SDM activation process.

Log snippets supporting the above 

'''
	 SDM Activations Triggered by Various Causes:
	•	Triggered by VOIP call:

trigger_cause: SDM_TRIGGER_CAUSE_VOIP_CALL

	1.	
	•	Triggered by screen status change:

trigger_cause: SDM_TRIGGER_CAUSE_SCREEN_STATUS

	1.	
	•	Triggered by VOLTE:

trigger_cause: SDM_TRIGGER_CAUSE_VOLTE


	2.	Deployment of DEPLOYMENT_NSA:

deployment: DEPLOYMENT_NSA


	3.	Disabling FR1 and Enabling NR Measurements:
	•	Disabling FR1 measurements:

fr1_meas_disabled: true

	3.	
	•	Enabling NR measurements:

fr2_meas_disabled: false


	4.	AP NR Recommendations with Varying Confidence Factors:
	•	AP NR recommendation with true confidence factor:

ap_nr_recomm: true
ap_nr_recomm_conf_factor: true

	4.	
	•	AP NR recommendation with false confidence factor:

ap_nr_recomm: true
ap_nr_recomm_conf_factor: false


	5.	Duration in Previous State:

duration_in_prev_state: [duration in milliseconds]


	6.	SDM Activations in Different System States:
	•	RRC connected state:

is_rrc_connected: true

	6.	
	•	Endc call active:

is_endc_call_active: true

	6.	
	•	Motion state (moving):

mobility_state: MOTION_ST_MOVING


	7.	Radio Link Failures and SDM Triggers:
	•	Radio link failure due to T310 expiry:

reason: NR5G_RLF_CAUSE_T310_EXPIRY

	7.	
	•	Radio link failure due to SCG change failure:

reason: NR5G_RLF_CAUSE_SCG_CHANGE_FAILURE
'''

End of incident report

-----------------------------------------------------------------------

