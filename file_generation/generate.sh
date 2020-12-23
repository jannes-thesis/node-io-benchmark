#!/bin/bash
for i in {1..200}
do
    # 50mb file
    head -c 52428800 </dev/urandom >/mnt/hdd/files/file$i
done
