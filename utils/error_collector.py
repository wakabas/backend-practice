from logger.logger import log


class ErrorCollector:

    def __init__(self):
        self.errors: list[AssertionError] = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is AssertionError:
            self.errors.append(exc_val)
            return True

        return False

    def verify_all_errors(self):
        if self.errors:
            message = (f'List of occurred errors:\n'
                       f'{"\n".join([str(err) for err in self.errors])}')
            log.info(message)
            raise AssertionError(message)
