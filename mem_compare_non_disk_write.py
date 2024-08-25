import json
import time

import orjson

_ = {
    "name": "Alice",
    "age": 30,
    "city": "Tokyo",
    "hobbies": ["reading", "traveling", "coding"],
    "skills": {"Python": "advanced", "C++": "intermediate", "Go": "beginner"},
    "friends": [{"name": "Bob", "age": 28}, {"name": "Charlie", "age": 32}],
}
sample_data = [_] * 1000000

with open("combined_dataset.json", "rb") as f:
    combined_dataset = [orjson.loads(line) for line in f] * 500


def json_dumps(data):
    start_time = time.time()
    json.dumps(data)
    end_time = time.time()
    return f"{end_time - start_time:.4f} s"


def orjson_dumps(data):
    start_time = time.time()
    orjson.dumps(data)
    end_time = time.time()
    return f"{end_time - start_time:.4f} s"


def log_and_dump(data, label, dump_function):
    print(f"Time: {dump_function(data)}, Data: {label}, Func: {dump_function.__name__}")
    time.sleep(10)


log_and_dump(sample_data, "sample_data", json_dumps)
log_and_dump(combined_dataset, "combined_dataset.json", json_dumps)
log_and_dump(sample_data, "sample_data", orjson_dumps)
log_and_dump(combined_dataset, "combined_dataset.json", orjson_dumps)
