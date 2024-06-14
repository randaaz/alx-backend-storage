#!/usr/bin/env python3
""" MongoDB Utility Functions """


def top_students(mongo_collection):
    # sourcery skip: inline-immediately-returned-variable
    """ Connect to MongoDB and return a collection object. """
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student
