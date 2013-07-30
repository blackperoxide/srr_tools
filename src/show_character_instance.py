import sys
sys.path.append('./protobuf-2.5.0-py2.7.egg')
import isogame_pb2 as isogame
from google.protobuf.text_format import MessageToString

if __name__ == '__main__':
    path = sys.argv[1]
    i = isogame.CharacterInstance()
    i.ParseFromString(file(path, 'rb').read())
    print MessageToString(i)
