from itertools import chain
from hashlib import sha256
from lsm import LSM


def checksum(filename, blocksize=65536):
    hasher = sha256()
    with open(filename, 'rb') as fp:
        chunks = iter(
                lambda: fp.read(blocksize),
                bytes(),
                )
        for chunk in chunks:
            hasher.update(chunk)
    return hasher.digest()


class Index(object):
    def __init__(self, db_path):
        self.db = LSM(db_path)

    def has_changed(self, path):
        return self.db[path] != checksum(path)

    def index(self, files=()):
        with self.db.transaction() as txn:
            for path in chain(self.files, files):
                self.db[path] = checksum(path)

    @property
    def files(self):
        return set(self.db.keys())

    @property
    def changed(self):
        return set(path for path in self.files if self.has_changed(path))
