import cv2
import numpy as np

def generate_depth_map(images):
    # Convert images to grayscale
    gray_images = [cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) for image in images]

    # Initialize StereoSGBM object
    stereo = cv2.StereoSGBM_create(minDisparity=0, numDisparities=16, blockSize=15)

    # Compute disparity map
    disparity = stereo.compute(gray_images[0], gray_images[1])

    # Normalize disparity map
    min_disp = disparity.min()
    max_disp = disparity.max()
    normalized_disparity = np.uint8((disparity - min_disp) * 255 / (max_disp - min_disp))

    return normalized_disparity

# def generate_depth_map(image_left, image_right):
#     # Convert images to grayscale
#     gray_left = cv2.cvtColor(image_left, cv2.COLOR_BGR2GRAY)
#     gray_right = cv2.cvtColor(image_right, cv2.COLOR_BGR2GRAY)
    
#     # 기존 코드에서 ORB 특징점 검출 및 매칭 코드 추가
#     orb = cv2.ORB_create()
#     keypoints_left, descriptors_left = orb.detectAndCompute(gray_left, None)
#     keypoints_right, descriptors_right = orb.detectAndCompute(gray_right, None)
#     bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
#     matches = bf.match(descriptors_left, descriptors_right)
#     matches = sorted(matches, key=lambda x: x.distance)
#     src_pts = np.float32([keypoints_left[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
#     dst_pts = np.float32([keypoints_right[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
    
#     # 깊이 맵 생성 부분 수정
#     disparity_map = np.zeros_like(gray_left)
#     for i in range(len(matches)):
#         x_left, y_left = src_pts[i][0]
#         x_right, y_right = dst_pts[i][0]
#         disparity_map[int(y_left), int(x_left)] = np.abs(x_left - x_right)
    
#     return disparity_map


# def generate_depth_map(image_left, image_right):
#     # 스테레오 카메라로 촬영한 이미지를 입력받아 깊이 맵을 생성하는 함수

#     # 스테레오 이미지를 그레이 스케일로 변환
#     gray_left = cv2.cvtColor(image_left, cv2.COLOR_BGR2GRAY)
#     gray_right = cv2.cvtColor(image_right, cv2.COLOR_BGR2GRAY)

#     # 스테레오 매칭 알고리즘 설정
#     stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)

#     # 깊이 맵 생성
#     depth_map = stereo.compute(gray_left, gray_right)

#     return depth_map
