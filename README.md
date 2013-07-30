This repository contains quick and dirty tools to look at the Shadowrun Return *.bytes files.

The proto directory contains the isogame.proto file, aswell as some of the default google protobuf definitions.

The src directory, at the moment contains only isogame_pb2.py, show_item.py and show_character_instance.py which just show the plaintext for this type of serialized messages.

In order to use this you will have to have google protobuf installed.

    pip install protobuf

The file isogame_pb2.py is a python library that allows you to read and write any of the *.bytes files, provided you know its type.

Reading a bytes file works something like this:

    import isogame_pb2 as isogame

    i = isogame.CharacterInstance()
    i.ParseFromString(open('/path/to/chars/bla.ch_inst.bytes").read())

And Writing works like this:
    with open('/path/to/whatever/filename.bytes', 'wb') as f:    
	f.write(i.SerializeToString())


