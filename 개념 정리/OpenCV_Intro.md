# opencv

> 컴퓨터 비전을 목적으로 한 프로그래밍 라이브러리
>
> \> 실시간 이미지 프로세싱에 중점



영상 신호의 디지털화 과정

**Sampling(표본화) → Quantizing(양자화) → Coding(부호화)**



## Sampling

`pixel` : picture element = pixel(화소)

`voxel` : volume element (MRI, CT 이런 곳에 쓰임)



`dpi` : (dots per inch) 픽셀 당 dot

`ppi` : c(대각선)에 있는 pixel의 수



`cartesian coordinate` : 직교좌표계(x1, y1)

`polar coordinate` : 극좌표계(반지름 , 세타)



`jpg` : 손실압축

`png` : 무손실압축



디지털 영상의 유형

- binary image 
  - = mask image : 0과 1로만
    - dithering : 밀도조절(크기 조절 X)
    - halftoning : 점 크기를 조절
- grayscale image
  - 흑백
- multi-spectral image
  - 여러 소스 합쳐서
- color image
  - 컬러



검정 > 0

흰색 > 255



RGB 24 bit >> 8bit짜리 3개



