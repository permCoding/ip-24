# ip-24
Информатика с основами программирования

[Дистант - трансляция Лекций](https://bbb.psaa.ru/rooms/clu-pi0-lck-coa/join)  

[Рейтинг ПИнб-1 ИсОП](https://docs.google.com/spreadsheets/d/1LVaA6ylPqNjshHW5J_EsH-A-WXPHCGQblsa5tadMM_I/edit?usp=sharing)  

---  


```txt
в VS Code не отображается кириллица при запуске программы:

- в settings.json меняем code-runner.executorMap
было  - "python": "python -u"
стало - "python": "set PYTHONIOENCODING=utf8 && py -u"

можно в settings добавить целый раздел:

    "code-runner.executorMap": {
        "javascript": "node",
        "php": "C:\\php\\php.exe",
        "python": "set PYTHONIOENCODING=utf8 && py -u",
        "perl": "perl",
        "ruby": "C:\\Ruby23-x64\\bin\\ruby.exe",
        "go": "go run",
        "html": "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"",
        "java": "cd $dir && javac $fileName && java $fileNameWithoutExt",
        "c": "cd $dir && gcc $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "cpp": "cd $dir && g++ -std=c++14 $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt"
    },

```

---  

```txt
Включение альтернативной версии Python

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 2

sudo update-alternatives --list python3

update-alternatives --config python3

sudo apt install python3-pip

sudo python3.12 -m pip install --upgrade pip

sudo apt-get install python-is-python3

sudo apt autoremove

переустановка pip:
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py 
sudo python3.12 get-pip.py 
```

---  

```txt
venv

sudo apt install -y python3.12-venv
  или: sudo apt install -y python3-venv
  иногда: sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
python -m venv myenv
source myenv/bin/activate
для выхода: deactivate
```

