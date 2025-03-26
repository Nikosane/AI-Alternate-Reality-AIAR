import logging

class Logger:
    def __init__(self, log_file='simulation.log'):
        self.logger = logging.getLogger('AIAR Logger')
        self.logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)

    def log(self, message, level='info'):
        if level == 'info':
            self.logger.info(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        else:
            self.logger.debug(message)

# Example usage
if __name__ == "__main__":
    logger = Logger()
    logger.log("Simulation started.")
    logger.log("An unexpected behavior occurred.", level='warning')
