### 내가 수정중인 파일을 다른 사람이 먼저 수정해서 나온 에러 수정작업

```bash
$ git branch fb

$ git branch
  fb
* main

$ git switch fb
Switched to branch 'fb'

$ git status
On branch fb
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   fizzbuzz.py

no changes added to commit (use "git add" and/or "git commit -a")

$ git add fizzbuzz.py

$ git commit
[fb 3c39028] feat: remove gitignore content
 1 file changed, 1 insertion(+), 302 deletions(-)

$ git status
On branch fb
nothing to commit, working tree clean

$ git status
On branch fb
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   fizzbuzz.py

no changes added to commit (use "git add" and/or "git commit -a")

$ git add fizzbuzz.py

$ git commit
[fb 5d6b0f6] feat: implement fizzbuzz
 1 file changed, 9 insertions(+), 1 deletion(-)

$ git push -u origin fb
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 16 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 588 bytes | 588.00 KiB/s, done.
Total 6 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 1 local object.
remote:
remote: Create a pull request for 'fb' on GitHub by visiting:
remote:      https://github.com/shayoyou/team-fb-fork/pull/new/fb
remote:
To https://github.com/shayoyou/team-fb-fork.git
 * [new branch]      fb -> fb
branch 'fb' set up to track 'origin/fb'.


$ git remote add upstream https://github.com/team-fb-1004/fb.git

$ git remote -v
origin  https://github.com/shayoyou/team-fb-fork.git (fetch)
origin  https://github.com/shayoyou/team-fb-fork.git (push)
upstream        https://github.com/team-fb-1004/fb.git (fetch)
upstream        https://github.com/team-fb-1004/fb.git (push)

$ git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

$ git fetch upstream main
remote: Enumerating objects: 23, done.
remote: Counting objects: 100% (23/23), done.
remote: Compressing objects: 100% (18/18), done.
remote: Total 21 (delta 6), reused 5 (delta 1), pack-reused 0 (from 0)
Unpacking objects: 100% (21/21), 5.57 KiB | 103.00 KiB/s, done.
From https://github.com/team-fb-1004/fb
 * branch            main       -> FETCH_HEAD
 * [new branch]      main       -> upstream/main

$ git merge FETCH_HEAD
Updating 404f3a7..152badc
Fast-forward
 .github/ISSUE_TEMPLATE/bug_report.md      |  38 ++++
 .github/ISSUE_TEMPLATE/project-backlog.md |  19 ++
 100_prison.py                             |  34 ++++
 fizzbuzz.py                               | 307 +-----------------------------
 4 files changed, 96 insertions(+), 302 deletions(-)
 create mode 100644 .github/ISSUE_TEMPLATE/bug_report.md
 create mode 100644 .github/ISSUE_TEMPLATE/project-backlog.md
 create mode 100644 100_prison.py

$ git switch fb
Switched to branch 'fb'
Your branch is up to date with 'origin/fb'.

$ git branch
* fb
  main

$ git rebase main
Auto-merging fizzbuzz.py
CONFLICT (content): Merge conflict in fizzbuzz.py
error: could not apply 3c39028... feat: remove gitignore content
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
hint: Disable this message with "git config advice.mergeConflict false"
Could not apply 3c39028... feat: remove gitignore content

MINGW64 ~/Documents/dev/team-fb-fork (fb|REBASE 1/2)
$ git status
interactive rebase in progress; onto 152badc
Last command done (1 command done):
   pick 3c39028 feat: remove gitignore content
Next command to do (1 remaining command):
   pick 5d6b0f6 feat: implement fizzbuzz
  (use "git rebase --edit-todo" to view and edit)
You are currently rebasing branch 'fb' on '152badc'.
  (fix conflicts and then run "git rebase --continue")
  (use "git rebase --skip" to skip this patch)
  (use "git rebase --abort" to check out the original branch)

Unmerged paths:
  (fix conflicts and then run "git rebase --continue")
  (use "git rebase --skip" to skip this patch)
  (use "git rebase --abort" to check out the original branch)

Unmerged paths:
  (use "git rebase --skip" to skip this patch)
  (use "git rebase --abort" to check out the original branch)

Unmerged paths:
  (use "git rebase --abort" to check out the original branch)

Unmerged paths:

Unmerged paths:
Unmerged paths:
  (use "git restore --staged <file>..." to unstage)
  (use "git add <file>..." to mark resolution)
        both modified:   fizzbuzz.py

no changes added to commit (use "git add" and/or "git commit -a")

MINGW64 ~/Documents/dev/team-fb-fork (fb|REBASE 1/2)
$ git add fizzbuzz.py

MINGW64 ~/Documents/dev/team-fb-fork (fb|REBASE 1/2)
$ git rebase --continue
[detached HEAD eda7633] feat: remove gitignore content
 1 file changed, 1 insertion(+), 1 deletion(-)
Auto-merging fizzbuzz.py
CONFLICT (content): Merge conflict in fizzbuzz.py
error: could not apply 5d6b0f6... feat: implement fizzbuzz
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
hint: Disable this message with "git config advice.mergeConflict false"
Could not apply 5d6b0f6... feat: implement fizzbuzz

MINGW64 ~/Documents/dev/team-fb-fork (fb|REBASE 2/2)
$ git status
interactive rebase in progress; onto 152badc
Last commands done (2 commands done):
   pick 3c39028 feat: remove gitignore content
   pick 5d6b0f6 feat: implement fizzbuzz
No commands remaining.
You are currently rebasing branch 'fb' on '152badc'.
  (fix conflicts and then run "git rebase --continue")
  (use "git rebase --skip" to skip this patch)
  (use "git rebase --abort" to check out the original branch)

Unmerged paths:
  (use "git restore --staged <file>..." to unstage)
  (use "git add <file>..." to mark resolution)
        both modified:   fizzbuzz.py

no changes added to commit (use "git add" and/or "git commit -a")

MINGW64 ~/Documents/dev/team-fb-fork (fb|REBASE 2/2)
$ git add fizzbuzz.py

MINGW64 ~/Documents/dev/team-fb-fork (fb|REBASE 2/2)
$ git status
interactive rebase in progress; onto 152badc
Last commands done (2 commands done):
   pick 3c39028 feat: remove gitignore content
   pick 5d6b0f6 feat: implement fizzbuzz
No commands remaining.
You are currently rebasing branch 'fb' on '152badc'.
  (all conflicts fixed: run "git rebase --continue")

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   fizzbuzz.py


MINGW64 ~/Documents/dev/team-fb-fork (fb|REBASE 2/2)
$ git rebase --continue
[detached HEAD d07b926] feat: implement fizzbuzz
 1 file changed, 7 insertions(+), 3 deletions(-)
Successfully rebased and updated refs/heads/fb.

MINGW64 ~/Documents/dev/team-fb-fork (fb)
$ git push origin fb
To https://github.com/shayoyou/team-fb-fork.git
 ! [rejected]        fb -> fb (non-fast-forward)
error: failed to push some refs to 'https://github.com/shayoyou/team-fb-fork.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you want to integrate the remote changes,
hint: use 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

MINGW64 ~/Documents/dev/team-fb-fork (fb)
$ git pull
Merge made by the 'ort' strategy.

MINGW64 ~/Documents/dev/team-fb-fork (fb)
$ git status
On branch fb
Your branch is ahead of 'origin/fb' by 9 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

MINGW64 ~/Documents/dev/team-fb-fork (fb)
$ git push origin fb
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 16 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 737 bytes | 368.00 KiB/s, done.
Total 6 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), completed with 1 local object.
To https://github.com/shayoyou/team-fb-fork.git
   5d6b0f6..dc76300  fb -> fb
```
