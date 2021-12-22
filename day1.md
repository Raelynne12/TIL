# GUI / CLI



**GUI(Graphic User Interface)**

\- 그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식



**CLI(Command Line Interface)**

\- 터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식



```
Interface(인터페이스)

서로 다른 개체끼리 맞닿아 있는 면
여기에서는 사용자와 컴퓨터가 서로 소통하는 '접점'
```



|         GUI          |         CLI          |
| :------------------: | :------------------: |
|    사용하기 편리     |   사용하기 어려움    |
| 컴퓨터의 성능 소모 ↑ | 컴퓨터의 성능 소모 ↓ |



---

# Git Bash



**Git Bash란?**

\- 최초의 *유닉스 쉘 프로그램인 sh의 확장판*



```
Shell Program(쉘 프로그램)

키보드로 입력한 명령어(command)를 운영체제에 전달해서 실행하게끔 하는 프로그램
```

 

**Git Bash를 사용하는 이유**

1. 명령어의 통일을 위해

   - UNIX 계열 운영체제의 명령어(MAX OS, Linux)와 Windows의 명령어 차이 有

   - Git Bash(번역기)를 사용하면 Windows에서도 UNIX 계열 명령어 사용 가능

     

2. UNIX 계열 운영체제의 명령어를 더 많이 사용하기 때문

   - 개발자 입장에서는 UNIX 계열 운영체제 기반 프로그램이 훨씬 많음



---

# 명령어



**Directory**

