#!/usr/bin/env python3
""" MongoDB Utility Functions """


def list_all(mongo_collection):
    """ Retrieve all documents from a MongoDB collection. """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
