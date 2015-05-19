#!/usr/bin/make -f

NAME=flysatellite

all: clean package

package:
	fpm -s python -t deb -a amd64 -d python \
        -x '**/*.py' -x '**/test' -x '**/tests' \
        --python-package-name-prefix fs \
        setup.py

clean:
	rm -rf dist build fs-$(NAME)*.deb usr *.egg-info

