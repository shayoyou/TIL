# Conventional Commits

[https://www.conventionalcommits.org/ko/v1.0.0/](https://www.conventionalcommits.org/ko/v1.0.0/)

Conventional Commits는 커밋 메시지를 작성하기 위한 규칙입니다. 일관된 커밋 히스토리를 만들어 프로젝트 협업 및 관리를 용이하게 하는 것이 목표입니다.

## 주요 특징

- 구조화된 메시지: 커밋 메시지는 유형, 범위, 제목, 본문, 꼬리말로 구성됩니다.
- 명확한 유형: 변경 사항의 유형을 명확히 나타내는 키워드를 사용합니다 (예: feat, fix).
- 간결한 제목: 커밋의 주요 내용을 50자 이내로 요약합니다.

## 구조

```md
<type>(<scope>): <subject>

<body>

<footer>
```

- type: 커밋 유형 (필수)
   - feat: 새로운 기능 추가
   - fix: 버그 수정
   - docs: 문서 수정
   - build: 빌드 작업 관련
   - ci: Continuous Integration 관련
   - style: 코드 스타일 수정 (코드 동작에 영향을 주지 않음)
   - refactor: 코드 리팩토링
   - test: 테스트 추가 또는 수정
   - chore: 빌드 작업, 패키지 매니저 설정 등 (코드 생산과 직접 관련 없음)
   - conf: 환경설정 관련
- scope: 변경 사항이 적용되는 범위 (선택 사항)
- subject: 커밋 제목 (필수) - 50자 이내, 명령형으로 작성
- body: 커밋에 대한 자세한 설명 (선택 사항) - 72자마다 줄 바꿈
- footer: 관련 이슈 번호, breaking change 등 추가 정보 (선택 사항)

## 장점

- 가독성 향상: 일관된 형식으로 커밋 히스토리를 쉽게 파악할 수 있습니다.
- 자동화: 커밋 메시지를 분석하여 자동으로 버전 번호를 생성하거나 릴리스 노트를 작성할 수 있습니다.
- 협업 개선: 명확한 커밋 메시지는 팀원 간의 코드 이해도를 높여 협업을 원활하게 합니다.
