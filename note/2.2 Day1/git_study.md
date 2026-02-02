# 🚀 git_study

## 一、 Git 7 大命令

| **命令**         | **用法**                   | **解析**                                                     |
| ---------------- | -------------------------- | ------------------------------------------------------------ |
| **`git init`**   | `git init`                 | **仓库初始化**。在文件夹里生成 `.git` 隐藏文件夹。没有它，Git 就不干活。 |
| **`git clone`**  | `git clone <url>`          | **下载项目**。把 GitHub 上的代码库完整地搬到本地。           |
| **`git status`** | `git status`               | **状态查询**。Git 的“眼睛”，告诉你哪些文件改了、哪些还没提交。 |
| **`git add`**    | `git add .`                | **添加暂存**。把“工作区”的修改放入“暂存区”。`.` 代表当前目录下所有文件。 |
| **`git commit`** | `git commit -m "说明"`     | **提交快照**。正式保存。注意：如果没有设置 `user.name`，这一步会报错。 |
| **`git push`**   | `git push <远程名> <分支>` | **上传云端**。把本地记录推送到 GitHub。第一次推建议加 `-u`。 |
| **`git pull`**   | `git pull <远程名> <分支>` | **拉取同步**。下载远程最新代码并自动合并到本地。             |

------

## 二、 两种建仓姿势

### 方案 A：先有远程，再关联本地

1. **GitHub 网页端**：新建 Repository，勾选 `Add a README.md`。

2. **本地克隆**：

   Bash

   ```
   git clone https://github.com/用户名/仓库名.git
   ```

3. **直接开写**：文件已经在本地了，直接 `add` -> `commit` -> `push`。

### 方案 B：先有本地，后关联远程

1. **本地初始化**：

   ```bash
   mkdir 仓库名 && cd 仓库名
   git init
   touch README.md     # 创建说明文档
   ```

   ### 2. 身份配置（查户口）

   **必须在第一次 commit 前完成，否则会报错。**

   ```bash
   git config --global user.name "你的名字"
   git config --global user.email "你的邮箱"
   ```

   ### 3. 本地提交

   ```bash
   git add .
   git commit -m "初始项目结构提交"
   ```

   ### 4. 关联远程仓库

   ```bash
   # 这里的 origin 是远程仓库的代号，你可以起名叫 origin 或 QG
   git remote add origin https://github.com/用户名/仓库名.git
   ```

   ### 5. 同步与推送

   **注意：** 如果你在 GitHub 网页端勾选了“创建 README”，必须要先 pull。

   ```bash
   # 强制拉取远程文件并与本地合并
   git pull origin master --rebase
   
   # 正式推送到 GitHub
   git push -u origin master
   ```

------

## 三、 分支管理命令

分支让你在不破坏主线代码（master/main）的前提下，自由尝试新功能。

- **查看分支**：`git branch`
- **创建分支**：`git branch <新名字>`
- **切换分支**：`git checkout <名字>` 或 `git switch <名字>`
- **创建并秒切**：`git checkout -b <新名字>`
- **合并分支**：先切换回 master，再执行 `git merge <要合并的分支名>`
- **删除分支**：`git branch -d <名字>`

***

