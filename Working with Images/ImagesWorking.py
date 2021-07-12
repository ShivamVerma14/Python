from PIL import Image

words = Image.open('Working with Images\\word_matrix.png')
mask = Image.open('Working with Images\\mask.png')

mask = mask.resize((1015, 559))
mask.putalpha(200)

words.paste(mask, (0, 0), mask)
words.show()