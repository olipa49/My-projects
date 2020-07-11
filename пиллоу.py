# импортируем необходимые модули
from PIL import Image, ImageFilter

try:
	# загружаем изображение с жесткого диска
	original = Image.open("pythonru-280x96.png")
except FileNotFoundError:
	print("Файл не найден")

# размываем изображение
blurred = original.filter(ImageFilter.BLUR)
# открываем оригинал и размтое изображение
original.show()
blurred.show()
# сохраняем изображение
blurred.save("blurred.png")






