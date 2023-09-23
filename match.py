#!/usr/bin/python3
# -*- coding: utf-8 -*-

def http_error(status):
    match status:
        case 400:
            return "End request"
        case 401 | 403:
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I am a teapot"
        case _:
            return "The internet is broken"
