This repository contains quick and dirty tools to look at the Shadowrun Return *.bytes files.

The proto directory contains the isogame.proto file, aswell as some of the default google protobuf definitions.

The src directory, at the moment contains only isogame_pb2.py, show_item.py and show_character_instance.py which just show the plaintext for this type of serialized messages.

The file isogame_pb2.py is a python library that allows you to read any of the *.bytes files, provided you know its type.

In order to use this scripts you will have to have google protobuf installed.

    pip install protobuf

