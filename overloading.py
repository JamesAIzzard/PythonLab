from typing import Optional


def get_filepath_from_filename(filename: str) -> str:
    return "path/{}".format(filename)


class UsefulClass:

    def save(self, filepath: Optional[str] = None, filename: Optional[str] = None):
        if filename is None and filepath is None:
            raise Exception('Invalid params.')
        if filename is not None:
            filepath = get_filepath_from_filename(filename)

        # Do something with filepath...
