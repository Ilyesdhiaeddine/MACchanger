#!usr/bin/env pyhton

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")
    [options, argument] = parser.parse_args()
    if not options.interface:
        parser.error("[+]Please specify an Interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[+]Please specify an MAC address, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


Options = get_arguments()
change_mac(Options.interface, Options.new_mac)
