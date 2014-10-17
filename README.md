kinetic
=======

A codebase for working with Seagate Kinetic Internet Protocol (IP)  Hard Disk Drives (HDDs)

## Dependencies ##

This code requires the kinetic Python module. You can either install is from seagate/kinetic-py or use my docker container sbates130272/kinetic-py in interactive mode. Note this image also pulls this github repo.

## Usage ##

For initial usage try running `python test/simple.py -i <IP> -p <PORT>` where `<IP>` and `<PORT>` point to a Kinetic IP HDD (or the simulator of such a drive).
