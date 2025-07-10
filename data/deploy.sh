#!/bin/bash

set -e  # Stop on error

echo "Pulling latest changes..."
git pull origin main  # Adjust branch name if necessary

echo "Running script to generate SUMMARY.md..."
python3 script.py  # Update based on your actual script

echo "Building mdBook..."
mdbook build

echo "Restarting mdBook service..."
systemctl restart mdbook.service

