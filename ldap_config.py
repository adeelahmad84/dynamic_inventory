#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
---
File:           ldap_config.py
Author:         Adeel Ahmad
Email:          adeelahmad84@me.com
Github:         https://github.com/adeelahmad84
Description:    LDAP script for Netbox.
"""

__version__ = "0.1"

import ldap
from django_auth_ldap.config import LDAPSearch
from django_auth_ldap.config import GroupOfNamesType

# Server URI
AUTH_LDAP_SERVER_URI = "ldaps://ad.example.com"

# The following may be needed if you are binding to Active Directory.
AUTH_LDAP_CONNECTION_OPTIONS = {
        ldap.OPT_REFERRALS: 0
}

# Set the DN and password for the NetBox service account.
AUTH_LDAP_BIND_DN = "CN=NETBOXSA, OU=Service Accounts,DC=example,DC=com"
AUTH_LDAP_BIND_PASSWORD = "demo"

# Include this setting if you want to ignore certificate errors. This might be
# needed to accept a self-signed cert.
# Note that this is a NetBox-specific setting which sets:
#     ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
LDAP_IGNORE_CERT_ERRORS = True

AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=Users,dc=example,dc=com",
                                   ldap.SCOPE_SUBTREE,
                                   "(sAMAccountName=%(user)s)")

# If a user's DN is producible from their username, we don't need to search.
AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=users,dc=example,dc=com"

# You can map user attributes to Django attributes as so.
AUTH_LDAP_USER_ATTR_MAP = {
        "first_name": "givenName",
        "last_name": "sn",
        "email": "mail"
}
# This search ought to return all groups to which the user belongs.
# django_auth_ldap uses this to determine group heirarchy.
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("dc=example,dc=com", ldap.SCOPE_SUBTREE,
                                   "(objectClass=group)")
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()

# Define a group required to login.
AUTH_LDAP_REQUIRE_GROUP = "CN=NETBOX_USERS,DC=example,DC=com"

# Define special user types using groups. Exercise great caution when assigning
# superuser status.
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
        "is_active": "cn=active,ou=groups,dc=example,dc=com",
        "is_staff": "cn=staff,ou=groups,dc=example,dc=com",
        "is_superuser": "cn=superuser,ou=groups,dc=example,dc=com"
}
# For more granular permissions, we can map LDAP groups to Django groups.
AUTH_LDAP_FIND_GROUP_PERMS = True

# Cache groups for one hour to reduce LDAP traffic
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600
