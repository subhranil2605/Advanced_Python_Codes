from functools import lru_cache


@lru_cache(maxsize=3)
def fetch_data_from_db(query):
    print(f"Executing query: {query}")
    return f"Result for query: {query}"


if __name__ == "__main__":
    queries = [
        "SELECT * FROM table1",
        "SELECT * FROM table2",
        "SELECT * FROM table3",
    ]
    for query in queries:
        fetch_data_from_db(query)
