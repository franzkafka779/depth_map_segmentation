import cv2
import numpy as np
from depth_map import generate_depth_map
from edge_detection import detect_edges
from object_segmentation import segment_objects

def resize_image(image, target_resolution):
    # 이미지를 지정된 해상도로 리사이징하는 함수
    resized_image = cv2.resize(image, target_resolution)
    return resized_image

def generate_depth_map2(image_left, image_right):
    # 스테레오 카메라로 촬영한 이미지를 입력받아 깊이 맵을 생성하는 함수

    # 스테레오 이미지를 그레이 스케일로 변환
    gray_left = cv2.cvtColor(image_left, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(image_right, cv2.COLOR_BGR2GRAY)

    # 스테레오 매칭 알고리즘 설정
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)

    # 깊이 맵 생성
    depth_map = stereo.compute(gray_left, gray_right)

    return depth_map

def save_segmented_images(segmented_wide, segmented_wide_mono):
    cv2.imwrite("segmented_wide.jpg", segmented_wide)
    cv2.imwrite("segmented_wide_mono.jpg", segmented_wide_mono)

def main():
    # 이미지 파일 경로 설정
    image_wide_path = "data/wide_image.jpg"
    image_ultra_wide_path = "data/ultra_wide_image.jpg"
    image_telephoto_path = "data/telephoto_image.jpg"

    # 이미지 불러오기
    image_wide = cv2.imread(image_wide_path)
    image_ultra_wide = cv2.imread(image_ultra_wide_path)
    image_telephoto = cv2.imread(image_telephoto_path)

    # 각 카메라의 해상도에 맞게 이미지 리사이징
    target_resolution = (1920, 1080)  # 예시 해상도 설정
    resized_wide = resize_image(image_wide, target_resolution)
    resized_ultra_wide = resize_image(image_ultra_wide, target_resolution)
    resized_telephoto = resize_image(image_telephoto, target_resolution)

    # 엣지 검출
    edges_wide = detect_edges(resized_wide)
    edges_ultra_wide = detect_edges(resized_ultra_wide)
    edges_telephoto = detect_edges(resized_telephoto)

    # 깊이 맵 생성
    depth_map_wide = generate_depth_map([resized_wide, resized_ultra_wide, resized_telephoto])
    depth_map_mono = generate_depth_map2(resized_wide, resized_ultra_wide)
    
    # 객체 세분화
    segmented_wide = segment_objects(resized_wide, depth_map_wide, edges_wide)
    segmented_wide_mono = segment_objects(resized_wide, depth_map_mono, edges_wide)
    
    # 결과 이미지 표시
    cv2.imshow("Segmented Wide Image", segmented_wide)
    cv2.imshow("Segmented Wide Image (Mono)", segmented_wide_mono)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    # 결과 이미지 저장
    save_segmented_images(segmented_wide, segmented_wide_mono)

   


if __name__ == "__main__":
    main()



# def main():
#     # 메인 함수에서는 이미지를 불러오고 각 단계의 함수를 호출하여 실행합니다.

#     # 이미지 파일 경로 설정
#     image_wide_path = "data/wide_image.jpg"
#     image_ultra_wide_path = "data/ultra_wide_image.jpg"
#     image_telephoto_path = "data/telephoto_image.jpg"

#     # 이미지 불러오기
#     image_wide = cv2.imread(image_wide_path)
#     image_ultra_wide = cv2.imread(image_ultra_wide_path)
#     image_telephoto = cv2.imread(image_telephoto_path)

#     # 각 카메라의 해상도에 맞게 이미지 리사이징
#     target_resolution = (1920, 1080)  # 예시 해상도 설정
#     resized_wide = resize_image(image_wide, target_resolution)
#     resized_ultra_wide = resize_image(image_ultra_wide, target_resolution)
#     resized_telephoto = resize_image(image_telephoto, target_resolution)

#     # 깊이 맵 생성
#     depth_map_wide = generate_depth_map(resized_wide, resized_ultra_wide)
#     depth_map_ultra_wide = generate_depth_map(resized_ultra_wide, resized_wide)
#     depth_map_telephoto = generate_depth_map(resized_telephoto, resized_wide)

#     # 엣지 검출
#     edges_wide = detect_edges(resized_wide)
#     edges_ultra_wide = detect_edges(resized_ultra_wide)
#     edges_telephoto = detect_edges(resized_telephoto)

#     # 객체 세분화
#     segmented_wide = segment_objects(resized_wide, depth_map_wide, edges_wide)
#     segmented_ultra_wide = segment_objects(resized_ultra_wide, depth_map_ultra_wide, edges_ultra_wide)
#     segmented_telephoto = segment_objects(resized_telephoto, depth_map_telephoto, edges_telephoto)

#     # 결과 이미지 표시
#     cv2.imshow("Segmented Wide Image", segmented_wide)
#     cv2.imshow("Segmented Ultra Wide Image", segmented_ultra_wide)
#     cv2.imshow("Segmented Telephoto Image", segmented_telephoto)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()
