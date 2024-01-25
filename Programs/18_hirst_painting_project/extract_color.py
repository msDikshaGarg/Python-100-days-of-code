import colorgram

rgb_colors = []
colors = colorgram.extract('sample_painting.png', 30)
for color in colors:
    R = color.rgb.r
    G = color.rgb.g
    B = color.rgb.b
    rgb_colors.append((R,G,B))