#!/usr/bin/env python3
""" MongoDB Utility Functions """


def update_topics(mongo_collection, name, topics):
    """ Update topics of documents in a MongoDB collection based on name. """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, new_values)
