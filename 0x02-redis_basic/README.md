# 0x02. Redis Basic

## Back-end | Redis

### Learning Objectives
- Understand how to use Redis for basic operations.
- Learn to use Redis as a simple cache.

### Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- The first line of all your files should be `#!/usr/bin/env python3`.
- Code must adhere to the pycodestyle style (version 2.5).
- All modules, classes, functions, and methods should have proper documentation.
- Functions and coroutines must be type-annotated.

### Installation Instructions

#### Install Redis on Ubuntu 18.04
```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf

