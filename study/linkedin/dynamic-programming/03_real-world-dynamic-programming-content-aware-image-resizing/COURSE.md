# Real-World Dynamic Programming: Content-Aware Image Resizing

## Seam carving

<https://en.wikipedia.org/wiki/Seam_carving>

## Content-aware image resizing

1. Pre-processing
   - getting the image into a form which dynamic programming can be applied
   - reading the image and finding the uninteresting parts of it
2. Dynamic programming
   - find the least interesting scene
3. Post-processing
   - Get the result of the Dynamic Programming algorithm and apply them
   - Remove the least interesting pixels from the picture and saving that to a file

## Pixel energy

- The difference (delta) of the colors between the pixel and all its surrounding area
- Face detection
- Background and foreground segmentation

## Seam carving algorithm

- M(x, y)

  - minimum total energy of any seam ending at pixel (x,y)
  - Recurrence relation:
    - The function has integer inputs `x` and `y`
    - The function references/depends itself
    - The solution can be easily derived from the hyphotesis

  ```python
  M(x, 0) = e(x, 0) # the first pixel is easy to get
  M(x, y) = e(x, y) + min { # subsequent will depend on the least energy of previous surrouding pixels
      M(x - 1, y - 1)
      M(x, y - 1)
      M(x + 1, y - 1)
  }

  # solution
  M(x, H - 1)
  0 <= x < W
  W = "width of image (x)"
  H = "height of image (y)"
  ```
