import cv2 as cv
import os

class video_preprocessing:
  string =""
  def __init__(self, directory, video_path):
    self.directory = directory
    self.video = video_path

  def empty_folder(self):
    contents = os.listdir(self.directory)
    if not contents:
      for file in [os.path.join(self.directory, f) for f in contents if os.path.isfile(os.path.join(self.directory, f))]:
        os.remove(file)
    return True

  def extract_frames_per_second(self):
    cap = cv.VideoCapture(self.video_path)
    if self.empty_folder():
      try:
        if not cap.isOpened():
          raise IOError("Error opening video!")
      except IOError as e:
        string=f"IOError: {e}"
        return False

    fps = cap.get(cv.CAP_PROP_FPS)
    frame_count = 0
    extracted_frame_count = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            string="Can't receive frame (stream end?). Exiting...\n"
            break

        # Extracting one frame every 1 second (assuming constant FPS)
        if frame_count % int(fps) == 0:
            filename = f"{self.directory}/frame_{extracted_frame_count}.jpg"
            cv.imwrite(filename, frame)
            extracted_frame_count += 1

    frame_count += 1
    string+=f"Extracted {extracted_frame_count} frames to {self.directory}"
    return True







    
        