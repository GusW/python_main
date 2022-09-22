from pathlib import Path, PosixPath
from typing import Any, Iterable
import pandas as pd

from f_emails.config import gmail_client
from f_emails.constants import CONTACTS_PATH, TEMP_FOLDER_PATH


def send_email_with_attachment(
    receiver: str, subject: str = "", contents: str = "", file_path: str = ""
):
    gmail_client().send(to=receiver, subject=subject, contents=[contents, file_path])
    print("Email with attachment was sent!")


def generate_file(file_path: PosixPath, contents: str = ""):
    with open(file_path, "w") as file_:
        file_.write(contents)


def handle_email(contacts: Iterable[tuple[str, Any]]):
    for _, row in contacts:
        client_name = row.get("name")
        total = row.get("amount")
        file_path = Path.joinpath(TEMP_FOLDER_PATH, f"{client_name}.txt")
        generate_file(file_path, contents=f"TOTAL: ${total}")
        send_email_with_attachment(
            row.get("email"),
            subject=f"Your invoice, {client_name}",
            contents=f"""Hey {client_name}!
            I'm sending this email using Python.
            Your invoice amount is {total}
            """,
            file_path=file_path.as_posix(),
        )


def main() -> None:
    df = pd.read_csv(CONTACTS_PATH)
    handle_email(df.iterrows())


if __name__ == "__main__":
    main()
