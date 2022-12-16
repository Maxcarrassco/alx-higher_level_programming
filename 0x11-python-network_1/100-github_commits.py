#!/usr/bin/python3
"""Request ALX SE MOdule."""
import requests
import sys


def main() -> None:
    """Print all commits by: `<sha>: <author name>` (one by line)."""
    user = sys.argv[2]
    repo = sys.argv[1]
    url = f'https://api.github.com/repos/{user}/{repo}/commits'
    res = requests.get(url)
    objs = res.json()

    for obj in objs:
        commit = obj['commit']
        committer = commit['committer']
        print(f"{obj.get('sha')}:", committer.get('name'))


if __name__ == '__main__':
    main()