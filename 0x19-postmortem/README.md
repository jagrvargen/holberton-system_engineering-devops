# POSTMORTEM
### Summary
On 5-1-18, from 04:03 to 13:30 PST, of yet unknown bad actors accessed and downloaded multiple gigabytes of sensitive user information including social security numbers, credit scores, and home addresses before the SRE team was successfully able to isolate and contain the breach. Due to an vulnerability in the Apache Struts 2 web application software, hackers were able to manipulate HTTP headers to issue commands within our servers. Handling the issue required a systemwide shutdown which led to 8.5 hours of network downtime.

### Timeline
- 04:03 - Our monitoring service sent out an alert to the security team that an abnormal spike in traffic was taking place and required immediate attention.
- 04:05 - The SRE team was paged and made aware of the suspicious activity.
- 04:30 - After ruling out an unintentional data backup and mail server issues, the team determines that a complete network shutdown is necessary.
- 05:00 - Lead systems administrator Luc Squaiwakker makes the determination that unpatched Apache Struts 2 software has allowed hackers to manipulate the file system and access sensitive information. Systemwide software patching begins.
- 13:30 - Patching is completed and the network is rebooted.

### Root Cause/Resolution
- Despite being warned of the vulnerability 2 months in advance, Equalfacks board members pushed back against software patching due to potential short-term financial losses. Hackers were able to locate the vulnerability in the system and make a quick grab of sensitive data. A simple network shutdown and software patching resolved further data loss, however the extent of the damage caused by the breach is as of yet undeterminable, and likely severe.

### Corrective and Preventative Measures
- The best course of action would be to set in place more robust software patching protocols. Furthermore, long-term security concerns should take precedence over short-term financial interests. It is likely that Equalfacks executives will have to increase congressional lobby spending for a brief period.
