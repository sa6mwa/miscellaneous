#!/bin/bash
for i in *; do echo mv "$i" "$(echo "$i" | sed 's/[<>:"\/\\|?*]//g')" ; done
