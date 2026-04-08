# 📏 PyQt6 Unit Converter (Feet to Centimeters)

A lightweight, desktop-based graphical user interface (GUI) application designed for rapid unit conversion. Built with Python and the PyQt6 framework, this tool provides a robust, interactive window for translating imperial distance (feet) into metric units (centimeters).

## 🧠 Engineering Architecture
This application utilizes a straightforward, event-driven architecture:
* **Frontend (View):** Constructed using `PyQt6.QtWidgets`. It employs a `QGridLayout` to ensure precise, rigid alignment of interface elements, including `QLabel` prompts, `QLineEdit` inputs, and `QComboBox` selection menus.
* **Backend Logic (Controller):** Mathematical conversion logic is bound to a `QPushButton` trigger. The system dynamically reads the user input, applies the standard conversion factor (1 foot = 30.48 cm), and updates the UI state.
* **Error Handling:** Implements `try/except` blocks to catch `ValueError` exceptions, ensuring the application remains stable and provides user feedback if non-numeric data is submitted.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **GUI Framework:** PyQt6
* **System Libraries:** `sys`

## 🚀 Installation & Execution

Follow these steps to isolate the environment and launch the application locally.

**1. Clone the repository**
```bash
git clone https://github.com/Nayanxyz/feet-to-cm-converter.git
cd feet-to-cm-converter
```
**2. Install Dependencies**
```bash
pip install PyQt6
```
**3. Execute the application**
```bash
python main.py
```
