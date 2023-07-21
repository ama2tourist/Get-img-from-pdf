# Get Images from PDF

This script allows you to extract and save all images from a PDF file.

## Installation

Follow these steps to install and use the script:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/ama2tourist/Get-img-from-pdf.git
   cd Get-img-from-pdf
   ```

2. Install the required dependencies using pip:

   ```
   pip install -r requirements.txt --user
   ```

## How to Use

To use the script, you have two options:

### Option 1: Use Prompt (Default Settings)

Simply run the script without any options to use the default settings:

```
python main.py
```

This will prompt you to enter the target PDF file or directory path and ask you where to store the extracted images. By default, if you don't provide the destination folder path, the images will be saved in the "Downloads" folder.

### Option 2: Specify Custom Paths

If you want to specify custom paths, you can use the following command:

```
python main.py --target <pdf_file_or_directory_path> --dest <destination_folder_path>
```

Replace `<pdf_file_or_directory_path>` with the path to the PDF file or the directory containing PDF files from which you want to extract images.

Replace `<destination_folder_path>` with the path to the folder where you want to store the extracted images. If you omit the `-d` option, you will be prompted to enter the destination folder path.

Shortcuts for the options:

- `-t` is short for `--target`
- `-d` is short for `--dest`

Make sure the Python version used to run the script is compatible with the requirements specified in the `requirements.txt` file.

Feel free to explore and use this script to extract images from PDF files conveniently!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
