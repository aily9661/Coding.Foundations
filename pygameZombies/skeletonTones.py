import cv2
import math
import time
import mediapipe as mp
import numpy as np
import simpleaudio as sa



minFrequency = 220.
maxFrequency = 440.
min2Freq = 320.
max2Freq = 640.
majorPentatonic = [0,2,4,7,9,12,16,19] #major pentatonic scale
minorPentatonic = [0,3,5,7,10,12,15,17] #minor pentatonic scale

def getDistance(idx1,idx2,landmarks):
    return math.sqrt((landmarks.landmark[idx1].x-landmarks.landmark[idx2].x)**2 + 
                     (landmarks.landmark[idx1].y-landmarks.landmark[idx2].y)**2 + 
                     (landmarks.landmark[idx1].z-landmarks.landmark[idx2].z)**2)

def getNewNote(baseFreq,nSemitones):
    return baseFreq*2.0**(nSemitones/12)

def play_tone(frequency, duration):
    # Generate a sine wave with fade-in and fade-out
    sample_rate = 44100  # Sample rate in Hz
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    fade_duration = 0.05  # Adjust the fade-in/fade-out duration as needed
    fade_samples = int(fade_duration * sample_rate)

    # Create a fade-in and fade-out envelope
    fade_in = np.linspace(0, 1, fade_samples)
    fade_out = np.linspace(1, 0, fade_samples)

    # Generate the sine wave
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    # Apply fade-in and fade-out
    wave[:fade_samples] *= fade_in
    wave[-fade_samples:] *= fade_out

    # Play the sine wave
    play_obj = sa.play_buffer((wave * 32767).astype(np.int16), 1, 2, sample_rate)
    #play_obj.wait_done()

def main():
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    # Set up the webcam
    cap = cv2.VideoCapture(0)

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame. Exiting...")
                break
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(rgb_frame)
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)   
            
            
                distanceWrists = getDistance(15,16,results.pose_landmarks)
                distanceWristToKneeLeft = getDistance(15,25,results.pose_landmarks)
                distanceWristToKneeRight = getDistance(16,26,results.pose_landmarks)

                freqToPlay = minFrequency + (maxFrequency*distanceWrists)
                play_tone(freqToPlay,0.1)
                
            cv2.imshow('MediaPipe Skeleton', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
