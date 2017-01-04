## Commands

`cas store <content>`

`cas fetch <sha>`

To store content from a file.
`cas store -f <filename>`

Supports fetch from short sha's also instead of the complete sha.
This will work only if there is no collision.

Requires atleast 5 characters of sha.

## Features

- [x] Store content in sha (First 2 chars - directory, remaining file name)
- [x] Support fetching content with just 5 chars of sha.
- [x] Store the content of a file, by providing the file path.
