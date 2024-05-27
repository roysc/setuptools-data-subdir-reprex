# Steps to reproduce problem

Run:

    docker build . -t debug-datadirs
    docker run -v .:/app debug-datadirs -c 'pip3 install /app && ls -l /usr/local/lib/python3.10/dist-packages/some_package/data'

This produces:

    Processing /app
      Installing build dependencies: started
      Installing build dependencies: finished with status 'done'
      Getting requirements to build wheel: started
      Getting requirements to build wheel: finished with status 'done'
      Installing backend dependencies: started
      Installing backend dependencies: finished with status 'done'
      Preparing metadata (pyproject.toml): started
      Preparing metadata (pyproject.toml): finished with status 'done'
    Building wheels for collected packages: debug-datadirs
      Building wheel for debug-datadirs (pyproject.toml): started
      Building wheel for debug-datadirs (pyproject.toml): finished with status 'done'
      Created wheel for debug-datadirs: filename=debug_datadirs-0.1.0-py3-none-any.whl size=1565 sha256=aae7346ab71998589ddd9f2ff4f71386d1b71161ebe343d4ea41ef2cf434bef9
      Stored in directory: /tmp/pip-ephem-wheel-cache-5v9hagcv/wheels/9b/2c/d1/15e20a2b97f37ccf65a87ba1049c73a9076d0bf0fbaf814e83
    Successfully built debug-datadirs
    Installing collected packages: debug-datadirs
    Successfully installed debug-datadirs-0.1.0
    WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
    total 8
    -rw-r--r-- 1 root root    0 May 28 09:06 __init__.py
    drwxr-xr-x 2 root root 4096 May 28 09:06 __pycache__
    -rw-r--r-- 1 root root   10 May 28 09:06 file1.txt

Note the absence of `some_package/data/subdir`.
