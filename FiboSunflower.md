---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.9.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

### Fibonacci Series

```python
import fibogrowth as fb
import importlib
import numpy as np
import matplotlib.pyplot as plt
import math

importlib.reload(fb)

print([fb.fibo(n) for n in range(20)])
```

### Sunflower Pattern

```python
print('Golden ratio = {}'.format(fb.golden))
print('Phi =          {}'.format(fb.phi))
```

```python
def draw_sunflower(N, interval_group, r0, a0, area_slope = 0):
    it = fb.fibo(interval_group)
    print('Total seeds = {}'.format(N))
    print('Red seeds interval = {}'.format(it))
    fg = fb.FiboGrowth(r0, a0, area_slope)
    dist = [ fg.radius(n) for n in range(N) ]
    theta = [ fg.angle(n) for n in range(N) ]
    area = [ fg.area(n) for n in range(N) ]
    colors = [ 0.05 ] * N
    for k in range(0, N, it):
        colors[k] = 0.9
        area[k] *= 1.5

    plt.figure(figsize=[10, 10])
    ax = plt.gca(projection='polar')
    plt.ylim(0, 1.05 * max(dist))
    print('Radius = {}'.format(max(dist)))
    pix_per_unit = (ax.transData.transform([0, 1]) - ax.transData.transform([0, 0]))[0]
    scaled_area = list(map(lambda r: pix_per_unit**2 * r, area))
    plt.scatter(theta, dist, c=colors, s=scaled_area, cmap='jet', vmin=0.0, vmax=1.0)
    plt.title('Sunflower')
    plt.show()
```

```python
draw_sunflower(1000, 10, 1, 0.5)
```

```python
draw_sunflower(2000, 10, 1, 2, 0.001)
```

```python
draw_sunflower(2000, 10, 1, 2, 0.01)
```

### References
- Helmut Vogel (1979) _A better way to construct the sunflower head_
