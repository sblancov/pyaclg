from git import Repo
from click import command


@command()
def main():
    repo = Repo()
    commits = repo.iter_commits('master')
    for commit in commits:
        print(commit.summary)


if __name__ == '__main__':
    main()
