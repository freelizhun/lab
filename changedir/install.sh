#!/usr/bin/env bash
CWD=`pwd`
SCRIPT_DIR=`dirname $0`
echo $CWD
echo $SCRIPT_DIR
$CWD/a/test.sh
$CWD/b/test.sh
echo $CWD
