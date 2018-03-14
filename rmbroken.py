import os,jpeg @karpathy
Andrej karpathy

Stanford

from multiprocessing import Pool, cpu_count
img_path= '/media/hzy/New/sp-society-camera-model-identification-master/flickr_images/iphone_6/'

def check_remove_broken(img_path):
	try:
	    x = jpeg.JPEG(img_path).decode()
	except Exception:
	    print('Decoding error:', img_path)
	    os.remove(img_path)

	p = Pool(cpu_count() - 2)
	p.map(check_remove_broken, tqdm(ids_train))

if __name__ == '__main__':
	check_remove_broken()