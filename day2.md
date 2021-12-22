# Github

**Github 회원가입**

- 회원가입 시 유의사항
  1. 회원가입 후 Github 설정을 변경해야
     - Settings  → Repositories → Repository default branch → main삭제하고 master로 작성

```
main VS master

2020년 Black Lives MAtter(아프리카계 미국인 인종차별반대운동) 당시 master가 주인과 노예(master and slave)를 상기시킨다고 생각해 master 대신 main이라는 이름으로 기존 브랜치 이름을 변경 (하지만 아직 많은 곳에서 master를 사용하기 때문에 현 수업에서는 master 사용)
```

---

# push

**원격 저장소**

> 로컬 저장소에서만 버전 관리를 하지 않고, Github의 원격 저장소를 이용해서 내 컴퓨터의 로컬 저장소를 다른 사람과 공유할 수 있다.
>
> Git의 주요 목적(백업, 복구, 협업)인 협업을 위해 로컬 저장소와 원격 저장소의 연동은 중요하다.
>
> push는 로컬 저장소의 내용을 원격 저장소에 업로드



- 원격 저장소 생성

  1.  \+ 버튼 누르고 New repository

  2. 생성 후 저장소의 주소 복사

  3. vscode 들어간 후

     - `git init`

     - `git remote add origin(이름) <주소>`

     - `git remote -v`

       (만약 삭제하고 싶다면 `git remote rm origin`)

  4. 원격 저장소에 업로드(커밋)

     - git add .
     - git commit -m "내용"
     - git log --oneline (확인)
     - git push origin(이름) master(브랜치 이름)

     `-u 옵션을 사용하면(push 뒤에) 그냥 git push만 써도 실행 ㅇ`

  5. vscode 자격 증명

     - Authorize 클릭

  6. 원격 저장소에서 정상 업로드 확인

  ```
  !주의!
  Github 원격 저장소에 절대로 파일을 드래그해서 업로드하면 안된다.
  
  반드시 git add → git commit → git push 의 단계로만 업로드해야
  로컬 저장소에서 변경이 먼저 일어나고, 그 변경 사항을 원격 저장소에 반영하는 형태여야 한다.
  ```

  

![git push](https://hphk.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F357df618-2ddf-4f18-b96c-c1b0787a1a45%2FUntitled.png?table=block&id=03914929-4534-4612-82e0-ed32d45b3e25&spaceId=daa2d103-3ecd-4519-8c30-4f55e74c7ef4&width=2000&userId=&cache=v2)



- README.md
  1. `README.md`는 원격 저장소의 소개와 설명이 담겨있는 대문 역할
  2. 반드시 파일 이름을 `README.md`라고 지정해야 Github가 인식

---

# .gitignore

> 특정 파일 혹은 폴더에 대해 Git이 버전 관리를 하지 못하도록 지정



- 어디에 사용?

  - 민감한 개인정보가 담긴 파일(전화번호, 계좌번호 등)
  - OS에서 활용되는 파일
  - IDE혹은 Text editor(vscode) 등에서 활용되는 파일
  - 개발 언어 혹은 프레임워크에서 사용되는 파일

  

- 작성 시 주의 사항

  - 반드시 이름을 `.gitignore`로 작성(앞의 점은 숨김 파일이라는 뜻)

  - `.gitignore`파일은 `.git`폴더와 동일한 위치에 생성

  - 제외하고 싶은 파일은 반드시 `git add`전에 `.gitignore`에 작성해야

    ```
    왜 git add 전에 .gitignore에 작성해야 할까?
    
    git add를 하면, 이제 Git은 그 파일을 버전 관리의 대상으로 여김.
    한 번 버전 관리의 대상이 된 파일은 이후에 .gitignore에 작성해도 무시되지 않고 계속 버전관리의 대상으로 인식됨.
    ```

     

- .gitignore 쉽게 작성하는 법

  - [Toptal](https://gitignore.io/)

  - [Github](https://github.com/github/gitignore)

     

- .gitignore 사용해보기

  - 패턴 규칙

    - 아무것도 없는 라인이나, `#`으로 시작하는 라인은 무시

    - `슬래시(/)`로 시작하면, 하위 디렉터리에 재귀적으로 적용되지 x

    - 디렉토리는 `슬래시(/)`를 끝에 사용하는 걸로 표현

    - `느낌표(!)`로 시작하는 패턴의 파일은 ignore하지 x

    - 표준 Glob 패턴 사용

      1. `*(asterisk, wildcard)`는 문자가 하나도 없거나 하나 이상

      2. `[abc]`는 중괄호 안에 있는 문자 중 하나

      3. `물음표(?)`는 문자 하나

      4. `[0-9]`처럼 하이픈 있을 땐 0에서 9사이 문자 중 하나

      5. `**(2개의 asterisk)`는 디렉토리 내부의 디렉토리까지 지정 가능

         (`a/**/z`라고 작성하면 `a/z`, `a/b/z`, `a/b/c/z`까지 모두 영향)

---

# clone, pull

**원격저장소 가져오기**

> 원격 저장소의 내용을 로컬 저장소로 가져오기



- git clone

  - 원격저장소의 커밋 내역 모두 가져와서 로컬 저장소 생성
  - clone은 복제라는 뜻, `git clone`명령어를 사용하면 원격 저장소를 통째로 복제해서 옮길 수 ㅇ
  - `git clone <주소>`
  - git clone을 이용해 생성된 로컬 저장소는 git init과 git remote add가 이미 수행되어 있음

- git pull

  - 원격 저장소의 변경사항을 가져와서 로컬 저장소를 업데이트
  - git pull origin master

  ```
  git clone VS git pull
  
  둘 다 모두 원격 저장소로부터 가져오는 명령어이지만,
  git clone은 한 번만 실행. 로컬 저장소를 만드는 역할
  git pull은 동기화 하고싶을 때 언제든지 사용
  ```

  

