class Logger():

    def __init__(self, filename):
        self.filename = filename

    def _write_log(self, level, msg):
        with open(self.filename, "a") as log_file:
            log_file.write("[{}] {}\n".format(level, msg))


    def critical(self, msg):
        self._write_log("CRITICAL", msg)

    def error(self, msg):
        self._write_log("ERROR", msg)

    def warning(self, msg):
        self._write_log("WARNING", msg)

    def info(self, msg):
        self._write_log("INFO", msg)

    def debug(self, msg):
        self._write_log("DEBUG", msg)
