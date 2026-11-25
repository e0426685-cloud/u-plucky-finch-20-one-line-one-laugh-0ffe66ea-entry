import os

ENTRY = "My fitness tracker congratulated me for burning 400 calories. I was just angrily pacing while my code refused to compile."

MAX_CHARS = 200


def validate(text):
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry text is empty")
    if len(text) > MAX_CHARS:
        raise ValueError("entry text exceeds 200 characters")
    if "\n" in stripped:
        raise ValueError("entry must be a single line")
    return text


def main():
    text = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    entry_path = "/output/entry.txt"
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
