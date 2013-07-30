This repository contains quick and dirty tools to look at the Shadowrun Return *.bytes files.

The proto directory contains the isogame.proto file, aswell as some of the default google protobuf definitions.

The src directory contains two sample scripts, show_item.py and show_character_instance.py aswell as the generated protobuf library isogame_pb2.py and the protobuf egg file.
Because of the egg, the sample scripts should be able to run with just a clean python installation.

The file isogame_pb2.py is a python library that allows you to read and write any of the *.bytes files, provided you know its type.

Reading a bytes file works something like this:

    import isogame_pb2 as isogame

    i = isogame.CharacterInstance()
    i.ParseFromString(open('/path/to/chars/bla.ch_inst.bytes").read())

And Writing works like this:

    f = open('/path/to/whatever/filename.bytes', 'wb')
    f.write(i.SerializeToString())
    f.close()


