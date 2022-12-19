from pathlib import Path

files = [f.stem.split('_')[-1] for f in list(Path.cwd().glob('*.zip'))]
print(files)