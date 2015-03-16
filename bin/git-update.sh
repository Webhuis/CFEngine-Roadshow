#!/bin/bash

for i in ` git status | grep deleted | awk '{print $3}' ` ; do git rm $i; done
for i in ` git status | grep modified | awk '{print $3}' ` ; do git add $i; done

