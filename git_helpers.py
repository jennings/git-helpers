import re
import sys

def get_base_url(remote):
    if remote.startswith("git@github.com:"):
        match = re.search(r"^git@github.com:(.+)/(.*?)(?:\.git)?(/|$)", remote)
        if not match: sys.exit(f"did not match GitHub SSH remote: {remote}")
        return f"https://github.com/{match.group(1)}/{match.group(2)}", "github"

    elif remote.startswith("git@bitbucket.org:"):
        match = re.search(r"^git@bitbucket.org:(.+)/(.*?)(?:\.git)?(/|$)", remote)
        if not match: sys.exit(f"did not match Bitbucket SSH remote: {remote}")
        return f"https://bitbucket.org/{match.group(1)}/{match.group(2)}", "bitbucket"

    elif remote.startswith("https://github.com/"):
        match = re.search(r"^https://github.com/(.+)/(.*?)(?:\.git)?(/|$)", remote)
        if not match: sys.exit(f"did not match GitHub HTTPS remote: {remote}")
        return f"https://github.com/{match.group(1)}/{match.group(2)}", "github"

    elif remote.startswith("https://bitbucket.org/"):
        match = re.search(r"^https://bitbucket.org/(.+)/(.*?)(?:\.git)?(/|$)", remote)
        if not match: sys.exit(f"did not match Bitbucket HTTPS remote: {remote}")
        return f"https://bitbucket.org/{match.group(1)}/{match.group(2)}", "bitbucket"

    else:
        sys.exit(f"unknown URL format: {remote}")
