import zipfile
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def correct_name(target_path):
    for par in os.listdir(target_path):
        for name in os.listdir(target_path + '/' +par):
            os.rename(target_path + '/' + par + '/' + name,
                target_path + '/' + par + '/'
                + name.encode('cp437').decode('utf-8'))

def unzip_data(src_path, target_path):
    if(not os.path.isdir(target_path)):    
        z = zipfile.ZipFile(src_path, 'r')
        z.extractall(path=target_path)
        z.close()
        correct_name(target_path)
    else:
        print("文件已解压")

def get_classdict(target_path):
    classdict={}
    for item in os.listdir(target_path):
        if not item=='__MACOSX':
            classdict[item] = target_path + '/' + item
    return classdict

def get_image(imagepath):
    # plt can handle Chinese path
    img = plt.imread(imagepath)
    if not img.shape==(20,20):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = np.array(img).astype('float32')
    img = np.reshape(img, 400)
    img = img/255.0
    return img

def get_class_data(classdict, classn):
    data = []
    i = list(classdict.keys()).index(classn)
    classpath = classdict[classn]
    for imagepath in os.listdir(classpath):
        imagepath = classpath + '/' + imagepath
        image = get_image(imagepath)
        label = np.zeros((len(classdict)))
        label[i] = 1
        data.append((image, label))
    return data

def get_data(classdict):
    data = []
    for i in range(len(classdict)):
        classn = list(classdict.keys())[i]
        classpath = classdict[classn]
        for imagepath in os.listdir(classpath):
            imagepath = classpath + '/' + imagepath
            image = get_image(imagepath)
            label = np.zeros((len(classdict)))
            label[i] = 1
            data.append((image, label))
    return data

def cut_license(licensepath):
    img = cv2.imread(licensepath)
    if not img.shape==(20,20):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary_plate = cv2.threshold(img, 175, 255, cv2.THRESH_BINARY)
    result = []
    for col in range(binary_plate.shape[1]):
        result.append(0)
        for row in range(binary_plate.shape[0]):
            result[col] = result[col] + binary_plate[row][col]/255
    character_dict = {}
    num = 0
    i = 0
    while i < len(result):
        if result[i] == 0:
            i += 1
        else:
            index = i + 1
            while result[index] != 0:
                index += 1
            character_dict[num] = [i, index-1]
            num += 1
            i = index
    characters = []
    for i in range(8):
        if i==2:
            continue
        padding = (170 - (character_dict[i][1] - character_dict[i][0])) / 2
        ndarray = np.pad(binary_plate[:,character_dict[i][0]:character_dict[i][1]], ((0,0), (int(padding), int(padding))), 'constant', constant_values=(0,0))
        ndarray = cv2.resize(ndarray, (20,20))
        cv2.imwrite(licensepath[:-4] + '/' + str(i) + '.png', ndarray)
        characters.append(ndarray)
    return characters