1. 루트 디렉토리 (**/**)

   - 모든 파일과 폴더를 담고 있는 최상위 폴더

   - 보통 C드라이브

     

2. 홈 디렉토리 (**~**)
   - (=Tilde), 현재 로그인 된 사용자의 폴더
   - Window에서는 C:/Users/현재 사용자 계정



```
폴더 VS 디렉토리

거의 같은 의미라서 구분이 무의미
굳이 따지면 폴더가 디렉토리보다 넓은 개념(내컴퓨터 이런 건 폴더지만 디렉토리는 아님)
```



**Root**

1. 절대 경로

   - 루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성

   - `C:/Users/Raelynne/Desktop`

     

2. 상대 경로

   - 현재 위치 기준으로 계산된 상대적 위치 작성
   - 간결하지만, 작업 중인 디렉토리 변경되면 같이 변경
   - `./`  : 현재 작업중인 폴더
   - `../` :  `./`의 부모 폴더



**Terminal Command**

1. `touch`

   - 파일 생성

   - 띄어쓰기 사용 -> 한 번에 여러 개 파일 생성 가능

   - 숨김 파일을 만들 때는 `.`를 파일명 앞에 붙임

     ```bash
     $ touch text.txt
     ```

     

2. `mkdir`

   - 새 폴더 생성

   - 띄어쓰기 사용 -> 한 번에 여러 개 폴더 생성 가능

   - 폴더 사이 공백을 넣을 때는 따옴표로 묶음

     ```bash
     $ mkdir folder
     $ mkdir 'happy hacking'
     ```

3. `ls`

   - 현재 작업 중인 디레고리의 폴더/파일 목록 보여줌

   - `-a` : all 옵션. 숨김 파일까지 모두 보여줌

   - `-l` : long 옵션. 용량, 수정 날짜 등 파일 정보 자세히 보여줌

     

4. `mv`

   - 폴더/파일을 다른 폴더 내로 이동 or 이름 변경

   - 다른 폴더로 이동 시 작성한 폴더가 반드시 있어야, 없으면 이름 바뀜

     ```bash
     # text.txt를 foldr 폴더 안에 넣을 때
     $ mv text.txt folder
     
     #text.txt의 이름을 text2.txt로 바꿀 때
     $ mv text.txt text2.txt
     ```

      

5. `cd`

   - 현재 작업 중인 디렉토리 변경

   - `cd ~ ` 입력하면 홈 디렉토리로 이동(그냥 `cd`라고만 써도 가능)

   - `cd ..` : 부모 디렉토리(위로 가기)

   - `cd -` : 바로 전 디렉토리(뒤로 가기)

     

6. `rm`

   - 폴더/파일 지우는 명령어

   - *완전 삭제*

   - `-r` : recursive 옵션. 폴더를 지울 때

     ```bash
     $ rm test.txt
     $ rm -r folder
     ```

      

7. `start, open`

   - 폴더/ 파일 여는 명령어

   - Windows에서는 start

     ```bash
     $ start test.txt
     ```

      

8. 유용한 단축키

   - `위, 아래 방향키` : 과거에 작성했던 명령어 조회
   - `tab` : 폴더/ 파일 이름 자동 완성
   - `ctrl + a` : 커서가 맨 앞으로 이동
   - `ctrl + e` : 커서가 맨 뒤로 이동
   - `ctrl + w` : 커서가 앞 단어를 삭제
   - `ctrl + l` : 터미널 화면을 깨끗하게 청소(스크린 내려간 거)
   - `ctrl + insert` : 복사
   - `ctrl + insert` : 붙여넣기



---

# Markdown



**Markdown이란?**

\- 일반 텍스트 기반의 경량 마크업(Markup) 언어

\- 마크업과 반대 X, 더 쉽고 간단하게 사용할 수 ㅇ

\- `.md` 확장자



```
Markup(마크업)

Mark로 둘러싸인 언어(mark : 글의 역할을 지정하는 표시)
```



**마크다운의 장점, 단점, 주의사항**

1. 장점
   - 문법이 직관적, 쉽다
   - 관리 쉽다
   - 지원 가능한 플랫폼과 프로그램 다양
2. 단점
   - 표준이 없어서 사용자마다 문법 상이
   - 모든  HTML 마크업 기능을 대신하지는 X
3. 주의사항
   - 반드시 '역할'에 맞는 마크다운 문법으로만 작성



**사용방법(문법)**

**\#** 제목

**\-** 목록

**\*글자* / \_글자_** : 기울이기

**\___ + Enter** : 수평선 나누기

**\**글자** / **\__글자__** : 굵게

**\~~글자~~** : 취소선

**\`  `** : 인라인 코드(한 줄)

**``` ** : 블록 코드(여러 줄)

**Ctrl + / ** : raw하게 보기 

**Ctrl + Enter** : 표 행 추가

**Ctrl + Shift + Backspace** : 표 행 삭제

**\\** : 원래 쓰는 거 그대로 이용



**Links(링크)**

`[표시할 글자](이동할 주소)`

```
[GOOGLE](https://google.com)을 눌러서 구글로 이동하세요.
```



**Images(이미지)**

`![대체 텍스트](이미지 주소)`

\- 대체 텍스트 : 이미지를 정상적으로 불러오지 못했을 때 표시되는 문구

(Typora에서는 이미지를 끌어서 놔도 자동으로 업로드 됨)

```
Git 로고입니다.
![Git로고](https://git-scm.com/images/log@2x.png)
```



**Blockquote(인용)**

`>` 사용(중첩 가능)

```
> 인용문을 작성합니다.
>> 중첩된 인용문
>>> 중첩된 인용문2
...
```





---

# Git



**Git이란?**

\- 분산 버전 관리 시스템



**초기 설정**

\- 최초 1번만 설정

```bash
#설정
$ git config --global user.name "이름"
$ git config --global user.email "이메일 주소"

#확인
$ git config --global -list(l)
```



**기본 명령어**

![명령어 사진](https://hphk.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F7142d992-3d01-481c-9d4e-e818c6e185d8%2FUntitled.png?table=block&id=f922af90-788d-4a13-aa3b-75e1b5e2a309&spaceId=daa2d103-3ecd-4519-8c30-4f55e74c7ef4&width=2000&userId=&cache=v2)



- `Working Directory(= Working Tree)` : 사용자의 일반적인 작업이 일어나는 곳
- `Staging Area (= Index)` : 커밋을 위한 파일 및 폴더가 추가되는 곳
- `Repository` : staging area에 있던 파일 및 폴더의 변경사항(커밋)을 저장하는 곳
- working directory → staging area → repository 과정으로 버전 관리 수행



1. git init

   - 현재 작업 중인 디렉토리를 git으로 관리한다는 명령어

   - `.git`이라는 숨김 폴더 생성, 터미널에는 `(master)`라고 표기

     ```bash
     $ git init
     ```

      

     ```
     ! 주의 사항 !
     
     1. 이미 git저장소인 폴더 내에 또다른 git저장소를 만들지 X(중첩 금지)
     2. 절대로 홈 디렉토리에서 git init 하지 X 
        (터미널의 경로가 ~ 인지 확인하면 ㅇ)
     ```

      

2. git status

   - working directory와 staging area에 있는 파일의 현재 상태를 알려주는 명령어

   - 작업 시행 전 수시로 status 확인하면 좋음

   - 상태

     - `untracked` : git이 관리하지 않는 파일(staging area에 한 번도 간 적 없는)

     - `tracked` : git이 관리하는 파일

       - `unmodified` : 최신 상태

       - `modified` : 수정됐지만 아직 staging area에는 반영  안된 상태

       - `staged` : staging area에 올라간 상태

          

   ![file's lifecycle](https://hphk.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F67719520-a1d8-4cbb-81dd-49dea429a7f4%2FUntitled.png?table=block&id=c646e753-b20e-4bdb-a77e-00bcd6518f0a&spaceId=daa2d103-3ecd-4519-8c30-4f55e74c7ef4&width=2000&userId=&cache=v2)

   

3. git add

   - Working directory에 있는 파일을 Staging Area로 올리는 명령어

   - Git이 해당 파일을 추적할 수 있도록

   - `Staged`로 상태 변경

      

4. git commit

   - Staging area에 올라온 파일의 변경 사항을 하나의 버전(커밋)으로 저장하는 명령어

   - 커밋 메세지는 변경사항 잘 나오게, 의미있게 작성하는 게 b

   - 각각의 커밋은 `SHA-1`알고리즘에 의해 반환된 고유의 해시값을 ID로 가짐

   - `(root-commit)`은 해당 커밋이 최초의 커밋일 때만 표시, 이후엔 사라짐

      

5. git log

   - 커밋의 내역을 조회할 수 있는 명령어(ID, 작성자, 시간, 메세지 등)

   - 옵션

     - `--oneline` : 한 줄로 축약해서

     - `--graph` : 브랜치와 머지 내역을 그래프로

     - `--all` : 현재 브랜치를 포함한 모든 브랜치의 내역 보여주기

     - `--reverse` : 커밋 내역의 순서를 반대로(최신이 가장 아래)

     - `-p` : 파일의 변경 내용도 같이 보여줌

     - `-2` : 원하는 갯수 만큼의 내역(2말고 임의의 숫자 가능)

        

```
옵션과 인자

옵션 : 명령어의 '동작 방식' 지정(생략 가능)
	  부가적인 기능 원할 때 사용
	  git log(o)
	  git log --oneline(o)
인자 : 명령어의 '동작 대상'을 지정(생략 불가능)
      git add(x)
      git add a.txt(o)
```



**강사님이 정리해주신 git사용**

- git을 이용한 버전관리 작성자 등록(한 번만)
  - git config --global user.name ~
  - git config --global user.email ~
  - git config --global --list
- 어떤 폴더를 git으로 버전관리하겠다
  - git init
- working directory → staging area로
  - git add a.txt
- staging area(인덱스) → commit(버전)으로
  - git commit -m "~Reason~"
- 현재 git이 관리하는 파일의 상태
  - git status     
  - ↑얘는 자주 해줘야
- 나의 버전 로그
  - git log



`U → A → M → 흑색으로 변해야`



**한 눈에 보는 Git 명령어**

![총정리](https://hphk.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fc86c667a-616f-45b6-892e-15da6a3c494e%2FUntitled.png?table=block&id=64acc3f6-5a25-4342-b6b1-a6a45f61b1f6&spaceId=daa2d103-3ecd-4519-8c30-4f55e74c7ef4&width=2000&userId=&cache=v2)
