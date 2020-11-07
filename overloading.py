from typing import Optional


def get_filepath_from_filename(filename: str) -> str:
    return "path/{}".format(filename)


class UsefulClass:

    def save(self, filepath: Optional[str] = None, filename: Optional[str] = None):
        # Check filename and filepath have not both been provided at the same time;
        if filename is None and filepath is None:
            raise Exception('Invalid params.')
        # If we got a filename, then turn it into a filepath;
        if filename is not None:
            filepath = get_filepath_from_filename(filename)

        # Now do something with filepath...
