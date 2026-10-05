# Wormy Game 🐍

This repository contains an implementation of **Wormy**, a classic arcade clone of the retro game *Nibbles* (commonly known as *Snake*). 

## 📚 Attributions & Credits
The code and assets in this repository are based entirely on Chapter 6 of the book **"Making Games with Python & Pygame"** written by **Al Sweigart (Albert Sweigart)**. 

* **Author Website:** [https://inventwithpython.com](https://inventwithpython.com)
* **Original Chapter Walkthrough:** [Wormy Game Chapter Guide](https://inventwithpython.com)
* **Original Source Code Reference:** [Official wormy.py Source](http://invpy.com)

---

## 🎮 How to Play

### Controls
You can use either of the following control schemes to steer the worm:
* **Arrow Keys:** `Up`, `Down`, `Left`, `Right`
* **WASD Keys:** `W` (Up), `A` (Left), `S` (Down), `D` (Right)

### Rules
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

### Prerequisites
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
The source code provided by Al Sweigart for this project is distributed under a **Simplified BSD License**:

Copyright (c) Al Sweigart. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
