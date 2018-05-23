#!/usr/bin/env python3

import sys
import feedback
import testing

import init
import prefs
import download
import manage
import listing

def main(args):

    if len(args) < 1:
        feedback.fail("No arguments supplied")

    action = args[0]

    if action == "init":
        init.new(args[1:])

    elif action == "pref":
        prefs.processAll(args[1:])

    elif action == "download":
        download.fetchAll(args[1:])

    elif action == "mark":
        manage.markAll(args[1:])

    elif action == "list":
        listing.listInfoFor(args[1:])

    elif action == "test":
        testing.testModule(args[1:])

    else:
        feedback.fail("Not a recognized command")

if __name__ == '__main__':
    main(sys.argv[1:])
