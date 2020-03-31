###############################################
#                                             #
#       Created by Youssef Sully              #
#       Beginner python                       #
#       File handling 3                       #
#                                             #
###############################################

# open write1.txt to write if NOT exist creates one
with open('to_write.txt', 'w') as write1_file:
    write1_file.seek(20)  # set file current position to 10
    write1_file.write('First')
    write1_file.seek(30)  # set file current position to 30
    write1_file.write('Second')
    write1_file.write('\n')
    write1_file.write('Third')
    write1_file.write('\t')
    write1_file.write('Fourth')
    write1_file.seek(0)  # set file current position to 0
    write1_file.write('Not first anymore')

# copying text file

with open('to_write.txt', 'r') as read_file:
    with open('to_copy.txt', 'w') as write_file:
        for line in read_file:
            write_file.write(line)

# copying image
# r for reading and b for binary used for images (rb)
# w for writing and b for binary used in images (wb)
with open('image.jpg', 'rb') as read_img_file:
    with open('image_copy.jpg', 'wb') as write_img_file:
        for line in read_img_file:
            write_img_file.write(line)