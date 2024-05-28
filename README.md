# Steps to reproduce problem

1. Build Docker image: `docker build . -t debug-datadirs --build-arg PIP_VERSION='22.2.2'`

2. Run container, install package, and check installed files:
```sh
docker run -v .:/app debug-datadirs -c 'pip3 -v install /app && ls -l /usr/local/lib/python3.10/dist-packages/some_package/data'
```

This produces:
```
Using pip 22.2 from /usr/local/lib/python3.10/dist-packages/pip (python 3.10)
Processing /app
  Installing build dependencies: started
  Running command pip subprocess to install build dependencies
  Collecting setuptools==70.0.0
    Downloading setuptools-70.0.0-py3-none-any.whl (863 kB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 863.4/863.4 kB 4.1 MB/s eta 0:00:00
  Installing collected packages: setuptools
  Successfully installed setuptools-70.0.0
  WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

  [notice] A new release of pip available: 22.2 -> 24.0
  [notice] To update, run: python3 -m pip install --upgrade pip
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Running command Getting requirements to build wheel
  running egg_info
  creating debug_datadirs.egg-info
  writing manifest file 'debug_datadirs.egg-info/SOURCES.txt'
  writing manifest file 'debug_datadirs.egg-info/SOURCES.txt'
  Getting requirements to build wheel: finished with status 'done'
  Installing backend dependencies: started
  Running command pip subprocess to install backend dependencies
  Collecting wheel
    Downloading wheel-0.43.0-py3-none-any.whl (65 kB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 65.8/65.8 kB 720.0 kB/s eta 0:00:00
  Installing collected packages: wheel
  Successfully installed wheel-0.43.0
  WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

  [notice] A new release of pip available: 22.2 -> 24.0
  [notice] To update, run: python3 -m pip install --upgrade pip
  Installing backend dependencies: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Running command Preparing metadata (pyproject.toml)
  running dist_info
  creating /tmp/pip-modern-metadata-frifq1ce/debug_datadirs.egg-info
  writing manifest file '/tmp/pip-modern-metadata-frifq1ce/debug_datadirs.egg-info/SOURCES.txt'
  writing manifest file '/tmp/pip-modern-metadata-frifq1ce/debug_datadirs.egg-info/SOURCES.txt'
  Preparing metadata (pyproject.toml): finished with status 'done'
Building wheels for collected packages: debug-datadirs
  Building wheel for debug-datadirs (pyproject.toml): started
  Running command Building wheel for debug-datadirs (pyproject.toml)
  running bdist_wheel
  running build
  running build_py
  creating build
  creating build/lib
  creating build/lib/some_package
  copying some_package/__init__.py -> build/lib/some_package
  creating build/lib/some_package/data
  copying some_package/data/__init__.py -> build/lib/some_package/data
  copying some_package/data/file1.txt -> build/lib/some_package/data
  running install
  running install_lib
  creating build/bdist.linux-aarch64
  creating build/bdist.linux-aarch64/wheel
  creating build/bdist.linux-aarch64/wheel/some_package
  copying build/lib/some_package/__init__.py -> build/bdist.linux-aarch64/wheel/some_package
  creating build/bdist.linux-aarch64/wheel/some_package/data
  copying build/lib/some_package/data/file1.txt -> build/bdist.linux-aarch64/wheel/some_package/data
  copying build/lib/some_package/data/__init__.py -> build/bdist.linux-aarch64/wheel/some_package/data
  running install_egg_info
  running egg_info
  writing manifest file 'debug_datadirs.egg-info/SOURCES.txt'
  Copying debug_datadirs.egg-info to build/bdist.linux-aarch64/wheel/debug_datadirs-0.1.0.egg-info
  running install_scripts
  Building wheel for debug-datadirs (pyproject.toml): finished with status 'done'
  Created wheel for debug-datadirs: filename=debug_datadirs-0.1.0-py3-none-any.whl size=1565 sha256=1c8d7b80728491397922630e418a69a57276a49bef030d575e789376a3adf2a7
  Stored in directory: /tmp/pip-ephem-wheel-cache-pliuep_h/wheels/9b/2c/d1/15e20a2b97f37ccf65a87ba1049c73a9076d0bf0fbaf814e83
Successfully built debug-datadirs
Installing collected packages: debug-datadirs
Successfully installed debug-datadirs-0.1.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

[notice] A new release of pip available: 22.2 -> 24.0
[notice] To update, run: python3 -m pip install --upgrade pip
total 8
-rw-r--r-- 1 root root    0 May 28 09:50 __init__.py
drwxr-xr-x 2 root root 4096 May 28 09:50 __pycache__
-rw-r--r-- 1 root root   10 May 28 09:50 file1.txt
```
Note the absence of `some_package/data/subdir`.
Running with `PIP_VERSION='23.0.0'` installs the directories properly.
