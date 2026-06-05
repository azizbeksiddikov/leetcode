from pathlib import Path

SUBDIRECTORIES = ("easy", "medium", "hard")


def count_files(directory: Path) -> int:
    return sum(1 for item in directory.iterdir() if item.is_file())


def main() -> None:
    root = Path(__file__).resolve().parent
    total = 0

    for name in SUBDIRECTORIES:
        directory = root / name
        if not directory.exists():
            print(f"{name}: missing directory")
            continue

        count = count_files(directory)
        total += count
        print(f"{name}: {count}")

    print(f"total: {total}")


if __name__ == "__main__":
    main()
