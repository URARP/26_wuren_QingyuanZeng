#!/bin/bash

# 1. 创建 linux_practice 文件夹及其子目录
mkdir -p linux_practice/{docs,backup}

# 2. 在 docs 目录下创建三个文件
touch linux_practice/docs/readme.txt linux_practice/docs/notes.log linux_practice/docs/temp.tmp

# 3. 删除 temp.tmp，将 notes.log 重命名为 daily_report.txt
rm linux_practice/docs/temp.tmp
mv linux_practice/docs/notes.log linux_practice/docs/daily_report.txt

# 4. 写入内容到 daily_report.txt
echo "Project Status: Active" > linux_practice/docs/daily_report.txt
date >> linux_practice/docs/daily_report.txt

# 5. 将 docs 下的所有 .txt 文件复制到 backup
cp linux_practice/docs/*.txt linux_practice/backup/

# 6. 修改 backup 目录下所有文件权限为只读
chmod 444 linux_practice/backup/*

# 输出完成信息
for file in linux_practice/backup/*; do
    if [ -f "$file" ]; then
        echo "Archive Complete. File [$file] is now read-only"
    fi
done