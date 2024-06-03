import os
import time
import random
import logging

from PIL import Image
import pytesseract

logging.basicConfig(level=logging.INFO, format="[%(levelname)s]  %(message)s")

# Developed By : mosTafa Arshadi
# Telegram : @mosishon

def crop_image(image_path: str, x: int, to_x: int, y: int, to_y: int) -> Image:
    """
    Crop the image specified by the image_path to the box defined by (x, to_x, y, to_y)

    Args:
    image_path (str): Path to the image file.
    x (int): The starting x-coordinate of the crop box.
    to_x (int): The ending x-coordinate of the crop box.
    y (int): The starting y-coordinate of the crop box.
    to_y (int): The ending y-coordinate of the crop box.

    Returns:
    Image: The cropped image.
    """
    # Open the image file
    with Image.open(image_path) as img:
        # Define the crop box
        crop_box = (x, y, to_x, to_y)
        # Crop the image using the defined box
        cropped_img = img.crop(crop_box)
        return cropped_img


# Example usage
phone_sizes = {
    "poco-x3": {
        "click_range_x": (200, 800),
        "click_range_y": (1000, 1700),
        "energy_range": (110, 350, 1850, 1950), # (start_x, end_x, start_y, end_y)
        "name_range": (185, 460, 300, 360),  # (start_x, end_x, start_y, end_y)
        "resolution": (1080, 2400),  # phone resolution (Required for dynamic size)
        "scores-range": (430, 845, 700, 805), # (start_x, end_x, start_y, end_y)
    }
}

# Select Your Phone Config
phone = phone_sizes["poco-x3"]

dynamic_sizes = True
if dynamic_sizes:
    resolution_size = phone["resolution"]
    click_range_x = (resolution_size[0] * 0.18, resolution_size[0] * 0.74)
    click_range_y = (resolution_size[1] * 0.41, resolution_size[1] * 0.708)
    energy_range = (
        resolution_size[0] * 0.101,
        resolution_size[0] * 0.34,
        resolution_size[1] * 0.770,
        resolution_size[1] * 0.81,
    )
    name_range = (
        resolution_size[0] * 0.1712,
        resolution_size[0] * 0.4259,
        resolution_size[1] * 0.125,
        resolution_size[1] * 0.15,
    )

    scores_range = (
        resolution_size[0] * 0.01,
        resolution_size[0] * 1,
        resolution_size[1] * 0.28,
        resolution_size[1] * 0.35,
    )

else:
    # Start x and end X for earn button in screen
    click_range_x = phone["click_range_x"]

    # Start y and end y for earn button in screen
    click_range_y = phone["click_range_y"]

    # start x, end x, start y,end y  for remain energy in screen
    energy_range = phone["energy_range"]

    # start x, end x, start y,end y  for name in screen
    name_range = phone["name_range"]

    # start x, end x, start y,end y  for scores in screen

    scores_range = phone["scores_range"]

_click_per_loop = 15
_sleep_time = 0.25
_coin_threshhold = 300

# What text show in name_range
my_name = "mosTafa (CEO)"


def random_click() -> None:
    """
    Simulate a random click on a device using ADB (Android Debug Bridge).

    This function generates random x and y coordinates within the specified
    ranges and sends a tap command to the connected Android device using ADB.

    The function does not return any value.

    Returns:
        None
    """
    x = random.randrange(
        int(click_range_x[0]), int(click_range_x[1])
    )  # Generate random x position
    y = random.randrange(
        int(click_range_y[0]), int(click_range_y[1])
    )  # Generate random y position
    os.popen(f"adb shell input tap {x} {y}")


def extract_text_from_image(image_path: str, tesseract_cmd: str | None = None) -> str:
    """
    Extract text from an image using Tesseract OCR.

    Args:
    image_path (str): Path to the image file.
    tesseract_cmd (str, optional): Path to the tesseract executable. Required on Windows.

    Returns:
    str: The extracted text from the image.
    """
    if tesseract_cmd:
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    img = Image.open(image_path)

    text = pytesseract.image_to_string(img)

    return text


