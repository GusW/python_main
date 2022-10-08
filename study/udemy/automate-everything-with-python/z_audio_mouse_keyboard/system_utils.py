from pathlib import Path

import psutil


def get_cpu_count(logical: bool = True):
    return psutil.cpu_count(logical=logical)


def get_cpu_percentage_consumption(interval: float = 1):
    return psutil.cpu_percent(interval=interval)


def get_cpu_times():
    return psutil.cpu_times()


def get_cpu_stats():
    return psutil.cpu_stats()


def get_ram_stats():
    return psutil.virtual_memory()


def get_swap_memory_stats():
    return psutil.swap_memory()


def get_storage_stats(root_path: Path):
    return psutil.disk_usage(root_path)


def get_storage_partitions():
    return psutil.disk_partitions()


def main():
    print(f"{get_cpu_count()=}\n")
    print(f"{get_cpu_count(logical=False)=}\n")
    print(f"{get_cpu_percentage_consumption(interval=3)=}\n")
    print(f"{get_cpu_times()=}\n")
    print(f"{get_cpu_stats()=}\n")
    print(f"{get_ram_stats()=}\n")
    print(f"{get_swap_memory_stats()=}\n")
    path = Path("/")
    print(f"{get_storage_stats(path)=}\n")
    print(f"{get_storage_partitions()=}\n")


if __name__ == "__main__":
    main()
