from git import Repo
from click import command, option

from pyaclg.output import FileOutput, ConsoleOutput


FILE_HELP = 'Write down the specified file in the current path'


@command()
@option('--path', '-p', help=FILE_HELP)
def main(path):
    repo = Repo()
    commits = repo.iter_commits('master')
    summaries = [commit.summary for commit in commits]

    if path is not None:
        output = FileOutput(path)
    else:
        output = ConsoleOutput()

    output.write(summaries)
