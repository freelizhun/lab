#!/usr/bin/make -f

NAME=flysatellite

all: clean package

package:
	fpm -s python -t deb -a amd64 -d python \
        -x '**/*.py' -x '**/test' -x '**/tests' \
	-x 'upstart/*'\
        setup.py

clean:
	rm -rf dist build $(NAME)*.deb usr *.egg-info


