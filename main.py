import typer
from get_downloads_folder import get_download_folder
from typing_extensions import Annotated


def main(
    target: Annotated[
        str, "Pass here file or folder from which image would be extracted"
    ],
    destination: Annotated[str, "Pass here where image would be stored"],
):
    print("Hello")


if __name__ == "__main__":
    typer.run(main)
