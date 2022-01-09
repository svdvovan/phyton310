import zipfile
import os


# z = zipfile.ZipFile('F:/spam.zip', 'w')
# for root, dirs, files in os.walk('F:/folder'):
#     for file in files:
#         z.write(os.path.join(root, file))
#
# z.close()
z = zipfile.ZipFile('F:/spam.zip', 'r')
z.printdir()

z.close()