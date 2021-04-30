#!usr/bin/env pyhton

import subprocess
import optparse

parser = optparse.OptionParser()

interface = input("interface >")
new_mac = input("new_mac ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])