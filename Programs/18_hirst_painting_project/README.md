# Hirst Painting Project

<video src="../../GIFs/turtle_hirst_painting.mp4" controls title="Title"></video>

This is a painting inspired by [Damien Hirst](https://www.artsy.net/artist/damien-hirst).

### Extracting colors
In the first part, we extract colors from a sample of an actual Hirst painting to stay within the colorscheme. We do this by using the colorgram module.


### Painting
When we make the module using the turtle we set the starting position of the turtle to be at the bottom left. We make a dot at the starting position pick the pen up and move 50 steps ahead. For each dot we use a random color from the colors we extracted using colorgram. Then we repeat the steps for 10 dots. After we make the last dot in a row we set the position to the same x axis value on the left and 50 steps higher than the previous y value. We repeat this for the next 10 rows.