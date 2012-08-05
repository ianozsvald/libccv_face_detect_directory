

import os
import cPickle
import glob
import bbfdetect_wrapper as bbf

# make sure FACES environment variable is set which points
# to the directory of test images
# e.g. source ./add_face_dir.sh (not added to git repo)

FACES = os.environ['FACES']
assert os.path.exists(FACES)

# get list of image files
image_files = glob.glob(os.path.join(FACES, '*.jpg'))

faces_libccv = {}
for img in image_files[:5]:
    print img
    img_path, img_filename = os.path.split(img)
    img_basic_root, img_final_dir = os.path.split(img_path)
    # create a filename like:
    # face-images/distilleryimage1.instagram.com_73484796a52911e180d51231380fcd7e_7.jpg
    final_path_filename = os.path.join(img_final_dir, img_filename)
    # detect faces
    output = bbf.find_faces(img)
    print len(output), output
    faces_libccv[final_path_filename] = len(output)

cPickle.dump(faces_libccv, open('faces_libccv.pickle', 'wb'))
