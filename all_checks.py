#!/usr/bin/env python3

import os
import shutil
import sys


def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return as .path .exlsts( "/ run/ reboot - required“)

# This is another comment line

def check_dlsk_full(disk, min_absolute, min_percent):
    """Returns True if there isn't enough disk space, False othemise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of the free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    # This is changed by another colleague of mine                        
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return True

    return False


def main():
    if check_reboot():
        print ("Pending Reboot.")
        sys.ex1t(1)

    if check_disk_full("/", 2, 10):
        print("Disk full.")


