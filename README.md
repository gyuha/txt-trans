## 파이썬 설치 하기

`pyenv`를 설치하고 python을 설치 하자.. 이것도 버전 관리가 필요 함..

- [https://pyenv-win.github.io/pyenv-win/](https://pyenv-win.github.io/pyenv-win/)

초코로 아래와 같이 설치하는게 가장 간단.

```
choco install pyenv-win
pyenv install --list
pyenv install [version]

```

## poetry(패키지 관리자) 설치

[](https://python-poetry.org/docs/)

### Powershell

```
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -

```

설치 프로그램은 Poetry의 bin 디렉토리의 path를 설정 해 줍니다. Unix에서는 `$HOME/.poetry/bin`에, Windows에서는 `%USERPROFILE%\.poetry\bin`에 있습니다.

<aside>
💡 윈도우의 경우 설치 후 잘 동작을 하지 않는 경우가 있다. 이럴때는 지웠다가 다시 설치 해 주면 된다.

</aside>

## peotry 설정하기

그냥 peotry를 사용하게 되면 user 폴더에 .venv 파일이 생성되어서.. vscode에서는 연결해서 사용하기 어렵다. 그래서 아래와 .venv 파일의 경우를 프로젝트 경로에 생성 되도록 해 준다.

```
poetry config virtualenvs.in-project true
poetry config virtualenvs.path "./.venv"
```

## 파이썬 가상 환경 만들어 주기

### peotry로 만들기

```
peotry install
.venv/Scripts/activate
```

`macos` or `linux`에서는 아래와 같이 실행 한다.

```
source .venv/bin/activate
```

`peotry`를 해 주면.. `.venv` 폴더를 만들고 여기에 패키지를 설치해 준다.
