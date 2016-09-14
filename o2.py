from itertools import chain
from hashlib import sha256
from lsm import LSM


def checksum(filename, blocksize=65536):
    hasher = sha256()
    with open(filename, 'rb') as fp:
        while True:
            chunk = fp.read(blocksize)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.digest()


class Index(object):
    def __init__(self, db_path):
        self.db = LSM(db_path)

    def has_changed(self, path):
        return self.db[path] != checksum(path)

    def update(self, files=()):
        with self.db.transaction() as txn:
            for path in files:
                self.db[path] = checksum(path)

    def __iter__(self):
        return iter(self.db.keys())

    @property
    def changed(self):
        return [path for path in self if self.has_changed(path)]
