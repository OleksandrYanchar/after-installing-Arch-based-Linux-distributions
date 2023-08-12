#!/bin/bash
sudo pacman -S docker
sudo systemctl start docker
sudo systemctl enable docker
