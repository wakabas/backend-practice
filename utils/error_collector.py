from logger.logger import log


class ErrorCollector:

    def __init__(self):
        self.errors = []

    def check(self, assert_condition: bool, message: str = None):
        try:
            assert assert_condition
        except AssertionError:
            self.errors.append(message or "Failed to assert!")

    def verify_all_errors(self):
        if self.errors:
            failure_lines = [f"[{index}] {error}" for index, error in enumerate(self.errors, start=1)]
            report = f'Failed assertions count: [{len(self.errors)}]\n' + '\n'.join(failure_lines)
            self.errors = []
            log.info(report)
            raise AssertionError(report)
