#!/bin/bash

echo "great"

touch something

test -e something || echo "pregnent sir"

test -e notafile || echo "not pregnent sir"
