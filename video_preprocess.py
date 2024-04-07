import cv2 as cv
import os

class video_preprocessing:
    def __init__(self, directory, video_path):
        self.directory = directory
        self.video = video_path

    def empty_folder(self):
        contents = os.listdir(self.directory)
        if not contents:
            for filename in os.listdir(self.directory):
                file_path = os.path.join(self.directory, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
        return True
    
    def extract_frames_per_second(self):
        cap = cv.VideoCapture(self.video_path)
        if empty_folder(self.directory):
            try:
                if not cap.isOpened():
                    raise IOError("Error opening video!")
            except IOError as e:
                print(f"IOError: {e}")
                return

        fps = cap.get(cv.CAP_PROP_FPS)
        frame_count = 0
        extracted_frame_count = 0
        while True:
            ret, frame = cap.read()

            if not ret:
                print("Can't receive frame (stream end?). Exiting...")
                break

            # Extracting one frame every 1 second (assuming constant FPS)
            if frame_count % int(fps) == 0:
                filename = f"{self.directory}/frame_{extracted_frame_count}.jpg"
                cv.imwrite(filename, frame)
                extracted_frame_count += 1

        frame_count += 1
        print(f"Extracted {extracted_frame_count} frames to {self.directory}")





    
        