In [1]: import os

In [2]:

In [2]: os.getcwd()
Out[2]: '/Users/yuichiyamamoto'

In [3]: os.chdir('Users/yuichiyamamoto/Desktop')
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-3-6284e0aee3c5> in <module>()
----> 1 os.chdir('Users/yuichiyamamoto/Desktop')

FileNotFoundError: [Errno 2] No such file or directory: 'Users/yuichiyamamoto/Desktop'

In [4]: os.chdir('/Users/yuichiyamamoto/Desktop')

In [5]: os.makedir('newfolder')
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-5-171e68241a7c> in <module>()
----> 1 os.makedir('newfolder')

AttributeError: module 'os' has no attribute 'makedir'

In [6]: os.makedirs('newfolder')

In [7]: os.makedirs('newfolder/images')

In [8]: os.makedirs('newfolder/scripts')

In [9]: os.makedirs('newfolder/styles')

In [10]: open('index.html')
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-10-f7128f815be3> in <module>()
----> 1 open('index.html')

FileNotFoundError: [Errno 2] No such file or directory: 'index.html'

In [11]: open('index.html', 'w')
Out[11]: <_io.TextIOWrapper name='index.html' mode='w' encoding='UTF-8'>

In [12]: import shutil

In [13]: shutil.move('index.html', 'newfolder')
Out[13]: 'newfolder/index.html'
