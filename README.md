# codextest Camera Demo

This project demonstrates how to stream video from the built-in camera
using Python and OpenCV.

## Requirements

- Python 3.12 or later
- OpenCV (`opencv-python` package)

If `pip install opencv-python` fails on ARM64 or some Python versions, try installing OpenCV from conda-forge:

```bash
conda install -c conda-forge opencv
```

## Usage

Install the dependencies and run the demo:

```bash
pip install -e .
python main.py
```

Press `q` in the video window to stop streaming.
