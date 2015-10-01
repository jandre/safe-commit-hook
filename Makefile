install:
	mkdir -p ~/.safe-commit-hook
	cp -r * ~/.safe-commit-hook
	git config --global alias.init-safe-commit '!~/.safe-commit-hook/install-for-project.sh'
