import fitz
import os
from PIL import Image
import glob


def save_images(target: str, destination: str):
    print(target)
    # Open PDF file
    pdf_file = fitz.open(target)
    base_name = os.path.basename(target)
    file_name = os.path.splitext(base_name)[0]

    # Calculate number of pages in PDF file
    page_nums = len(pdf_file)
    print(page_nums)

    # Create empty list to store images information
    images_list = []

    # Extract all images information from each page
    for page_num in range(page_nums):
        page_content = pdf_file[page_num]
        images_list.extend(page_content.get_images())

    # Raise error if PDF has no images
    if len(images_list) == 0:
        print("No files in:", target)

    # Save all the extracted images
    for i, image in enumerate(images_list, start=1):
        # Extract the image object number
        xref = image[0]
        # Extract image
        base_image = pdf_file.extract_image(xref)
        # Store image bytes
        image_bytes = base_image["image"]
        # Store image extension
        image_ext = base_image["ext"]
        # Generate image file name
        image_name = str(i) + "." + image_ext
        image_name = f"{file_name}-{str(i)}.{image_ext}"
        # Save image
        with open(os.path.join(destination, image_name), "wb") as image_file:
            image_file.write(image_bytes)
            image_file.close()
