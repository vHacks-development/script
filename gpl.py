import os, sys

os.system("clear")
plugins = []
host = "localhost:2024"

path = "/sdcard/Download"
for file in os.listdir(path):
	if file[-4:] == ".jar":
		newName = file.replace(" ", "_")
		os.rename(f"{path}/{file}", f"{path}/{newName}")
		plugins.append(f"{host}{path[7:]}/{newName}")

template = f" ".join(plugins)
print(f'\n\nRun this: wget {template}')
