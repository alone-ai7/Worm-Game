# 🐍 Wormy Game

This repository contains an implementation of **Wormy**, a classic arcade clone of the retro game *Nibbles* (commonly known as *Snake*).

---

## 📚 Attributions & Credits

The code and assets in this repository are based entirely on Chapter 6 of the book **"Making Games with Python & Pygame"** written by **Al Sweigart (Albert Sweigart)**.

* **Author Website:** [https://inventwithpython.com](https://inventwithpython.com)
* **Original Chapter Walkthrough:** [Wormy Game Chapter Guide](https://inventwithpython.com)
* **Original Source Code Reference:** [Official wormy.py Source](https://inventwithpython.com)

---

## 🎮 How to Play

### 🕹️ Controls
You can use either of the following control schemes to steer the worm:
* **Arrow Keys:** `Up`, `Down`, `Left`, `Right`
* **WASD Keys:** `W` (Up), `A` (Left), `S` (Down), `D` (Right)

### 📜 Rules
* **Objective:** Eat as many red apples as possible to increase your length and score.
* **Game Over:** You lose if the worm hits the edge of the screen or crashes into its own tail.
* **Anti-Suicide System:** The game automatically ignores invalid reversed steering inputs (e.g., hitting `Left` while moving `Right` will not cause an instant self-collision).

---

## 🛠️ Technical Specifications & Mechanics

* **Resolution:** 640 × 480 pixels
* **Cell Grid Size:** 20 × 20 pixels square
* **Grid Matrix:** 32 cells wide by 24 cells high
* **Frame Rate:** Locked at 30 FPS to preserve an authentic, retro-style gameplay speed.

---

## 🚀 Getting Started

### 📋 Prerequisites
To run the source code directly, you need **Python 3.x** and **Pygame** installed on your system.

1. **Install Pygame:**
   ```bash
   pip install pygame
   ```

2. **Run the Game:**
   ```bash
   python wormy.py
   ```

---

## 📦 Running the Executable (.exe)

If you don't have Python or Pygame installed, you can download a standalone Windows executable binary directly from the **Releases** section of this repository.

1. Go to the **Releases** tab on the right side of this GitHub repository page.
2. Download the `Worm Game` executable from the latest release assets.
3. Double-click the file to launch and play instantly!

---

## ⚖️ License

The code and assets in this repository are based on the work of Al Sweigart from "Making Games with Python & Pygame". In accordance with the book's original licensing, this project is distributed under the **Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License (CC BY-NC-SA 3.0 US)**.

### Under this license, you are free to:
* **Share** — To copy, distribute, display, and perform the work.
* **Remix** — To make derivative works.

### Under the following conditions:
* **Attribution** — You must attribute the work in the manner specified by the author or licensor (visibly include the title and author's name in any excerpts of this work).
* **Noncommercial** — You may not use this work for commercial purposes.
* **Share Alike** — If you alter, transform, or build upon this work, you may distribute the resulting work only under the same or similar license to this one.

Copyright (c) 2012 by Albert Sweigart. Some Rights Reserved.  
For the full legal code, visit the official [Creative Commons License Page](http://creativecommons.org).
