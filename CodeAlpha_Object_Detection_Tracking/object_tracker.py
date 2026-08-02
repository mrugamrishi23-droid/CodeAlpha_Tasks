import cv2
from ultralytics import YOLO

def main():
    # --- 1. Load the Model ---
    # We use YOLOv8 nano ('yolov8n.pt') because it is incredibly fast for real-time video.
    # It will automatically download the model weights the very first time you run this.
    print("Loading YOLOv8 model...")
    model = YOLO('yolov8n.pt')

    # --- 2. Initialize Video Stream ---
    # '0' tells OpenCV to use your default web camera. 
    # (If you want to use a pre-recorded video, change 0 to the file path, e.g., 'cars.mp4')
    print("Starting video stream...")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("✅ System Ready! Press 'q' in the video window to quit.")

    # --- 3. Process Video Frames ---
    while cap.isOpened():
        success, frame = cap.read()
        
        if not success:
            print("Video stream ended or failed to grab frame.")
            break

        # Run YOLOv8 tracking on the frame. 
        # 'persist=True' tells the model to remember objects across frames (Tracking)
        results = model.track(frame, persist=True, tracker="botsort.yaml", verbose=False)

        # Plot the tracking results (bounding boxes, labels, and IDs) onto the frame
        annotated_frame = results[0].plot()

        # --- 4. Display the Output ---
        cv2.imshow("CodeAlpha: Real-Time Object Tracking", annotated_frame)

        # Check for user input: Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # --- 5. Clean Up ---
    cap.release()
    cv2.destroyAllWindows()
    print("Video stream closed.")

if __name__ == "__main__":
    main()