import os

directory = "/var"
for root, dirs, files in os.walk("/var"):
   #for name in files:
   #   print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))
