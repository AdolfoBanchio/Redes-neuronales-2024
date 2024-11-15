from concurrent.futures import ProcessPoolExecutor, as_completed
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def simple_function(x):
    logging.debug(f"Processing {x}")
    return x * x

with ProcessPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(simple_function, i) for i in range(10)]
    for future in as_completed(futures):
        try:
            result = future.result()
            logging.debug(f"Result: {result}")
        except Exception as e:
            logging.error(f"Future resulted in an error: {e}")

logging.debug("All tasks have been processed.")