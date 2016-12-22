import os


class FileSystem:
    def __init__(self):
        self.cas_dir = "/Users/dinesh/Documents/developer/cas/.cas"

    def _create_dir(self, dirname):
        """
        Create the directory in objects directory. The name is the
        first 2 chars of the sha of the content + header.
        """
        object_dir_path = os.path.join(self.cas_dir, 'objects', dirname)

        # Check if directory exists.
        if not os.path.exists(object_dir_path):
            os.makedirs(object_dir_path)

    def get_file_and_dir_name(self, sha):
        dirname = sha[:2]
        filename = sha[2:40]

        return dirname, filename

    def get_file_path(self, dirname, filename):
        file_path = os.path.join(self.cas_dir, 'objects', dirname,
                                 filename)

        return file_path

    def write(self, sha, content):
        """
        Write the zlib compressed data to the given file.
        """
        dirname, filename = self.get_file_and_dir_name(sha)
        self._create_dir(dirname)
        file_path = self.get_file_path(dirname, filename)

        with open(file_path, 'wb') as f:
            f.write(content)

    def read(self, sha):
        dirname, filename = self.get_file_and_dir_name(sha)
        file_path = self.get_file_path(dirname, filename)

        if not os.path.exists(file_path):
            return None

        with open(file_path, 'rb') as f:
            content = f.read()

        return content
