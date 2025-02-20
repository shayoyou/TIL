## 설정

git config --global user.name "{username}"  
git config --global user.email "{email}"  
git config --global core.editor "vim"  
git config --global core.pager "cat"

git config --list

수정이 필요할 경우, vim ~/.gitconfig 에서 값 수정

## 빠른시작

1. git clone {username/repo-addr}
    * 원격 저장소(repository)를 로컬 컴퓨터에 복사
    * git clone https://github.com/shayoyou/TIL.git
2. cd {repo-addr}
    - 방금 복제한 저장소 디렉토리로 이동
    - cd TIL/
3. vim README.md
    - vim 편집기로 README.md 파일 오픈
    - README.md 파일은 저장소에 대한 설명을 담고 있는 파일로, 일반적으로 저장소의 목적, 사용 방법 등을 작성한다
4. git status
    - 현재 저장소의 상태 확인
    - 수정된 파일, 새로 추가된 파일, 삭제된 파일 등의 정보를 보여준다
    - README.md 파일을 수정했으면 git status 명령어 실행시 파일이 수정된 것으로 표시된다
5. git add README.md
    - 스테이징 영역에 있는 변경 사항을 커밋
    - 스테이징 영역은 다음 커밋에 포함될 변경 사항을 준비하는 공간
6. git commit
    - 스테이징 영역에 있는 변경 사항을 커밋
    - 커밋은 변경 사항을 저장소에 기록하는 작업이다
    - git commit 명령어 실행시 커밋 메시지를 입력하라는 창이 나온다. 변경 사항에 대한 설명을 작성한다
    - -m 옵션을 사용하여 커밋 메시지를 바로 입력할 수 있지만..
7. git push origin main
    - 로컬 저장소의 변경 사항을 원격 저장소(origin)의 main 브랜치에 업로드
    - origin은 원격 저장소의 기본 이름이며, main은 기본 브랜치 이름 (경우에 따라 다를 수 있음)
