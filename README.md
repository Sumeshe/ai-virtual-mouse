# AI Virtual Mouse 🖐️🖱️

A real-time AI Virtual Mouse built using Python, OpenCV, and MediaPipe. It uses hand gestures captured through a webcam to control mouse movement and perform common mouse actions without a physical mouse.

## ✨ Features

- **Cursor Movement:** Move the mouse cursor using index-finger tracking.
- **Cursor Freeze:** Freeze the cursor using a custom thumb and finger landmark gesture.
- **Left Click:** Perform a left-click using a thumb and index-finger pinch.
- **Right Click:** Perform a right-click using a custom thumb and middle-finger gesture.
- **Double Click:** Perform a double-click using a custom three-fingertip gesture.
- **Screenshot Capture:** Capture and save screenshots using an open-palm → closed-fist → open-palm gesture.
- **Real-Time Hand Tracking:** Detect and track hand landmarks through a webcam.

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- Math and coordinate geometry

## ⚙️ Requirements

- Windows computer
- Python environment
- Webcam
- Git (for cloning the repository)

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/ai-virtual-mouse.git
cd ai-virtual-mouse
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python virtual_mouse.py
```

Press **Q** while the webcam window is active to exit.

## 🖐️ Gesture Controls

| Action | Gesture |
|---|---|
| Move cursor | Keep thumb and index finger apart |
| Freeze cursor | Bring thumb close to index-finger landmarks |
| Left click | Bring thumb and index fingertip close together |
| Right click | Use the configured thumb and middle-finger gesture |
| Double click | Bring thumb, index, and middle fingertips close together |
| Screenshot | Open palm → close fist → open palm |

*Gesture thresholds may require adjustment depending on camera position, hand size, and lighting.*

## 📸 Screenshot Storage

Screenshots are saved to the configured screenshot folder. The folder path and filename format can be customized in the Python code.

## 🧠 How It Works

1. OpenCV captures frames from the webcam.
2. MediaPipe detects hand landmarks in each frame.
3. Landmark coordinates are used to calculate finger distances.
4. Custom gesture conditions determine the intended mouse action.
5. PyAutoGUI moves the cursor and performs clicks or captures screenshots.

## 🔮 Future Improvements

- Improve cursor smoothing and precision.
- Add gesture calibration.
- Improve gesture detection under different lighting conditions.
- Add a graphical user interface for gesture configuration.
- Improve screenshot feedback and error handling.

## 👨‍💻 Author

**SUMESHE**

Developed as a computer vision project to explore real-time hand tracking and gesture-based human-computer interaction.
