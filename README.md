# Steganography Tool with Tkinter

## Project Overview

This repository contains a Steganography Tool developed in Python using Tkinter for the GUI. The tool allows users to embed files within images, providing a secure and discreet way to share information. The system utilizes steganographic techniques to hide files within the pixel data of images.

## Features

- **File Embedding:** Users can embed files within images seamlessly.
- **Image Selection:** Choose the cover image for embedding and the image containing hidden data.
- **Password Protection:** Optionally, users can set a password for added security.
- **Tkinter GUI:** The system utilizes Tkinter for building the graphical user interface.
- **Python-Based:** Developed entirely in Python, ensuring simplicity and ease of customization.

## Requirements

Ensure you have the following dependencies installed:

- Python 3.x

Install required Python packages using:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the steganography tool script:

```bash
python frontend.py
```

2. Use the Tkinter GUI to select the cover image, the file to be embedded, and set a password if desired.
3. Click the "Embed" button to hide the file within the image.

## File Structure

- **`steganography_tool.py`**: Main script for the steganography tool with Tkinter GUI.
- **`images/`**: Directory for storing sample images.
- **`icons/`**: Directory for storing icons used in the GUI.

## Configuration

Adjust the configuration parameters in `config.py` as needed:

```python
# Configuration Parameters
ENCRYPT_KEY = "your_secret_key"
```

## Decoding

To extract the hidden file from an image, run the steganography tool script and select the steganographic image. Enter the correct password if it was set during embedding.

## Acknowledgments

- Tkinter: [https://docs.python.org/3/library/tkinter.html](https://docs.python.org/3/library/tkinter.html)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Contact

For any questions or inquiries, please contact [vethanathan] at [vethanathanvk@gmail.com].
