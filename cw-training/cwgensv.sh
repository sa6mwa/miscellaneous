#!/bin/sh
cwgen -c 'ABCDEFGHIJKLMNOPQRSTUVWXYZaeo0123456789' $* | sed 's/a/Å/g; s/e/Ä/g; s/o/Ö/g'
