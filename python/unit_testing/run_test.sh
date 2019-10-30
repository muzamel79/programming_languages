#!/bin/bash

PYTHONPATH="$(git rev-parse --show-toplevel)/python"
export PYTHONPATH

function print_help()
{
    echo "Usage:"
    echo '    run_test.sh                       Run all the tests'
    echo '    run_test.sh -f <test file path>   Run a specific test file'
    echo '    run_test.sh -h                    Display this help message.'
}

target=''
while getopts 'hf:' opt; do
    case "${opt}" in
        h )
            print_help
            exit 0
            ;;
        f )
            target="${OPTARG}"
            break
            ;;
        : )
            echo "Invalid Option: -${OPTARG} requires a file name argument" 1>&2
            exit 1
            ;;
        \? )
            echo "Invalid Option: -${OPTARG}" 1>&2
            print_help
            exit 1
            ;;
    esac
done

if [ -z "${target}" ] ; then
    find "${PYTHONPATH}/unit_testing/" -type f -name 'test_*\.py' -exec pytest {} \;
else
    pytest "${target}"
fi
