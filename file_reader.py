class FileReader:
    def __init__(self, path: str):
        self.path = path
        self.file = self.read_file()

    def read_file(self):
        """ Reads the File """
        read_file = open(self.path, 'r', encoding='UTF-8')
        file = read_file.read().replace('\n', '')
        read_file.close()
        return file

    def count_words(self):
        """ Counts the characters of the file """
        return len(self.file)
