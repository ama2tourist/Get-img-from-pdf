import typer
import os
import glob
from typing_extensions import Annotated

from get_downloads_folder import get_download_folder
from save_images import save_images


def is_it_pdf(target: str) -> bool:
    base_name = os.path.basename(target)
    return os.path.splitext(base_name)[1] == ".pdf"


def is_it_file(target: str) -> bool:
    if os.path.isdir(target):
        return False
    return True


def get_all_pdf_files(target: str) -> list[str]:
    return glob.glob(f"{target}*.pdf")


def main(
    target: Annotated[
        str, "Pass here file or folder from which image would be extracted"
    ],
    destination: Annotated[
        str,
        (
            "Pass here where image would be store\n",
            "Default location is Downloads folder",
        ),
    ] = "",
    renmove_after_saving: bool = False,
):
    if not destination:
        destination = get_download_folder()

    if is_it_file(target=target) and is_it_pdf(target=target):
        save_images(target=target, destination=destination)

    for file in get_all_pdf_files(target=target):
        save_images(file, destination=destination)

    print("Successfully extracted images")


if __name__ == "__main__":
    typer.run(main)
