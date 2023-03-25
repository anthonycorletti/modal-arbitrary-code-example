#!/bin/sh -ex

mypy app tests
black app tests --check
ruff app tests scripts
