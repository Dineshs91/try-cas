import os
import sys


class FileSystem:
    def __init__(self):
        self.cas_dir = os.path.join(os.getcwd(), ".cas")

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
        filename = sha[2:]

        return dirname, filename

    def get_file_and_dir_name_smart(self, sha):
        dirname = sha[:2]
        filename = sha[2:]

        # Go through all files to see how many matches can be found
        # for filename. If only one is found, return.
        # Else raise exception.
        complete_filename = self.search_file(dirname, filename)
        return dirname, complete_filename

    def search_file(self, dirname, filename):
        count = 0

        files = os.listdir(os.path.join(self.cas_dir, 'objects', dirname))
        complete_filename = ''

        for f in files:
            if f[0:len(filename)] == filename:
                complete_filename = f
                count += 1

        if count > 1:
            print("Multiple files found")
        elif count == 0:
            print("Unable to find the content")
        return complete_filename

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
        """
        Support fetch using just 5 chars from sha
        """
        sha_length = len(sha)
        if sha_length < 5:
            print('Not enough sha chars to fetch content')
            sys.exit(1)
        if sha_length != 40:
            dirname, filename = self.get_file_and_dir_name_smart(sha)
        else:
            dirname, filename = self.get_file_and_dir_name(sha)
        file_path = self.get_file_path(dirname, filename)

        if not os.path.exists(file_path):
            return None

        with open(file_path, 'rb') as f:
            content = f.read()

        return content
