# [![Website](https://img.shields.io/badge/Website-Visit-brightgreen)](https://psairam9301.wixsite.com/website) [![YouTube](https://img.shields.io/badge/YouTube-Subscribe-red)](https://www.youtube.com/@sairampenjarla) [![GitHub](https://img.shields.io/badge/GitHub-Explore-black)](https://github.com/sairam-penjarla) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/sairam-penjarla-b5041b121/) [![Instagram](https://img.shields.io/badge/Instagram-Follow-ff69b4)](https://www.instagram.com/sairam.ipynb/)

# Swirl Art Generator

A Tkinter-based application that uses Turtle graphics to create stunning swirl art with customizable options.

## Getting Started

Follow these steps to clone the repository, set up the environment, and run the project:

### Clone the Repository

```bash
git clone https://github.com/sairam-penjarla/swirl-art-generator.git
cd swirl-art-generator
```

### Set Up a Virtual Environment

Learn how to create a virtual environment from this blog post: [Learn Virtualenv Basics](https://psairam9301.wixsite.com/website/post/learn-virtualenv-basics).

#### Using Virtualenv

```bash
python -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`
```

#### Using Anaconda

```bash
conda create --name swirl-art-env python=3.9
conda activate swirl-art-env
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

## Project Details

The **Swirl Art Generator** is designed to create intricate spiral patterns using Python's Turtle and Tkinter modules.

### Key Features:

- **Customizable Options**: Set angle, iterations, background color, and color palette.
- **Multiple Line Styles**: Supports line, circle, and rhombus patterns.
- **Dynamic Animation**: Smooth, real-time drawing with customizable speed.
- **Interactive Controls**:
  - **Pause** and **Resume** buttons for the animation.
  - **Reset** button to clear the canvas and restore default settings.
- **Random Color Generation**: Generate unique patterns with random colors.
- **User-Friendly UI**: Designed with beginners in mind for an engaging experience.
- **Canvas Size**: Default canvas size is 1000x1000 pixels, with the pen starting at the center (500x500).

### Use Cases:

- Generate artistic patterns for creative projects.
- Visual demonstrations for teaching geometry or programming.
- Fun, interactive tool for hobbyists and art enthusiasts.

## Examples and Suggestions

### Sample Angles and Color Palettes:

- **Angle**: 25 degrees, **Color Palettes**: #f2f2f2, #d9d9d9, #bfbfbf, #a6a6a6, #8c8c8c  
- **Angle**: 30 degrees, **Color Palettes**: #7ba591, #cc222b, #f15b4c, #faa41b  
- **Angle**: 31 degrees, **Color Palettes**: #FF5733, #33FF57, #3357FF, #FF33A8  
- **Angle**: 40 degrees, **Color Palettes**: #537c78, #7ba591, #cc222b  
- **Angle**: 45 degrees, **Color Palettes**: #cc222b, #f15b4c, #faa41b, #ffd45b  
- **Angle**: 50 degrees, **Color Palettes**: #537c78, #7ba591, #cc222b, #f15b4c, #faa41b, #ffd45b  
- **Angle**: 50 degrees, **Color Palettes**: #537c78, #7ba591, #cc222b, #f15b4c, #33FF57, #faa41b, #ffd45b  
- **Angle**: 59 degrees, **Color Palettes**: #537c78, #7ba591, #cc222b, #f15b4c, #faa41b, #ffd45b  
- **Angle**: 59 degrees, **Color Palettes**: #f2f2f2, #d9d9d9, #bfbfbf, #a6a6a6, #8c8c8c  
- **Angle**: 60 degrees, **Color Palettes**:  #f15b4c, #faa41b, #ffd45b  
- **Angle**: 62 degrees, **Color Palettes**:  #f15b4c, #faa41b, #ffd45b  
- **Angle**: -70 degrees, **Color Palettes**: #f15b4c, #faa41b, #ffd45b  
- **Angle**: 80 degrees, **Color Palettes**: #537c78, #7ba591, #cc222b, #f15b4c, #faa41b, #ffd45b, #FF5733, #33FF57, #3357FF  
- **Angle**: 89 degrees, **Color Palettes**: #7ba591, #cc222b, #f15b4c, #faa41b  
- **Angle**: 90 degrees, **Color Palettes**: #537c78, #7ba591, #cc222b, #f15b4c  
- **Angle**: 91 degrees, **Color Palettes**: #537c78, #7ba591, #cc222b, #f15b4c  
- **Angle**: 108 degrees, **circle**, **Color Palettes**: #537c78, #7ba591, #cc222b, #f15b4c, #faa41b, #ffd45b  
- **Angle**: 120 degrees, **circle**, **Color Palettes**: #537c78, #7ba591, #cc222b, #f15b4c  
- **Angle**: 145 degrees, **circle**, **Color Palettes**: #f2f2f2, #d9d9d9, #bfbfbf, #a6a6a6, #8c8c8c  
- **Angle**: 150 degrees, **circle**, **Color Palettes**: #537c78, #7ba591, #cc222b, #f15b4c, #faa41b, #ffd45b   
- **Angle**: 160 degrees, **circle**, **Color Palettes**: #f2f2f2, #d9d9d9, #bfbfbf, #a6a6a6, #8c8c8c  
- **Angle**: 175 degrees, **circle**, **Color Palettes**: #faa41b, #ffd45b 
- **Angle**: 180 degrees, **circle**, **Color Palettes**: #faa41b, #ffd45b 
- **Angle**: 180 degrees, **circle**, **Color Palettes**: #faa41b, #ffd45b 
- **Angle**: 200 degrees, **circle**, **Color Palettes**: #537c78, #7ba591 
- **Angle**: 215 degrees, **circle**, **Color Palettes**: #537c78, #7ba591 
- **Angle**: 215 degrees, **circle**, **Color Palettes**: #537c78, #7ba591, #cc222b, #f15b4c, #faa41b 
- **Angle**: 310 degrees, **rhombus**, **Color Palettes**: #537c78, #7ba591, #cc222b, #f15b4c, #faa41b
- **Angle**: 295 degrees, **rhombus**, **Color Palettes**: #537c78, #7ba591, #cc222b, #f15b4c, #faa41b, #ffd45b


### Sample Color Palettes:

1. `#537c78, #7ba591, #cc222b, #f15b4c, #faa41b, #ffd45b` (Default)
2. `#FF5733, #33FF57, #3357FF, #FF33A8` (Vibrant)
3. `#f2f2f2, #d9d9d9, #bfbfbf, #a6a6a6, #8c8c8c` (Monochrome)


---

Happy Creating!

