#!/bin/bash
echo "1. build web html"
gitbook build
echo "2. sync files to cos"
#cp -R _book/* /var/web/bytetoy
coscli sync ~/web/bytetoy/_book/ cos://bytetoy/ -r
