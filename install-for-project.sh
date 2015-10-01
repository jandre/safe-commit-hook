#!/bin/bash

cp ~/.safe-commit-hook/safe-commit-hook.py .git/hooks/pre-commit
echo "[-] Installed git safe commit hook. You will not be able to commit suspicious files."
