import tensorflow as tf
import subprocess
import shutil
import logging

logger = logging.getLogger(__name__)


class Formatter(logging.Formatter):
    GREY = "\x1b[38;20m"
    YELLOW = "\x1b[33;20m"
    RED = "\x1b[31;20m"
    GREEN = "\033[92m"
    BOLD_RED = "\x1b[31;1m"
    RESET = "\x1b[0m"
    FORMATS = {
        logging.DEBUG: GREY + "[%(levelname)s] %(asctime)s %(message)s" + RESET,
        logging.INFO: GREEN + "[%(levelname)s]" + RESET + " %(asctime)s %(message)s",
        logging.WARNING: YELLOW
        + "[%(levelname)s]"
        + RESET
        + " %(asctime)s %(message)s",
        logging.ERROR: RED + "[%(levelname)s] %(asctime)s %(message)s" + RESET,
        logging.CRITICAL: BOLD_RED + "[%(levelname)s] %(asctime)s %(message)s" + RESET,
    }

    def format(self, record):
        log_format = Formatter.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_format)
        return formatter.format(record)


def set_logger():
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(Formatter())
    logger.addHandler(stream_handler)


def log_version_and_gpu():
    logger.info("*" * 50)
    logger.info(f"Tensorflow version: {tf.__version__}")
    logger.info(f"Number of GPUs: {len(tf.config.list_physical_devices('GPU'))}")
    logger.info("*" * 50)


def set_log_placements():
    logger.info("*" * 50)
    logger.info("Log Placement Details")
    logger.info("*" * 50)
    tf.debugging.set_log_device_placement(True)


def run_tensor_test():
    a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    c = tf.matmul(a, b)

    logger.info("*" * 50)
    logger.info("Tensor Test")
    logger.info("*" * 50)
    logger.info(f"Tensor A: {a}")
    logger.info(f"Tensor B: {b}")
    logger.info(f"Tensor A x B: {c}")


def check_nvidia_driver():
    if shutil.which("nvidia-smi") is not None:
        logger.info(subprocess.check_output("nvidia-smi", shell=True))
    else:
        logger.warning("NVidia driver not found")


if __name__ == "__main__":
    set_logger()
    log_version_and_gpu()
    check_nvidia_driver()
    set_log_placements()
    run_tensor_test()
