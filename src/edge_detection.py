def detect_edges(image):
    # 이미지에서 엣지를 검출하는 함수

    # 그레이 스케일 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 가우시안 블러 적용
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 캐니 엣지 검출
    edges = cv2.Canny(blurred, 50, 150)

    return edges
