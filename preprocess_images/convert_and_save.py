import os
from PIL import Image

#Mount your gdrive if the activity is being done on colab
from google.colab import drive
drive.mount("/content/gdrive")

saveto_path = "/content/gdrive/My Drive/filename_of_original_images/"
image_path = "/content/gdrive/My Drive/filename_where_padded_images_have_to_be_saved/"

def avg(lst):
    return sum(lst) // len(lst)
  
def add_margin(pil_img, top, tup):
    width, height = pil_img.size
    result = Image.new(mode=pil_img.mode, size=(300, 300), color=tup)
    result.paste(pil_img, (0, top))
    return result

ct=0

#iterate over the filenames in the given directory
for filename in os.listdir(image_path):
  
  #following lines are just for convenience. 
  #Check in the target folder if the images have been
  #saved just as you liked and then comment the below 4 lines
  ct+=1
  if(ct==6):
    break
  print(ct)
  
  #open the image as img
  im1 = image_path + filename;
  img = Image.open(im1).convert('L')
  
  #resize the image
  w, h = img.size;
  imgres = img.resize((300, h*300//w))

  #store new image sizes as nh and nw
  nw, nh = imgres.size;
  
  #convert the image to RGB to get colour channel values so as to pad with a suitable colour
  rgb_im = imgres.convert('RGB')
  
  #Now, we take two squares (topmost-leftmost and topmost-rightmost) of 5x5 size pixel and put their R,G,B values in rc, gc and bc lists.
  #Then we take the average of the lists and feed it as color in the add_margin function.
  rc=[]
  gc=[]
  bc=[]
  for i in range(0, 5):
    for j in range(0, 5):
      r, g, b = rgb_im.getpixel((i, j))
      rc.append(r);
      gc.append(g);
      bc.append(b);

  for i in range(nw-5, nw):
    for j in range(0, 5):
      r, g, b = rgb_im.getpixel((i, j))
      rc.append(r);
      gc.append(g);
      bc.append(b);
      
  tup = (avg(rc), avg(gc), avg(bc))
  
  #convert to hex values as only 6-colour codes are supported by the Image.new function inside add_margin
  #Reference: https://stackoverflow.com/questions/3380726/converting-a-rgb-color-tuple-to-a-six-digit-code
  bo = '#%02x%02x%02x' % tup
  res = add_margin(imgres, (300-nh)//2, bo)
  
  #save file
  res.save(saveto_path+filename[:len(filename)-4]+".jpeg", format="jpeg")
