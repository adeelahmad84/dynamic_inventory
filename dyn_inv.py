#!/usr/bin/env python
# -*- coding: utf-8;

"""
---
File:           dyn_inv.py
Author:         Adeel Ahmad
Email:          adeelahmad84@me.com
Github:         https://github.com/adeelahmad84
Description:    Ansible Dynamic Inventory script.
"""

__version__ = "0.1"

from __future__ import (absolute_import, division, print_function, unicode_literals)

import argparse

def main():
    """The main function to import variables dynamically for Ansible"""

    #Argument Parsing
    parser = argparse.ArgumentParser(description="Ansible dynamic inventory")
    parser.add_argument("--list", help="Ansible inventory of all of the groups", \
                        action="store_true", dest="list_inventory")
    parser.add_argument("--host", \
                       help="Ansible inventory of a particular host", action="store", \
                       dest="ansible_host", type=str)

    cli_args = parser.parse_args()
    list_inventory = cli_args.list_inventory
    ansible_host = cli_args.ansible_host

    print("list_inventory: {}".format(list_inventory))
    print("ansible_host: {}".format(ansible_host))

if __name__ == "__main__":
    main()
