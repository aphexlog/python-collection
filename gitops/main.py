import git

repo = git.Repo("./flask-empty")
# print(repo.git.status())
# print(repo.git.log())

# print git logs for all commits with a certain tag
# print(repo.git.log('--pretty={"tags":"%t","message":"%s"}', '--all'))

# WORKS
# commits = repo.iter_commits('--all', )
# for commit in commits:
#     print(commit, commit.message
# 
#    # print(commit.message)
#    # print(commit.tags)
#    # print(commit.tree)
#    # print(commit.parents)
#    # print(commit.stats)
#    # print(commit.author)
#    # print(commit.committed_date)
#    # print(commit.authored_date)
#    # print(commit.hexsha)
#    # print(commit.name_rev)
#    # print(commit.summary)
#    # print(commit.message_short)
#    # print(commit.message_long)
#    # print(commit.raw_body)
#    # print(commit.diff)
#    # print(commit.diff.stats)
#    # print(commit.diff.files)
#    # print(commit.diff.iter_change_type('A'))
#    # print(commit.diff.iter_change_type('M'))


print(repo.tag('0.5.2').commit)
