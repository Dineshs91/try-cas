import argparse

from api.api import API


parser = argparse.ArgumentParser(description="content addressable storage")
parser.add_argument('action', nargs=1, help='cas store <content>')
parser.add_argument('content', nargs=1, help='cas fetch <sha>')

args = parser.parse_args()

action = args.action[0]
content = args.content[0]

api = API()

if action == 'store':
    sha = api.store(content.encode('utf-8'))
    print(sha)
elif action == 'fetch':
    data = api.fetch(content)
    print(data.decode('utf-8'))