def screen_shot(fname: str) -> str:
    """
    Capture a screenshot from a connected Android device using ADB (Android Debug Bridge).

    This function captures the current screen of the connected Android device and saves it to the specified file.

    Args:
        fname (str): The filename (including path) where the screenshot will be saved.

    Returns:
        str: The output from the ADB command, which may include error messages or confirmations.
    """
    os.popen(f"adb exec-out screencap -p > {fname}").read()
    return fname


def capture_name(remove_images: bool = False) -> str:
    """
    Capture and extract the name text from a screenshot.

    This function captures a screenshot, crops the image to the specified name range,
    and uses OCR to extract the text. Optionally, it can remove the images after processing.

    Args:
        remove_images (bool): If True, remove the images after extracting text. Default is False.

    Returns:
        str: The extracted name text.
    """
    screen_shot("a2.png")
    cropped_image = crop_image(
        "a2.png", name_range[0], name_range[1], name_range[2], name_range[3]
    )
    cropped_image.save("a2_1.png")
    text = extract_text_from_image("a2_1.png").strip()
    if remove_images:
        os.remove("a2.png")
        os.remove("a2_1.png")
    return text


def caputre_energy(remove_images: bool = False) -> str:
    """
    Capture and extract the energy text from a screenshot.

    This function captures a screenshot, crops the image to the specified energy range,
    and uses OCR to extract the text. Optionally, it can remove the images after processing.

    Args:
        remove_images (bool): If True, remove the images after extracting text. Default is False.

    Returns:
        str: The extracted energy text.
    """
    screen_shot("energy.png")
    cropped_image = crop_image(
        "energy.png",
        energy_range[0],
        energy_range[1],
        energy_range[2],
        energy_range[3],
    )
    cropped_image.save("remains_energy.png")
    text = extract_text_from_image("remains_energy.png").strip()
    if remove_images:
        os.remove("remains_energy.png")
        os.remove("energy.png")
    return text


def caputre_current_scores(remove_images: bool = False) -> str:
    """
    Capture and extract the current scores text from a screenshot.

    This function captures a screenshot, crops the image to the specified scores range,
    and uses OCR to extract the text. Optionally, it can remove the images after processing.

    Args:
        remove_images (bool): If True, remove the images after extracting text. Default is False.

    Returns:
        str: The extracted scores text.
    """
    screen_shot("scores.png")
    cropped_image = crop_image(
        "scores.png",
        scores_range[0],
        scores_range[1],
        scores_range[2],
        scores_range[3],
    )
    cropped_image.save("current_scored.png")
    text = extract_text_from_image("current_scored.png").strip()
    if remove_images:
        os.remove("current_scored.png")
        os.remove("scores.png")
    numbers = "".join((i for i in text if i.isdigit()))
    if numbers.isdigit():
        numbers = int(numbers)
        return f"{numbers:,}"
    else:
        return numbers


def main():
    i = 0
    total_click = 0
    start_score = 0
    while 1:

        # Checking app is open or no in loop
        retry = 0
        while 1:
            tt = capture_name()
            if tt != my_name:
                retry += 1
                logging.warning(f"You exited app.waiting for 1s (Total wait {retry}s)")
                time.sleep(1)
                if retry % 15 == 0:
                    os.system("cls")
            else:
                if start_score == 0:
                    start_score = caputre_current_scores()

                break
        for _ in range(_click_per_loop):
            random_click()
        logging.info(
            f"{_click_per_loop} Clicked! Total Click: {total_click}, Current Scores : {caputre_current_scores()} Start score : {start_score}"
        )
        total_click += _click_per_loop

        i += 1

        if i == 5:
            time.sleep(_sleep_time)
            i = 0

            # Check energy is lower then _coin_threshhold
            retry = 0

            while 1:
                tt = caputre_energy()
                if (
                    tt.split("/")[0].strip().isdigit()
                    and int(tt.split("/")[0].strip()) < _coin_threshhold
                ):  # Check if remain energy lower then _coin_threshhold
                    retry += 1

                    logging.warning(
                        f"Waiting 3s for energy. current energy : {int(tt.split('/')[0].strip())} / {int(tt.split('/')[1].strip())} minimum energy required : {_coin_threshhold} ({retry})"
                    )
                    time.sleep(3)
                    if retry % 5 == 0:
                        os.system("cls")
                else:
                    break


if __name__ == "__main__":
    main()
