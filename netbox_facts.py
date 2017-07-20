#!/usr/bin/env python
# -- coding: utf-8 --

ANSIBLE_METADATA = {'version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = """
---
module: netbox_facts
short description: Manage the IPAM aspect of Netbox
description:
    - Add/remove prefixes
    - Validating Prefixes with interfaces
    - Allocating next available IP Range
version_added: "0.1"
author: Adeel Ahmad (@adeelahmad84)
options:
    first_option:
        description:
            - Description of the options goes here.
            - Must be written in sentences.
        required: true or false
        default: string value or the word null
        choices:
            - enable
            - disable
        aliases:
            - repo_name
        version_added: "0.1"
    second_option:
        description:
            - Description of the options goes here.
            - Must be written in sentences.
        required: true or false
        default: string value or the word null
        choices:
            - enable
            - disable
        aliases:
            - repo_name
        version_added: "0.1"
    third_option:
        description:
            - Description of the options goes here.
            - Must be written in sentences.
        required: true or false
        default: string value or the word null
        choices:
            - enable
            - disable
        aliases:
            - repo_name
        version_added: "0.1"
"""

EXAMPLES = """
- name: Allocate Loopback IP
  netbox_ipam:
      type: 'loopback'
      host: {{ inventory_hostname }}
"""


RETURN = """
updates:
    description: first description
    returned: success
    type: string
    sample: 'doodoo'
"""

import re
import unittest

try:
    import json
except ImportError:
    import simplejson as json

try:
    import requests
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    imported = True
except ImportError:
    imported = False

from module_utils.basic import AnsibleModule
from module_utils.basic import get_exception
from module_utils.six import iteritems
from module_utils.urls import SSLValidationError
from module_utils.urls import url_argument_spec
from module_utils.urls import fetch_url

server_name = 'https://netbox.example.com'
api_endpoint = '/api/ipam/prefixes/'
headers = {'Content-Type':'application/json'}
header_update = {'Authorization': 'Token 83d60a94dadc64789c1490c65ab4b99aa8abc322'}

def api_request(method, url, data=None):
    if method == 'GET':
        try:
            r = requests.get(url)
        except:
            return False
    elif method == 'POST':
        try:
            r = requests.post(url, data=data)
        except:
            return False
    elif method == 'DELETE':
        try:
            r = requests.delete(url)
        except:
            return False
    else:
        return False
    if r.status_code != requests.codes.ok:
        return False
    else:
        json = r.json()
        if 'error' in json:
            return False
        else:
            return json

def main():
    """
    This module will liaise the Fresh Service Desk API.
    """
    module = AnsibleModule(
        argument_spec=dict(
            application=dict(required=True, \
                                  choices=['circuit', 'dcim', 'extras', \
                                           'ipam', 'secrets', 'tenancy']),
            endpoint=dict(required=True, type='str'),
            endpoint_id=dict(required=False)
            ),
        supports_check_mode=False
    )

    application = module.params['application']
    endpoint        = module.params['endpoint']
    endpoint_id     = module.params['endpoint_id']

    if not imported:
        module.fail_json(msg='Failed to import required packages')

    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



if __name__ == '__main__':
    main()
    import doctest
    doctest.testmod()
    class MyTest(unittest.TestCase):
        def test(self):
            self.assertEqual(main(), )
