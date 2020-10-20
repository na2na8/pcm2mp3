# pcm2mp3
Convert pcm files to mp3 files

## Usage
```
python run.py -i [input_path] -o [output_path]
```

* input_path : pcm 파일을 갖고 있는 폴더
* output_path : mp3 파일이 만들어질 폴더

커맨드를 입력하기 전에 `output_path` 디렉토리가 존재해야 함.

* 예시
```
python run.py -i /home/pcm -o /home/mp3
```

* run.py에서 `mp3_path`를 수정하여 mp3 외의 wav파일 등으로 export 할 수 있음.

## 필요 프로그램
* ffmpeg
