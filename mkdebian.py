import fnmatch
import os
import shutil
import subprocess
import tarfile

basedir = 'debian_build'
module = 'cpl'

os.mkdir(basedir)
os.mkdir(os.path.join(basedir, module))
os.mkdir(os.path.join(basedir, 'debian'))
tar = tarfile.open('python-cpl.tar.gz', mode='w:gz')

shutil.copy('setup.py', basedir)
tar.add('setup.py')
shutil.copy('README', basedir)
tar.add('README')

files = fnmatch.filter(os.listdir(module), '*.py') + ['CPL_recipe.c']
for fname in files:
    shutil.copy(os.path.join(module, fname), os.path.join(basedir, module))
    tar.add(os.path.join(module, fname))

tar.close()

for fname in ['compat', 'control', 'copyright', 'docs', 'rules', 'changelog' ] :
    shutil.copy(os.path.join('debian', fname), os.path.join(basedir, 'debian'))

os.chdir(basedir)
subprocess.call(['dpkg-buildpackage', '-S'])

os.chdir('..')
#subprocess.call(['dput', 'ppa:olebole/astro', 'python-cpl_0.1.0-3_source.changes'])
