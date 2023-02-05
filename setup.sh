#!/bin/bash

if [ ! -d "~/.env" ] 
then
  python -m venv .env
  echo "venv already exists"
fi
source .env/bin/activate
python -m pip install -r requirements.txt


rm -rf ./dist
rm -rf ./build

pyinstaller --onefile youtube-dl.py
cp ./dist/youtube-dl ~/.local/bin/
exec zsh

rm -rf ./dist
rm -rf ./build

