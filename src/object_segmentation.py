def segment_objects(image, depth_map, edges):
    # 이미지와 깊이 맵을 입력으로 받아 객체를 세분화하는 함수

    # 엣지 영상을 이진화하여 객체 경계를 생성
    ret, threshold = cv2.threshold(edges, 127, 255, 0)

    # 경계선을 찾기 위해 findContours 함수 적용
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 객체별로 루프 수행
    for contour in contours:
        # 각 객체의 외곽선을 그리기
        cv2.drawContours(image, contour, -1, (0, 255, 0), 3)

    return image
