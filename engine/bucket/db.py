""" An interface to the embedded database
"""
import util

class BucketDBExcception(Exception):
    
    def __init__(self, message):
        Exception.__init__(self, message)


class BucketDB:

    "The file itself"
    databse_file = None

    "The handle on the database"
    cursor = None

    def __init__(self, database_file):
        self.database_file = database_file
    
    def addEpisode(self, eid, published, title):
        """ Add an episode to the databse
        """
        title = util.defaultTo(title, eid)
        pass

    def markRead(self, eid):
        """ Mark an episode as read
        """
        pass

    def open(self):
        """ Open a cursor to the databse

        If the database does not have the table, bootstrap it.
        """
        pass

    def close(self):
        """ Close the cursor

        Throws an SQLite error if the cursor could not be closed
        """
        self.cursor.close()
        self.cursor = None
