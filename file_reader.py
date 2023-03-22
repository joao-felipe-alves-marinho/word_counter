import pathlib
from docx import Document


class FileReader:
    def __init__(self, path: str):
        self.path = path
        self.file_type = self._get_file_extension()
        self.file = self._read_file()

    def _get_file_extension(self):
        """ Returns the file type """
        return pathlib.Path(self.path).suffix

    def _read_file(self):
        """ Reads the File based on the type of the file """
        if self.file_type == '.txt':
            return self._read_txt_file()
        elif self.file_type == '.docx':
            return self._read_docx_file()

    def count_words(self):
        """ Counts the characters of the file """
        return len(self.file.replace('\n', ''))

    def _read_txt_file(self):
        """ Reads txt files  """
        with open(self.path, 'r', encoding='utf-8') as file:
            return file.read()

    def _read_docx_file(self):
        """ Reads docx files """
        doc = Document(self.path)
        fulltext = []
        for p in doc.paragraphs:
            fulltext.append(p.text)
        return '\n'.join(fulltext)
