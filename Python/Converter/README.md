# VideoConverter
---
 
 > 비디오 확장자(코덱) 변환 파일


## # 기능
1.  mov, avi, wmv 등 확장자를 가진 동영상을 `ffmpeg`를 이용해서 웹에서 실행 가능한 `mp4`로 변환해 주는 파일.<br/>
2. `os.walk` 명령어로 입력한 경로의 하위 모든 폴더까지 검색함.<br/>
3. audio & video converter인 `ffmpeg`가 설치 되어 있어야 함.<br/>
5. 변환시 오류난 파일은 마지막에 따로 표시됨.<br/>

## # FFMPEG https://ffmpeg.org/
* **qscale** 
  * 1~51사이 값 입력.<br/>
  * 값이 작을 수록 결과물이 고화질 고용량이 되고, 값이 클 수록 저화질 저용량이 됨.
* **y**
  * 오버라이트

## # 변수

#### 1. rootDir
 * 검색을 시작할 폴더의 Full Path.
   * 윈도우의 경우 "**\\**"를 "**/**"로 변경해서 입력해야 한다.
   * 한글 입력 가능하다.
   * 띄어쓰기가 포함 된 경우 "**\\**" 를 입력하지 않아도 된다.<br/>
   EX) 
   ```python
   rootDir = 'C:/동영상 폴더/'
   ```
   
#### 2. exts (extentions) 확장자
 * 검색할 동영상 확장자
 * 현재는 .mov, .avi, .wmv 외 추가로 검색할 확장자 입력.

#### 3. subprocess.Popen
  * ffmpeg 실행 명령어 입력.
  * 추가로 주고 싶은 옵션이 있으면, `리스트`를 추가해 주면 된다.
  * `콤마`로 구분한다.<br/>
  EX)
   ```python
   # ffmpeg -i 파일이름 -vcodec h264 결과물이름
   subprocess.Popen([
                'ffmpeg',
                '-i',
                파일이름,
                '-vcodec',
                'h264',
                결과물이름,
              ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   ```

