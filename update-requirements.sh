#!/usr/bin/env bash

set -o pipefail

fatal()
{
    echo -e "\033[31m${BASH_SOURCE}: fatal:\033[0m" $@ >&2
    exit 1
}

declare -r REQUIREMENTS_FILE="${1:-$(dirname $BASH_SOURCE)/requirements.txt}"
for req in $(grep -oP '^[^=]+' "$REQUIREMENTS_FILE"); do
    # echo $req:
    version="$(pip freeze | grep -iP "${req//[^[:alnum:]]/.}[<=>]" | grep -oP '[^<=>]+$')" || fatal Failed getting $req\'s version >&2
    sed -i "s/${req}.*/${req}==${version}/" "$REQUIREMENTS_FILE" || fatal Failed updating $req to $version in '$REQUIREMENTS_FILE'
done
