#!/bin/sh -ex

black app tests scripts
ruff check app tests scripts --fix
