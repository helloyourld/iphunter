import sys
import requests
import ipaddress
import os


banner = '''
      ::::::::::: :::::::::  :::    ::: :::    ::: ::::    ::: ::::::::::: :::::::::: ::::::::: 
         :+:     :+:    :+: :+:    :+: :+:    :+: :+:+:   :+:     :+:     :+:        :+:    :+: 
        +:+     +:+    +:+ +:+    +:+ +:+    +:+ :+:+:+  +:+     +:+     +:+        +:+    +:+  
       +#+     +#++:++#+  +#++:++#++ +#+    +:+ +#+ +:+ +#+     +#+     +#++:++#   +#++:++#:    
      +#+     +#+        +#+    +#+ +#+    +#+ +#+  +#+#+#     +#+     +#+        +#+    +#+    
     #+#     #+#        #+#    #+# #+#    #+# #+#   #+#+#     #+#     #+#        #+#    #+#     
########### ###        ###    ###  ########  ###    ####     ###     ########## ###    ###      
'''


def list_ip_addresses(ip_address, cidr_netmask):
    try:
        net = ipaddress.ip_network(
            f"{ip_address}/{cidr_netmask}", strict=False)

        if not os.path.exists("saved"):
            os.makedirs("saved")

        filename = f"saved/{ip_address}.txt"
        with open(filename, "w") as f:
            for ip in net:
                f.write(str(ip) + "\n")

        print(
            f"Successfully listed all IP addresses in the netblock {net} and saved them to {filename}")

    except Exception as e:
        print(f"Error: {e}")


def lookup_asn(ip_address):
    try:
        response = requests.get(
            f"https://api.hackertarget.com/aslookup/?q={ip_address}")

        if "API count exceeded" in response.text:
            print(response.text.strip())
            return

        if response.status_code != 200:
            print(
                f"Error: Could not retrieve ASN information for {ip_address}.")
            return

        ip, asn_number, asn_range, asn_description = response.text.strip().split('","')
        asn_description = asn_description[:-1]

        print(
            f"IP address {ip_address} belongs to ASN {asn_number}: {asn_description}")
        print(f"AS range: {asn_range}")

        ip_address, cidr_netmask = asn_range.split("/")

        list_ip_addresses(ip_address, cidr_netmask)

    except Exception as e:
        print(f"Error: {e}")


def main():
    if len(sys.argv) == 1:
        print(
            f"Usage: python3 {sys.argv[0]} [-t <IP Address>] [-f <filename>]")
        return

    if "-t" in sys.argv:
        ip_index = sys.argv.index("-t") + 1
        ip_address = sys.argv[ip_index]
        lookup_asn(ip_address)
    elif "-f" in sys.argv:
        filename_index = sys.argv.index("-f") + 1
        filename = sys.argv[filename_index]
        with open(filename, "r") as f:
            for line in f:
                ip_address = line.strip()
                lookup_asn(ip_address)
    else:
        print(
            f"Usage: python3 {sys.argv[0]} [-t <IP Address>] [-f <filename>]")
        return


if __name__ == "__main__":
    print(banner)
    print("Note: Only 50 queries per day.\n")
    main()
