import json
import time

import orjson
import ujson

_ = {
    "name": "Alice",
    "age": 30,
    "city": "Tokyo",
    "hobbies": ["reading", "traveling", "coding"],
    "skills": {"Python": "advanced", "C++": "intermediate", "Go": "beginner"},
    "friends": [{"name": "Bob", "age": 28}, {"name": "Charlie", "age": 32}],
}
sample_data = [_] * 100000  # 大きなデータセットを作成

# kaggle dataset: https://www.kaggle.com/datasets/melissamonfared/mental-health-counseling-conversations-k
with open("combined_dataset.json", "rb") as f:
    combined_dataset = [orjson.loads(line) for line in f] * 100


def comparison(data):
    # json.dump() の速度測定
    start_time = time.time()
    with open("json_dump.json", "w") as f:
        json.dump(data, f)
    end_time = time.time()
    print(f"json.dump()   : {end_time - start_time:.4f} s")

    # json.dumps() の速度測定
    start_time = time.time()
    json_string = json.dumps(data)
    with open("json_dumps.json", "w") as f:
        f.write(json_string)
    end_time = time.time()
    print(f"json.dumps()  : {end_time - start_time:.4f} s")

    # ujson.dump() の速度測定
    start_time = time.time()
    with open("ujson_dump.json", "w") as f:
        ujson.dump(data, f)
    end_time = time.time()
    print(f"ujson.dump()  : {end_time - start_time:.4f} s")

    # ujson.dumps() の速度測定
    start_time = time.time()
    ujson_string = ujson.dumps(data)
    with open("ujson_dumps.json", "w") as f:
        f.write(ujson_string)
    end_time = time.time()
    print(f"ujson.dumps() : {end_time - start_time:.4f} s")

    # orjson.dump() の速度測定
    start_time = time.time()
    with open("orjson_dump.json", "wb") as f:
        f.write(orjson.dumps(data))
    end_time = time.time()
    print(f"orjson.dump() : {end_time - start_time:.4f} s")

    # orjson.dumps() の速度測定
    start_time = time.time()
    orjson_data = orjson.dumps(data)
    with open("orjson_dumps.json", "wb") as f:
        f.write(orjson_data)
    end_time = time.time()
    print(f"orjson.dumps(): {end_time - start_time:.4f} s")


def log_and_compare(data, label):
    print(f"Data: {label}")
    comparison(data)
    time.sleep(5)


log_and_compare(sample_data, "sample_data")
log_and_compare(combined_dataset, "combined_dataset.json")
