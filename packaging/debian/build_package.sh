#! /usr/bin/env sh

SCRIPT_DIRECTORY="$(dirname -- "$(readlink -f -- "$0")")"
PROJECT_DIRECTORY="$(dirname -- "$(dirname -- "$SCRIPT_DIRECTORY")")"
BUILD_DIRECTORY="$PROJECT_DIRECTORY"/build
PACKAGE_DIRECTORY_STUB="python3-pysetting"
MODE="$(echo "$1" | tr "[:upper:]" "[:lower:]")"
if [ "$MODE" != "stable" ] && [ "$MODE" != "local" ]; then
    echo ""
    echo "ERROR: Please specify \"stable\", or \"local\" as the first argument to this script, to indicate the mode to run this script in."
    exit 1
fi
shift 1
if [ "$MODE" != "stable" ]; then
    PACKAGE_DIRECTORY_STUB="$PACKAGE_DIRECTORY_STUB-$MODE"
fi
PACKAGE_DIRECTORY="$SCRIPT_DIRECTORY/$PACKAGE_DIRECTORY_STUB"
if [ "$MODE" != "local" ]; then

    ( # Create subshell to nullify directory changes on exit
        # Run makepkg
        set -o xtrace
        cd "$PACKAGE_DIRECTORY" && \
        make deb 
        set +o xtrace
    )
else
    ( # Create subshell to nullify directory changes on exit
        # Run makepkg
        set -o xtrace
        cd "$PACKAGE_DIRECTORY" && \
        make deb 
        set +o xtrace
    )
fi

