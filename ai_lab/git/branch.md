## 브랜치 확인

- git branch
- 현재 작업중인 브랜치 앞에 *표시되어 보인다
- -a 옵션: 로컬 및 원격 브랜치 모두 확인 (git branch -a)
- -r 옵션: 원격 브랜치만 확인

## 브랜치 생성

- git branch <브랜치 이름>
- ex) git branch origin/sample

## 브랜치 변경

- git switch <브랜치 이름>

## 로컬 브랜치 삭제

- git branch -d <브랜치 이름>: 병합된 브랜치 삭제
  - 해당 브랜치가 현재 브랜치에 병합된 경우에만 삭제된다
  - 병합되지 않은경우, 에러메시지와 함께 삭제가 거부된다

- git branch -D <브랜치 이름>: 병합 여부와 관계없이 강제 삭제
  - 주의: 복구 불가능