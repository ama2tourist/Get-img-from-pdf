import typer
import os
import glob
from typing_extensions import Annotated
from rich import print

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


def is_path_exists(target: str) -> bool:
    return os.path.exists(target)


def main(
    target: Annotated[
        str,
        typer.Option(
            "--target",
            "-t",
            prompt="Pass file or folder",
            help="Target pdf file or directory with pdf files",
        ),
    ],
    destination: Annotated[
        str,
        typer.Option(
            "--dest",
            "-d",
            prompt="Where to store images(default Downloads folder)",
            help="Option where to store images",
        ),
    ] = "",
):
    if not is_path_exists(target=target):
        print("[bold red]ValueError:[/bold red] Target path doesn't exists")
        return

    if not destination:
        destination = get_download_folder()
    elif not is_path_exists(destination):
        print("[bold red]ValueError:[/bold red] Destination doesn't exists")
        return

    if is_it_file(target=target) and is_it_pdf(target=target):
        save_images(target=target, destination=destination)

    for file in get_all_pdf_files(target=target):
        save_images(file, destination=destination)

    print("[green]Successfully extracted images[/green]")


if __name__ == "__main__":
    typer.run(main)
