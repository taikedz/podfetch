#!/usr/bin/env python3

import sys
import feedback

def main(args):
    action = args[0]

    if action == "pref":
        prefs.processAll(args[1:])

    elif action == "init":
        init.new(args[1:])

    elif action == "download":
        download.fetchAll(args[1:])

    elif action == "mark":
        manage.markAll(args[1:])

    elif action == "list":
        listing.listInfoFor(args[1:])

    else:
        feedback.fail("Not a recognized command")

if __name__ == '__main__':
    return main(sys.argv[1:])
