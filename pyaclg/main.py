from git import Repo


def main():
    repo = Repo()
    commits = repo.iter_commits('master')
    for commit in commits:
        print(commit.message)


if __name__ == '__main__':
    main()
