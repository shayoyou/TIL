## git을 쓰면서 습관들이면 안되는 것들

- $ git add . : 현재 디렉토리 하위의 모든 파일을 staging할 때 사용. but, 현재 commit단위에 들어가면 안되는 파일까지 휩쓸릴 수 있으므로 습관적으로 사용하면 안됩니다.
- $ git commit -m "Message" : 쉘에서 바로 메시지를 쓰면서 커밋할 때 사용. but, revert commit, merge commit 등의 상황에서 메시지를 덮어쓸 우려가 있으므로 습관적으로 사용하면 안됩니다.
- 저장소 안에 저장소 clone 하기 : 프로젝트 단위는 항상 독립적으로 존재해야 합니다. clone 전 항상 현재 작업위치가 dev 디렉토리인지 확인 후 사용!!
- 의미없는 commit message 남기기(ex. a, 1, ..) : commit message는 제목만으로 해당 작업단위에 대한 설명이 가능해야 나중에 고생하지 않습니다. Conventional commit 잘 지키기!!
