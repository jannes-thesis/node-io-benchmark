#!/bin/bash
for i in {1..20}
do
    # 50mb file
    head -c 52428800 </dev/urandom >files/file$i
done
