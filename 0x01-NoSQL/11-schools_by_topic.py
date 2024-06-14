#!/usr/bin/env python3
""" MongoDB Utility Functions """


def schools_by_topic(mongo_collection, topic):
    """ Retrieve schools from a MongoDB collection based on a specific topic. """
    documents = mongo_collection.find({"topics": topic})
    return list(documents)
