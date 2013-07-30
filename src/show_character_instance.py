import isogame_pb2 as isogame
from google.protobuf.text_format import MessageToString
import sys

if __name__ == '__main__':
    path = sys.argv[1]
    i = isogame.CharacterInstance()
    i.ParseFromString(file(path, 'rb').read())
    print MessageToString(i)
