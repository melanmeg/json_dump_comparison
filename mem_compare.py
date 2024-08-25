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
    # json.dumps()
    start_time = time.time()
    json_data = json.dumps(data)
    with open("json_dumps.json", "w") as f:
        f.write(json_data)
    end_time = time.time()
    return f"{end_time - start_time:.4f} s"


def orjson_dumps(data):
    # orjson.dumps()
    start_time = time.time()
    orjson_data = orjson.dumps(data)
    with open("orjson_dumps.json", "wb") as f:
        f.write(orjson_data)
    end_time = time.time()
    return f"{end_time - start_time:.4f} s"


def log_and_dump(data, label, dump_function):
    print(f"Time: {dump_function(data)}, Data: {label}, Func: {dump_function.__name__}")
    time.sleep(10)


log_and_dump(sample_data, "sample_data", json_dumps)
log_and_dump(combined_dataset, "combined_dataset.json", json_dumps)
log_and_dump(sample_data, "sample_data", orjson_dumps)
log_and_dump(combined_dataset, "combined_dataset.json", orjson_dumps)
