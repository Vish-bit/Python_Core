import logging

# Logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format = '%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a, b):
    result = a+b
    logger.debug(f"Adding {a}+{b} = {result}")
    return result

def divide(a, b):
    try:
        result = a/b
        logger.debug(f"Dividing {a}+{b} = {result}")
        return result
    except:
        logger.error("Division by zero error")
        return None
    
add(5,84)
divide(99,817)



