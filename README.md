# Depth Map and Object Segmentation

이 프로젝트는 다중 카메라를 사용하여 깊이 맵 생성과 객체 세분화를 수행하는 파이썬 코드입니다. 주로 스마트폰의 다중 렌즈 카메라를 대상으로 하며, 각 렌즈로 촬영한 이미지를 이용하여 깊이 맵을 생성하고 객체를 세분화합니다.

## 필요한 라이브러리

이 프로젝트를 실행하기 위해서는 다음과 같은 파이썬 라이브러리가 필요합니다:

- OpenCV
- NumPy

라이브러리를 설치하려면 다음 명령어를 사용합니다:

```
pip install opencv-python
pip install numpy
```

## 파일 구조

```
depth-map-segmentation/
│
├── data/             # 이미지 데이터 디렉토리
│   ├── wide_image.jpg
│   ├── ultra_wide_image.jpg
│   └── telephoto_image.jpg
│
├── src/              # 소스 코드 디렉토리
│   ├── __init__.py
│   ├── depth_map.py
│   ├── edge_detection.py
│   ├── object_segmentation.py
│   └── main.py
│
├── requirements.txt  # 필요한 라이브러리 목록
├── README.md         # 프로젝트 설명 및 사용법
└── LICENSE           # 소스 코드 라이센스 정보
```

- **data/**: 깊이 맵 및 객체 세분화를 수행할 이미지 데이터가 있는 디렉토리입니다.
- **src/**: 깊이 맵 생성, 엣지 검출, 객체 세분화 등의 기능이 구현된 소스 코드가 있는 디렉토리입니다.
- **requirements.txt**: 필요한 라이브러리 목록이 있는 파일입니다.
- **README.md**: 이 파일입니다. 프로젝트 설명과 사용법을 담고 있습니다.

## 사용 방법

1. 이미지 데이터를 `data/` 디렉토리에 추가합니다.
2. `main.py` 파일을 실행하여 깊이 맵 생성 및 객체 세분화를 수행합니다.

```
python src/main.py
```

## 참고 사항

- 이 프로젝트는 파이썬 3.x 버전에서 테스트되었습니다.
- 깊이 맵 생성 및 객체 세분화에는 이미지 해상도, 렌즈 종류 등을 고려하는 추가적인 작업이 필요할 수 있습니다.

## 라이센스

MIT 라이센스를 따릅니다. 자세한 내용은 LICENSE 파일을 참조하세요.
