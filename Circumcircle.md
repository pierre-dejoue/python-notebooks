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

```python
a = [0.025047823616310, -0.4133734963715]
d = [-0.01870869221693, -0.4012556846482]
e = [-0.01866820383825, -0.4012496129870]
f = [-0.01865929845770, -0.4012482863366]
```

```python
def inCircumcircle(a, b, c, d):
    """Is d in abc's circumcircle?"""

    adx = a[0] - d[0];
    ady = a[1] - d[1];
    bdx = b[0] - d[0];
    bdy = b[1] - d[1];
    cdx = c[0] - d[0];
    cdy = c[1] - d[1];

    oabd = adx * bdy - bdx * ady;
    ocad = cdx * ady - adx * cdy;
    obcd = bdx * cdy - cdx * bdy;

    alift = adx * adx + ady * ady;
    blift = bdx * bdx + bdy * bdy;
    clift = cdx * cdx + cdy * cdy;

    det = alift * obcd + blift * ocad + clift * oabd;

    return (det > 0, det);
```

```python
print(inCircumcircle(f, e, a, d))
print(inCircumcircle(e, d, f, a))
print(inCircumcircle(d, a, e, f))
```

```python

```
