import time

import orjson

with open("combined_dataset.json", "rb") as f:
    combined_dataset = [orjson.loads(line) for line in f] * 100


def orjson_dumps(data):
    start_time = time.time()
    orjson_data = orjson.dumps(data)
    with open("orjson_dumps.tmp14.json", "wb") as f:
        f.write(orjson_data)
    end_time = time.time()
    return f"{end_time - start_time:.4f} s"


def log_and_dump(data, label, dump_function):
    print(f"Time: {dump_function(data)}, Data: {label}, Func: {dump_function.__name__}")


log_and_dump(combined_dataset, "combined_dataset.json", orjson_dumps)
