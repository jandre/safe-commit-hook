# Safe Commit Hook

This is a git [pre-commit hook](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) that is inspired by the [Gitrob project](https://github.com/michenriksen/gitrob).

It adds an automatic check to prevent developers from checking in suspicious files (as defined by Gitrob's [signatures.json](https://github.com/michenriksen/gitrob/blob/master/signatures.json))

# Installation

```bash
git clone https://github.com/jandre/safe-commit-hook.git 
cd safe-commit-hook
make install  
```

This will do the following:

 * Create a `~/.safe-commit-hook` directory and copy the files from this repo there.
 * Create a git alias so you can do `git init-safe-commit` in a project directory, which will create `.git/hooks/pre-commit` (WARNING: will blow away
any other pre-commit hooks).

Now you will get an error if you try to do anything fishy!

[![asciicast](https://asciinema.org/a/0uqf6dcaautz599xru1kefa6b.png)](https://asciinema.org/a/0uqf6dcaautz599xru1kefa6b)

# Editing the rules

They are currently in JSON format at `~/.safe-commit-hook/git-deny-patterns.json`.

Just remove the rules you wish to ignore. In the future, would nice to have a `.git-safe-commit-ignore` file for a repo. 

# TODO

 * [ ] Allow project specific exceptions for safe commit checks.
 * [ ] Don't blow away any other git pre-commit hooks in `git init-safe-commit`.
 * [ ] Extend the JSON spec to allow for searching for body of modified files.
