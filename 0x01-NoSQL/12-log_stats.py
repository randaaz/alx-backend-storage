#!/usr/bin/env python3
""" MongoDB Utility Functions """


def schools_by_topic(mongo_collection, topic):
    """ Connect to MongoDB and return a collection object. """
    documents = mongo_collection.find({"topics": topic})
    return list(documents)
