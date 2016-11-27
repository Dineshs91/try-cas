import zlib
import hashlib

from core.filesystem import FileSystem
from exceptions import ContentNotFoundError


class API:
    def __init__(self):
        self.compress_level = 3
        self.file_system = FileSystem()

    def store(self, content):
        """
        1. Generate hash from content.
        2. Generate zlib defalte from content.
        """
        sha = self._generate_hash(content)
        deflated_content = self._compress(content)

        self.file_system.write(sha, deflated_content)

        return sha

    def _generate_hash(self, content):
        return hashlib.sha1(content).hexdigest()

    def _compress(self, content):
        return zlib.compress(content, self.compress_level)

    def _decompress(self, content):
        return zlib.decompress(content)

    def fetch(self, sha):
        """
        Get the content from the hash.
        """
        compressed_content = self.file_system.read(sha)
        if compressed_content is None:
            raise ContentNotFoundError("Content not found")
        content = self._decompress(compressed_content)

        return content
