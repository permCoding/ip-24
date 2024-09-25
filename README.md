# ip-24
Информатика с основами программирования

[Дистант - трансляция Лекций](https://bbb.psaa.ru/rooms/clu-pi0-lck-coa/join)  

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