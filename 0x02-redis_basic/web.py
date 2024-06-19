#!/usr/bin/env python3
""" Module for caching and counting requests with Redis """

from functools import wraps
import redis
import requests
from typing import Callable

redis_ = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ Decorator that counts how many times a
    URL is accessed and caches the result """
    @wraps(method)
    def wrapper(url):  # sourcery skip: use-named-expression
        """ Wrapper function that increments the
        count and caches the result """
        redis_.incr(f"count:{url}")
        cached_html = redis_.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        redis_.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ Fetches the content of a URL """
    req = requests.get(url)
    return req.text
