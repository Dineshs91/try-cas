import argparse

from api.api import API


parser = argparse.ArgumentParser(description="content addressable storage")
parser.add_argument('action', nargs=1, help='cas store <content>')
parser.add_argument('content', nargs='?', help='cas fetch <sha>')
parser.add_argument('-f', help='store content of a file')

args = parser.parse_args()

action = args.action[0]

content = args.content

api = API()

if action == 'store' and args.f:
    file = args.f
    with open(file, 'r+') as f:
        content = f.read()
    sha = api.store(content.encode('utf-8'))
    print(sha)
elif action == 'store':
    sha = api.store(content.encode('utf-8'))
    print(sha)
elif action == 'fetch':
    print(content)
    data = api.fetch(content)
    print(data.decode('utf-8'))
