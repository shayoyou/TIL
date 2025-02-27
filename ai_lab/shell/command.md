## Shell이란

운영체제의 커널과 사용자를 이어주는 소프트웨어

## Shell Command

- ls (list segments) : 현재 디렉토리의 파일 및 디렉토리 목록 표시
  - ls -l: 파일 및 디렉토리에 대한 자세한 정보를 표시
  - ls -a: 숨겨진 파일 및 디렉토리까지 표시
- cd (change directory) : 디렉토리 이동
  - cd .. : 상위 디렉토리로 이동
  - cd / : 루트 디렉토리로 이동
  - cd ~ : 홈 디렉토리로 이동
  - cd - : 이전 디렉토리로 이동
  - cd Documents : Documents 폴더로 이동
- mkdir (make directory) : 디렉토리 생성
  - mkdir [옵션] [디렉토리명]
  - mkdir -p : 중간에 없는 디렉토리까지 한 번에 생성
  - mkdir dev : dev 디렉토리 생성
- pwd (print working directory) : 현재 작업중인 디렉토리 절대경로 표시
- touch : 빈 파일 생성 또는 파일 타임스탬프 업데이트
  - touch newfile.md : newfile.md 파일 생성
- mv (move) : 파일 또는 디렉토리 이동/이름 변경
  - mv [옵션] [원본 파일/디렉토리] [대상 파일/디렉토리]
  - mv newfile.md temp/ : newfile.md 파일을 temp 디렉토리로 이동
- cp (copy) : 파일 또는 디렉토리 복사
  - cp [옵션] [원본 파일/디렉토리] [대상 파일/디렉토리]
  - cp -r : 디렉토리 및 하위 내용까지 재귀적으로 복사
- rm (remove) : 파일 또는 디렉토리 삭제
  - rm [옵션] [파일 또는 디렉토리]
  - rm -f : 강제 삭제 (삭제 확인 메시지 없음)
  - rm -r : 디렉토리 및 하위 내용까지 재귀적으로 삭제
- cat : 파일의 내용을 표준 출력(일반적으로 터미널 화면)으로 출력하는 데 사용
  - cat [파일명]
  - cat myfile.txt