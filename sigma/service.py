import config


class ITerminal(object):

    def __init__(self):
        self._argparse = __import__("argparse")

        self._parser = self._argparse.ArgumentParser(description="Sigma")

        self._parser.add_argument("-m", "--modifier", 
                nargs="+", 
                type=str,
                choises=config.modifiers, 
                help="data modifier stack")

        self._parser.add_argument("-f", "--filter", 
                nargs="+", 
                type=str,
                choises=config.filters, 
                help="data filter stack")

        self._parser.add_argument("-c", "--creator", 
                nargs=1,
                type=str,
                choices=config.creators,
                help="creator on data")

        self._parser.add_argument("-i", "--infile", 
                nargs="?",
                default=config.data_filename,
                type=argparse.FileType("r"),
                help="raw data file")

        self._args = self._parser.parse_args()


class IGUI(object):
    pass


class IMatplotlib(object):
    pass


class IRhino(object):
    pass


class IBlender(object):
    pass


class IDatabase(object):
    pass


class IFilesystem(object):
    pass
