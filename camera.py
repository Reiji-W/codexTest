import cv2


def stream_from_camera(camera_id: int = 0) -> None:
    """Display the video stream from the specified camera.

    Press the ``q`` key to quit the window.
    """
    cap = cv2.VideoCapture(camera_id)
    if not cap.isOpened():
        raise RuntimeError(f"Unable to open camera {camera_id}")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame")
                break

            cv2.imshow("Camera Stream", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


def main() -> None:
    """Entry point for running the camera stream demo."""
    stream_from_camera()


if __name__ == "__main__":
    main()
