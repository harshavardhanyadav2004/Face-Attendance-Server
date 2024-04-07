import face_recognition as fr
import cv2 as cv
import os
import pickle
import numpy as np

class face_recog:
    def __init__(self,filename, frames, pickle_path) :
        self.filename = filename
        self.pickle_path = pickle_path
        self.frames = frames
        with open('pickle_path', 'rb') as file:
            known_face_encodings = pickle.load(file)
        self.students = {
            'Dinesh' : '213J1A4267',
            'Ritesh' : '213J1A4280',
            'Vardhan' : '213J1A4287',
            'Bhavani Shankar' : '213J1A4288',
            'Shyam': '213J1A4297',
            'Hemant Srinivas' : '213J1A4298',
            'Harsha Vardhan' : '213J1A42A6',
            'Sadhik' : '213J1A42B1',
            'Sadhiq Shaik' : '213J1A42B2',
            'Manideep' : '213J1A42B6',
            'Rohit' : '213J1A42B9', 
            'Purna' : '213J1A42C2',
            'Dev' : '213J1A42C3',
            'Murali' : '213J1A42C6',
            'Vivek' : '213J1A42C9',
            'Deepak' : '213J1A42D2',
            'Naveen' :  '223J5A4208',
            'Praveen Kumar': '223J5A4209',
            'Tharun' : '223J5A4211',
        }

    #this is temporary code for path exrtaction this was written based on path design of windows file
    def load_image_paths(self):
        image_paths = []
        for filename in os.listdir(self.frames):
            if filename.lower().endswith('.jpg'):
                image_path = os.path.join(self.frames, filename)
                self.FACES = self.load_faces(image_path)
                image_paths.append(image_path)
        return image_paths
    
    def find_faces(image_paths):
        face_locations = []
        final_face = []
        face_encodings = []

        for path in image_paths:
            frame = fr.load_image_file(path)
            rgb_small_frame = frame[:, :, ::-1]
            face_locations = fr.face_locations(rgb_small_frame, number_of_times_to_upsample=1, model='hog')
            face_encodings = fr.face_encodings(frame, face_locations)
            for face_encoding in face_encodings:
                final_face.append(face_encoding)
            with open('video_face_encodings.pkl', 'wb') as file:
                pickle.dump(final_face, file)
            print(f"Extracted {len(final_face)} faces and encoded to {video_face_encodings}")

    def cosine_similarity(vector_a, vector_b):
        dot_product = np.dot(vector_a, vector_b)
        magnitude_a = np.linalg.norm(vector_a)
        magnitude_b = np.linalg.norm(vector_b)

        # Avoid division by zero (if magnitudes are close to zero)
        if magnitude_a == 0 or magnitude_b == 0:
            return 0

        cosine_similarity_value = dot_product / (magnitude_a * magnitude_b)
        return cosine_similarity_value


    def compare_faces(self,video_face_encodings, known_face_encodings):
        similarities = []
        nec = []
        student_names = []
        for y in video_face_encodings:
            for x in known_face_encodings:
                similarity = cosine_similarity(y, x)
                nec.append(similarity)
            similarities.append(nec)
        for x in similarities:
            student_names.append(self.students.keys[np.argmax[x]])
        return student_names




