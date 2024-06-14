#!/usr/bin/env python3
""" MongoDB Utility Functions """


def insert_school(mongo_collection, **kwargs):
    """ Insert a document into a MongoDB collection. """
    return mongo_collection.insert(kwargs)
