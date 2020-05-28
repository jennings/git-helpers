# git-helpers

Helper scripts used by my `.gitconfig`.

## git-upstream-url

Creates a URL for interacting with Git hosting providers.

```bash
# Get the main repository URL

> git-upstream-url repo --remote git@github.com:jennings/git-helpers
https://github.com/jennings/git-helpers

> git-upstream-url repo --remote $(git config remote.origin.url)
https://github.com/jennings/git-helpers


# Get a URL for opening a pull request

> git-upstream-url new-pr --remote $(git config remote.origin.url) --branch $(git rev-parse --abbrev-ref HEAD)
https://github.com/jennings/git-helpers/pull/new/my-current-branch
```
