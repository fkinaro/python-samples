#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Sample collection
users = {'Hans': 'active', 'Elenore': 'inactive', 'Peter': 'active'}

# Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
