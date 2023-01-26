#!/bin/bash

rm -rf ./dist
rm -rf ./build

pyinstaller --onefile youtube-dl.py
cp ./dist/youtube-dl ~/.local/bin/
exec zsh

rm -rf ./dist
rm -rf ./build
