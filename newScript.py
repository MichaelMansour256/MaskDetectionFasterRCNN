from bs4 import BeautifulSoup
import glob
import csv


def remove_space(text):
    text = text.replace("\n", "")
    text = text.replace(" ", "")
    return text


xml_files = glob.glob('dataset/train/annotations/*.xml')
all_rows = []
for i in xml_files:
    infile = open(i, "r")
    contents = infile.read()
    soup = BeautifulSoup(contents, 'lxml')
    annotations = soup.find("annotation")
    file_name = remove_space(soup.find("filename").get_text())
    objects = annotations.findAll("object")
    for o in objects:
        class_name = remove_space(o.find("name").get_text())
        x_min = remove_space(o.find("xmin").get_text())
        y_min = remove_space(o.find("ymin").get_text())
        x_max = remove_space(o.find("xmax").get_text())
        y_max = remove_space(o.find("ymax").get_text())
        all_rows.append([file_name, class_name, x_min, y_min, x_max, y_max])


with open('data2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(all_rows)
