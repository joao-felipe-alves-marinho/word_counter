SUPPORTED_FILES_TYPES = [('Txt files', '*.txt'),
                         ('Doc files', '*.docx'),
                         ('Pdf files', '*.pdf')]

ALL_FILES_TYPES = [('All supported files', '; '.join(y for x, y in SUPPORTED_FILES_TYPES))]

VALID_FILES_TYPES = ALL_FILES_TYPES + SUPPORTED_FILES_TYPES
