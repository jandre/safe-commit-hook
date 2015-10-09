#!/bin/bash

srcFile="$HOME/.safe-commit-hook/safe-commit-hook.py"
dstFile=".git/hooks/pre-commit"

function combineHooks() {
    local hookCmd="\nexec ${dstFile}_safe\n"

    if [[ $(tail -n 3 ${dstFile}) =~ ${dstFile} ]]; then
        echo "[!] safe commit hook is already installed."
        exit
    fi

    # if "exit" exists, prepend `hookCmd` before it.
    if [[ $(tail -n 1 ${dstFile}) =~ "exit".* ]]; then
        sed --in-place=".bak-$(date +%s)" '$ i \ '"${hookCmd}"'' "${dstFile}"
    else
        echo -e "${hookCmd}" >> "${dstFile}"
    fi
}

if [[ ! -e "${dstFile}" ]]; then
    cp "${srcFile}" "${dstFile}"
else
    cp "${srcFile}" "${dstFile}_safe"
    combineHooks
fi

echo "[-] Installed git safe commit hook. You will not be able to commit suspicious files."
