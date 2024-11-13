# File Splitter and Assembler

[English](#english) | [Русский](#русский)

## English

This project contains two Python scripts for splitting large files into smaller chunks and reassembling them back into the original file.

### Scripts

1. `splitfile.py`: Splits a large file into 20MB chunks.
2. `file-make.py`: Reassembles the chunks back into the original file.

### Usage

#### Splitting a file

```
python3 splitfile.py <filename>
```

This command will create a new folder with the same name as the input file and place all the chunks inside it.

#### Assembling a file

```
python3 file-make.py <dir>
```

This command will reassemble the file from the chunks in the specified directory. The assembled file will be placed in the parent directory of the specified folder. After successful assembly, the script will:
1. Move the assembled file to the parent directory.
2. Delete all the chunk files.
3. Remove the directory that contained the chunks.

### Requirements

- Python 3.x

### Features

- Progress indicator for both splitting and assembling processes
- Error handling for common issues (file not found, directory not found, etc.)
- Automatic naming of output files and directories
- Cleanup process after successful file assembly

---

## Русский

Этот проект содержит два Python-скрипта для разделения больших файлов на меньшие части и их последующей сборки обратно в исходный файл.

### Скрипты

1. `splitfile.py`: Разделяет большой файл на части по 20 МБ.
2. `file-make.py`: Собирает части обратно в исходный файл.

### Использование

#### Разделение файла

```
python3 splitfile.py <имя_файла>
```

Эта команда создаст новую папку с тем же именем, что и входной файл, и поместит все части внутрь нее.

#### Сборка файла

```
python3 file-make.py <директория>
```

Эта команда соберет файл из частей в указанной директории. Собранный файл будет помещен в родительскую директорию указанной папки. После успешной сборки скрипт выполнит следующие действия:
1. Переместит собранный файл в родительскую директорию.
2. Удалит все файлы-части.
3. Удалит директорию, которая содержала части файла.

### Требования

- Python 3.x

### Особенности

- Индикатор прогресса для процессов разделения и сборки
- Обработка ошибок для распространенных проблем (файл не найден, директория не найдена и т.д.)
- Автоматическое именование выходных файлов и директорий
- Процесс очистки после успешной сборки файла
