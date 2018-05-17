
class ConsoleOutput(object):

    def write(self, summaries):
        print('\n'.join(summaries))


class FileOutput(object):

    def __init__(self, path):
        self.path = path

    def write(self, summaries):
        with open(self.path, 'w') as output:
            output.write('\n'.join(summaries))
