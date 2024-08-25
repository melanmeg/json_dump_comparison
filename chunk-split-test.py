import time

import orjson

chunk_size = 1000

with open("combined_dataset.json", "rb") as f:
    combined_dataset = [orjson.loads(line) for line in f] * 500


def orjson_dumps(data):
    orjson_data = orjson.dumps(data)
    with open("orjson_dumps.tmp.json", "wb") as f:
        f.write(orjson_data)


def split_and_dump(dataset, chunk_size):
    total_chunks = (len(dataset) + chunk_size - 1) // chunk_size
    start_time = time.time()
    for i in range(total_chunks):
        chunk = dataset[i * chunk_size : (i + 1) * chunk_size]
        orjson_dumps(chunk)
    end_time = time.time()
    print(f"Time: {end_time - start_time:.4f} s")


split_and_dump(combined_dataset, chunk_size)
