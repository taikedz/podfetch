import os

import util.feedback as out
import buckets.db
import

""" Podcast bucket initializer

Initializes a new podcast bucket which will contain

* Database file
* Preferences file
* Individual podcast assets
"""

def newBucket(directory, url):
    # FIXME - check the arguments
    os.mkdir(directory)

    __createBucketDatabse(directory, url)

    __createBucketPreferences(directory, url)

def __createBucketDatabse(directory, url):
    db = buckets.db.BucketDB( os.path.sep.join([directory, "episodes.db"]) )
    db.open()
    db.close()

def __createBucketPreferences(directory, url):
    # TODO at this point, we need to know or be able to extract info from the URL

    prefs = buckets.prefs.BucketPreferences()
    prefs.open()
