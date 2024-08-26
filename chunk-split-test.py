import time
import os
import orjson

chunk_size = 100000

with open("combined_dataset.json", "rb") as f:
    combined_dataset = [orjson.loads(line) for line in f] * 500


def orjson_dumps(data, chunk_index):
    orjson_data = orjson.dumps(data)
    filename = f"orjson_dumps_chunk_{chunk_index}.json"
    with open(filename, "wb") as f:
        f.write(orjson_data)


def split_and_dump(dataset, chunk_size):
    total_chunks = (len(dataset) + chunk_size - 1) // chunk_size
    start_time = time.time()
    for i in range(total_chunks):
        chunk = dataset[i * chunk_size : (i + 1) * chunk_size]
        orjson_dumps(chunk, i)
    end_time = time.time()
    print(f"Time: {end_time - start_time:.4f} s")
    

split_and_dump(combined_dataset, chunk_size)

def load_chunk(chunk_index):
    filename = f"orjson_dumps_chunk_{chunk_index}.json"
    with open(filename, "rb") as f:
        data = orjson.loads(f.read())
    return data

def find_total_chunks(directory, base_filename):
    files = os.listdir(directory)
    chunk_files = [f for f in files if f.startswith(base_filename) and f.endswith(".json")]
    return len(chunk_files)

def load_all_chunks(directory="."):
    base_filename = "orjson_dumps_chunk_"
    total_chunks = find_total_chunks(directory, base_filename)
    dataset = []
    for i in range(total_chunks):
        chunk_data = load_chunk(i)
        dataset.extend(chunk_data)
    return dataset


orjson_data = loaded_dataset = load_all_chunks()
print(f"  consistency: {combined_dataset == orjson_data}")
