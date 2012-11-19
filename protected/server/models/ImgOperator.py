import Image,os,sys,glob
class ImgOperator(object):
	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.canvas = Image.new("RGB", [self.width, self.height],0xffffff)
	def mergeImage(self,):
		pass
	def saveToPng(self,path):
		self.canvas.save(path,"PNG")
	def make_thumb(self,path, thumb_path, size):
		img = Image.open(path)
		width, height = img.size
		if width > height:
			delta = (width - height) / 2
			box = (delta, 0, width - delta, height)
			region = img.crop(box)
		elif height > width:
			delta = (height - width) / 2
			box = (0, delta, width, height - delta)
			region = img.crop(box)
		else:
			region = img
		thumb = region.resize((size, size), Image.ANTIALIAS)

		base, ext = os.path.splitext(os.path.basename(path))
		filename = os.path.join(thumb_path, '%s_thumb.jpg' % (base,))
		print filename
		thumb.save(filename, quality=70)
		def merge_thumb(files, output_file):
			imgs = []
			width = 0
			height = 0
			for file in files:
				img = Image.open(file)
				if img.mode != 'RGB':
				    img = img.convert('RGB')
				imgs.append(img)
				if img.size[0] > width:
				    width = img.size[0]
				height += img.size[1]

			# 新建一个白色底的图片
			merge_img = Image.new('RGB', (width, height), 0xffffff)
			cur_height = 0
			for img in imgs:
				merge_img.paste(img, (0, cur_height))
				cur_height += img.size[1]

			merge_img.save(output_file, quality=70)

if __name__=="__main__":
	ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
	IMG_PATH = os.path.join(ROOT_PATH, 'images')
	THUMB_PATH = os.path.join(IMG_PATH, 'thumbs')
	print THUMB_PATH
	if not os.path.exists(THUMB_PATH):
		os.makedirs(THUMB_PATH)
	files = glob.glob(os.path.join(IMG_PATH, '*.jpg'))
	img = ImgOperator(188,195)
	img.saveToPng("aa.png")
	for file in files:
		img.make_thumb(file, THUMB_PATH, 90)
