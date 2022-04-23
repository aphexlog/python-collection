import git

repo = git.Repo("./automatic-disco")
# print(repo.git.status())
# print(repo.git.log())

# print git logs for all commits with a certain tag
print(repo.git.log('--pretty=%H', '--grep=tag:v1'))
