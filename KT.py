from PIL import Image, ImageFilter, ImageChops, ImageDraw

def find_contours_pillow(input_img, output_path):
    img = input_img.convert('RGB')
    result = img.copy()
    draw = ImageDraw.Draw(result)
      
    gray = img.convert('L')
      
    edges = gray.filter(ImageFilter.FIND_EDGES)
      
    edges = edges.point(lambda p: 255 if p > 50 else 0)
      
    width, height = edges.size
    pixels = edges.load()
      
    for x in range(width):
        for y in range(height):
            if pixels[x, y] > 200:
                draw.point((x, y), fill='green')
      
    result.save(output_path)

with Image.open("example.jpg") as f:
  img = f.convert('L')
  img = f.filter(ImageFilter.MedianFilter(size=5))
  find_contours_pillow(img, 'result.jpg')
