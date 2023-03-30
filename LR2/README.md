## Install necessary libraries and run LR2

### For Windows. / 對於 Windows.

First of all you need to install Python using / 首先，您需要使用安裝 Python

[Official Python Installation Documentation / 官方 Python 安裝文檔](https://docs.python.org/3/using/windows.html#windows-full)

The Tkinter is there by default / 默認情況下 Tkinter 在那裡

Next you need to copy files from the repository / 接下來，您需要從存儲庫中復製文件
```{r, engine='bash', count_lines}
 git clone https://github.com/vasilevskykv/KG.git
```
Then you need to open LR2 folder and make necessary installations / 然後你需要打開 LR2 文件夾並進行必要的安裝


Finally, run main.py from LR2 folder / 最後，運行 main.py 從 LR2 文件夾
```{r, engine='bash', count_lines}
 python main.py
```

### For Ubuntu / 對於 Ubuntu

Check python version: / 檢查 python 版本:
```{r, engine='bash', count_lines}
 python --version
```
If python is missing, run the following command: / 如果缺少python，請運行以下命令
```{r, engine='bash', count_lines}
 sudo apt install python3.10
```
Install pip: / 安裝 pip:
```{r, engine='bash', count_lines}
 sudo apt install -y python3-pip
```
Install Tkinter: / 安裝 Tkinter:
```{r, engine='bash', count_lines}
 sudo apt-get install python3-tk
```
Next you need to copy files from the repository / 接下來，您需要從存儲庫中復製文件
```{r, engine='bash', count_lines}
 git clone https://github.com/vasilevskykv/KG.git
```
Finally, run main.py from LR2 folder / 最後，運行 main.py 從 LR2 文件夾
```{r, engine='bash', count_lines}
 python main.py
 ```
