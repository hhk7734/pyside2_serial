#!/bin/sh

RED=$(tput setaf 1)
BOLD=$(tput bold)
DEFAULT=$(tput sgr0)

SCRIPT_PATH=$(dirname $(realpath $0))

helpMsg() {
    cat <<END
Usage:
    $(basename "$0") [options] [arguments]
Options:
    -h | --help
    --uic
Examples:
END
}

if [ $# -eq 0 ] || ! options=$(getopt -o ih -l install,help,uic \
    -n $(basename "$0") -- "$@"); then
    printf "%sTry '%s --help'\n%s" "${RED}${BOLD}" "$0" "${DEFAULT}" >&2
    exit 1
fi

eval set -- "$options"

while true; do
    case "$1" in
    --uic)
        pyside2-uic \
            $SCRIPT_PATH/py_src/pyside2_serial/main_window/main_window.ui \
            -o $SCRIPT_PATH/py_src/pyside2_serial/main_window/ui_main_window.py
        shift
        ;;
    -h | --help)
        helpMsg
        exit 0
        ;;
    --)
        shift
        break
        ;;
    esac
done

echo "$@"
