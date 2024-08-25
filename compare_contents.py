import json

import orjson
import ujson

with open("combined_dataset.json", "rb") as f:
    combined_dataset = [orjson.loads(line) for line in f]


def compare(data):
    # json.dump()
    with open("json_dump.json", "w") as f:
        json.dump(data, f)
    print("json.dump()")
    with open("json_dump.json", "rb") as f:
        json_data = [json.loads(line) for line in f]
    print(f"  consistency: {[data] == json_data}")

    # json.dumps()
    json_data = json.dumps(data)
    with open("json_dumps.json", "w") as f:
        f.write(json_data)
    print("json.dumps()")
    with open("json_dumps.json", "rb") as f:
        json_data = [json.loads(line) for line in f]
    print(f"  consistency: {[data] == json_data}")

    # ujson.dump()
    with open("ujson_dump.json", "w") as f:
        ujson.dump(data, f)
    print("ujson.dump()")
    with open("ujson_dump.json", "rb") as f:
        ujson_data = [ujson.loads(line) for line in f]
    print(f"  consistency: {[data] == ujson_data}")

    # ujson.dumps()
    ujson_data = ujson.dumps(data)
    with open("ujson_dumps.json", "w") as f:
        f.write(ujson_data)
    print("ujson.dumps()")
    with open("ujson_dumps.json", "rb") as f:
        ujson_data = [ujson.loads(line) for line in f]
    print(f"  consistency: {[data] == ujson_data}")

    # orjson.dumps()
    orjson_data = orjson.dumps(data)
    with open("orjson_dumps.json", "wb") as f:
        f.write(orjson_data)
    print("orjson.dumps()")
    with open("orjson_dumps.json", "rb") as f:
        orjson_data = [orjson.loads(line) for line in f]
    print(f"  consistency: {[data] == orjson_data}")

    # orjson.dumps() with cast string
    orjson_data = orjson.dumps(data).decode("utf-8")
    with open("orjson_dumps_with_cast_string.json", "w") as f:
        f.write(orjson_data)
    print("orjson.dumps(), with cast string")
    with open("orjson_dumps_with_cast_string.json", "rb") as f:
        orjson_data = [orjson.loads(line) for line in f]
    print(f"  consistency: {[data] == orjson_data}")

    # orjson.dumps() and json.loads()
    print("orjson.dumps() and json.loads()")
    with open("orjson_dumps.json", "r") as f:
        json_data = [json.loads(line) for line in f]
    print(f"  consistency: {[data] == json_data}")


compare(combined_dataset)
