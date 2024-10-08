# HOW TO USE

```
from pyswirl import swirl

pen = swirl()
pen.set_style(style="shuffle")
pen.set_style(color_style=["#7b4b8b", "#828b4b"], bg_style="#ffffff")
pen.draw(185, iterations=127, circles=True, change_colors=True)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.draw(270, iterations=200, circles=True, change_width=True, change_colors=True)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.set_style(style="shuffle")
pen.draw(245, iterations=200, change_colors=True)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.set_style(color_style=["#556B2F", "#6B8E23", "#808000", "#8FBC8F", "#9ACD32"], bg_style="#ffffff")
pen.draw(150, iterations=200, circles=True, change_width=True, change_colors=True)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.set_style(color_style=["#BDB76B", "#DAA520", "#CD853F", "#8B4513", "#006400"], bg_style="#ffffff")
pen.draw(103, iterations=200, circles=True, change_width=True, change_colors=True)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.set_style(color_style="default", bg_style="#ffffff")
pen.draw(119, iterations=200, change_colors=True)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.draw(64, iterations=200, change_colors=True)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.draw(61, iterations=200, change_colors=True)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.draw(59, iterations=200, change_colors=True)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.set_style(color_style="all colors", bg_style="#FFFFFF", num_colors=2)
pen.draw(48, iterations=200, change_colors=True)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.set_style(color_style="pastel", bg_style="#000000", num_colors=2)
pen.draw(118, iterations=200, change_colors=True)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.set_style(style="default")
pen.draw(103, iterations=200, change_colors=False)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.draw(103, iterations=200, change_colors=False)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.draw(91, iterations=200, change_colors=False)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.draw(165, iterations=200, change_colors=False)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.draw(121, iterations=200, change_colors=False)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.draw(123, iterations=200, change_colors=False)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.draw(120, iterations=200, change_colors=False)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.draw(108, iterations=200, change_colors=False)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.draw(108, iterations=200, change_colors=False)
pen.clear()
```

```
from pyswirl import swirl
pen = swirl()
pen.draw(60, iterations=200, change_colors=False, circles=True)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.draw(80, iterations=200, change_colors=False, circles=True)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.draw(182, iterations=200, change_colors=False, circles=True)
pen.clear()
```

```
from pyswirl import swirl

pen = swirl()
pen.set_style(color_style="default", bg_style="#ffffff", num_colors=5)
pen.draw(144, iterations=200, circles=True, change_colors=True)
pen.clear()
```



# `swirl.set_style()`
## modify the look and style of background color, pen color.
## **parameters:**

### `style` : {'random', 'shuffle', 'default'}, optional
- **Data type** : string, array like
- **Description** : It takes any one of the following styles.
    - `"random"`: Automatically generate a random set of configurations for background and pen color.
    - `"shuffle"`: Pick a random style every time the draw function is called.
    - `"default"`: Revert back all/any changes made to the `set_style()` and use the default VIBGYOR color palette, white background, and black pen color.

### `color_style` : {'random', 'all colors', 'pastel', 'default'}, optional
- **Data type** : string, array like
- **Description** : It takes any one of the following styles or a list of hex color codes:
    - `"random"`: A random set of hex color codes will be generated automatically that will be used to draw the lines.
    - `"all colors"`: This will generate hex colors that are not too light or pastel. They are more suitable for an image with a white background as they contrast with white.
    - `"pastel"`: This will generate hex color codes that are of pastel colors. They are mostly suitable to be used with a black background color.
    - `"default"`: This will use the fundamental VIBGYOR color palette `['#537c78', '#7ba591', '#cc222b', '#f15b4c', '#faa41b', '#ffd45b']`

### `num_colors` : optional
- **Data type** : int
- **Description** : To allow users to specify the number of colors they want to use in their pattern, the `num_colors` parameter can be passed to the function. For instance, if the user intends to generate a pattern resembling the top of a pyramid, they can set `num_colors` to 3.

### `bg_style` : {’random’}, optional
- **Data type**: string, array like
- **Description**: It takes either `“random”` or any hex colour code as a parameter, which is used as a background colour for the canvas.

--- 
# `swirl.draw()`
## Draw a swirl drawing with the defined parameters and/or configrations from `set_style()` method.
## **parameters:**

### `change_colors` : optional
- **Data type**: bool
- **Description**: This parameter can be used to change the pen colour from black to colour. Use the `color_style` parameter in the `set_style()` method to customise the colors. By default swirl uses the VIBGYOR color palette `['#537c78', '#7ba591', '#cc222b', '#f15b4c', '#faa41b', '#ffd45b']`.

### `angle` : non-optional
- **Data type**: float
- **Description**: This parameter is used to define the angle with which the swirl must be drawn.

### `iterations` : default = 500
- **Data type**: int
- **Description**: This parameter is used to define the number of lines to be used. Each iteration draws one line.

### `change_colors` : optional
- **Data type**: bool
- **Description**: This parameter is used to turn the colours on and off. When this is set True, the pen uses the default colors unless the `set_style` is modified.

### `change_width` : optional
- **Data type**: bool
- **Description**: This parameter is used to gradually increases the width of each line in each iteration.

### `width_speed` : optional
- **Data type**: bool
- **Description**: This parameter is used to set the speed at which the line width changes for each iteration.

### `circles` : optional
- **Data type**: bool
- **Description**: This parameter is used to draw a circle after each line. The radius of the circle increases in every iteration.

### `rhombus` : optional
- **Data type**: bool
- **Description**: This parameter is used to draw a rhombus after each line. The radius of the circle increases in every iteration.

### `random_moves` : optional
- **Data type**: bool
- **Description**: This parameter is used to make random moves at every iteration.

---
# `swirl.save_result()`
## Save the swirl drawing
## **parameters:**

### `File_name` : optional
- **Data type**: str
- **Description**: This is used to name the file that is being generated.

### `png` : optional
- **Data type**: bool
- **Description**: To save a `.png` version of the drawing.

### `eps` : default = True
- **Data type**: bool
- **Description**: To save the `.eps` version of the file.
---
# `swirl.clear()`
## Clear the canvas by erasing whatever has been drawn so far.
## **parameters:**

### None
