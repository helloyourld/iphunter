# IPHUNTER
This is a simple command-line tool that allows you to retrieve the Autonomous System Number (ASN) and ASN range of an IP address using the hackertarget.com API. Then it will list all IP addresses in the ASN range.

# Installation:

Clone the repository: `git clone https://github.com/helloyourld/iphunter.git`

Navigate to the project directory: `cd iphunter`

Install the dependencies: `pip3 install -r requirements.txt`

# Usage:

To look up the ASN and ASN range of a single IP address, run: `python3 iphunter.py -t <IP Address>`

To look up the ASN and ASN range of multiple IP addresses from a file, run: `python3 iphunter.py -f <filename>`

**Note: The tool has a limit of 50 queries per day.**

Example usage:

`python3 iphunter.py -t 8.8.8.8`

`python3 iphunter.py -f ips.txt`

