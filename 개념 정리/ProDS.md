## 1. 데이터 전처리 : 데이터 생성, 데이터 정제



데이터 마이닝

- 대용량 데이터 > 패턴 > 정보



머신러닝 알고리즘

- 데이터 > 패턴



**데이터 전처리**

- 데이터 생성
  - 요약변수
    - 수집된 정보를 분석의 정보의 목적에 맞게 **종합**(aggregate)한 변수
    - 단어의 빈도, 상품별 구매금액, 영화 매출액
    - **재활용성 높음**
  - 파생변수
    - 특정한 의미를 갖는 작위적 정의에 의한 변수
    - 매우 **주관적**일 수 있으므로 논리적 타당성을 갖춰야 함
    - 구매상품 다양성 변수, 가격 선호대 변수, 라이프 스타일 변수, 영화 인기도 변수



**데이터 정제**

- 결측값의 이해
  - 정보의 손실을 최소화하도록 결측을 처리하는 것이 바람직
  - 완전제거법(list-wise deletion)
    - 정보의 손실로 분석 결과가 왜곡될 수 있음
  - 평균대체법(mean value imputation)
    - 추정량의 표준오차가 과소추정되는 문제가 있음
  - 핫덱대체법(hot deck imputation)
    - 동일한 데이터 내에서 결측값이 발생한 관찰치와 유사한 특성을 가진 다른 관찰치의 정보를 이용해서 대체
  - 그 밖의 처리법
    - regression imputation(다른 변수들 회귀분석을 통해서 회귀식을 통한 결측치 대체법), kNN imputation 등
- 이상값의 이해
  - 상자그림
  - 표준화 점수(Z-score)
    - 표준화 점수의 절대값이 +- 2 사이 95% 밖을 벗어나면 이상치라고 판단
    - z로 변환하게 되면 언제나 그 평균값이 0이고 표준편차가 1이 된다는 특징
  - 처리 방법
    - 이상값 제외(triming)
      - 간단하지만 정보 손실
      - 추정량 왜곡 생길 수 있음
    - 이상값 대체(winsorization)
      - 정상값 중 최대 또는 최소 등으로 대체(우선 정상값 범위 판단하고 이용)
    - 변수 변환
      - 자료값 전체에 로그 변환, 제곱근 변환 등을 적용
- 연속형 자료의 범주화
  - 변수구간화(binning)
    - 연속형 변수를 구간을 활용해서 범주화
    - 이상치 문제를 완화시키고, 결측치 처리 방법이 될 수 있음
    - 변수 간 관계가 단순화 > 분석 시 과적합 방지, 결과 해석 용이해짐



---



## 2. 데이터 전처리 : 데이터 변환, 데이터 결합



**데이터 변환**

- 자료 변환을 통해 자료 해석 쉽고 풍부하게
- 목적
  - 분포의 대칭화
  - 산포를 비슷하게 하기 위해
  - 변수 간 관계 단순하게 하기 위해(like 비선형 > 선형)
- 제곱근 변환 vs 제곱 변환
  - 제곱근 : 왼쪽 꼬리 길어지고
  - 제곱 : 오른쪽 꼬리 길어지고
- 로그 변환 vs 지수 변환(조금 더 크게 치우침이 생김)
  - 로그  : 왼쪽 꼬리 길어지고
  - 지수 : 오른쪽 꼬리 길어지고
- 박스콕스 변환(box-cox transform)
  - 원점을 지나감
  - 왼쪽 꼬리가 긴 애들은 x가 클수록 y값이 급격히 커짐
  - 반대의 경우도 ㅇ



기울기가 급격히 상승하는 형태 >> x를 제곱 또는 지수변환 or y를 제곱근 또는 로그변환 하면 선형관계가 됨



오른쪽 꼬리 길 때  : 로그 제곱근

왼쪽꼬리 길 때 : 지수 제곱



**데이터 결합**

- 이너조인
  - 두 테이블에 키가 공통으로 존재하는 레코드만 결합
- 풀아우터조인
  - 어느 한 쪽이라도 존재하는 키에 대한 레코드를 모두 결합
- 레프트조인
  - 왼쪽 테이블에 존재하는 키에 대한 레코드를 결합
- 라이트조인
  - 오른쪽 테이블에 존재하는 키에 대한 레코드를 결합



---



## 3. 머신러닝의 기본 개념 및 방법론의 분류



**머신러닝**

> 명시적으로 프로그래밍하지 않더라도 데이터를 스스로 학습해서 문제를 해결할 수 있게 하는 기술
>
> 사람이 인지하기 어려운 복잡한 규칙과 패턴을 파악하여 의미있는 결과를 얻을 수 있음



**머신러닝 방법론의 분류**

- 지도학습(supervised learning)
  - 라벨이 있는 훈련용 데이터에서 여러 특성 변수를 이용해서 목표변수인 라벨을 예측하도록 학습
  - 라벨의 데이터 타입에 따라 라벨이 연속형(숫자로)이면 **회귀**(regression) 알고리즘, 라벨이 범주형이면 **분류**(classification) 알고리즘으로 구분
  - 분류형 > 분류 경계선을 찾아내는 것
  - 회귀형 > 어떤 함수를 찾아내는 것(직선)
  - 분류형 : linear regression, k-nearest neighbors, logistic regression, softmax regression
  - 회귀+분류형 : decision tree, svm, random forest, boosting, neural network, deep learning
  - x,y(범주형, 연속형)
- 비지도학습(unsupervised learning)
  - 라벨이 없는 훈련용 데이터에서 특정 변수들 간 관계나 유사성 기반으로 의미있는 패턴 추출
  - '자율학습'
  - 군집화(clustering), 차원축소(dimention reduction), 추천시스템 등에 활용
  - 차원축소 : 특성변수들만 모아서 차원축소, 최대한 많이 남기면서 필요한 데이터들만 > 예측력 높일 수 ㅇ
  - k-means clustering, hierachical clustering, pca, t-sne, apirori, auto-encoders
  - x
- 강화학습(reinforcement learning)
  - 행동하는 주체가 있고 행동 했을 때 상태와 보상을 바꿔주는 환경으로 구성
  - sarsa, q-learning



---



## 4. 머신러닝 모델의 검증 및 평가

>아주 복잡한 패턴이 학습 가능



**지도학습 분석 절차**

1. 데이터 전처리 탐색

2. 모델 선택

3. 주어진 데이터로 모델 훈련

4. 모델 적용해서 새로운 데이터에 대한 예측 수행



과대적합의 문제

- 미래의 새로운 자료에 대한 예측력이 떨어지는 문제
- 복잡한 알고리즘 사용해서 데이터 훈련할 시 과적합 문제를 항상 염두에 두어야 함



**모델 평가의 필요성**

1. 과대적합 막고 일반화 오차 줄이기 위해서는 새로운 데이터에 얼마나 잘 일반화될지 판단해야 함
2. 평가만을 위한 데이터를 확보할 필요 있음(재활용하지 않고)



**모델 평가**

1. hold-out 방식
   - 두 그룹 또는 세 그룹으로 쪼개서 train, test로 활용(세 개는 validation 튜닝)
2. k-fold 교차검증(cross-validation)
   - 자료가 충분하지 않은 경우에는 교차검정 기법 사용
   - 1,2를 두고 3을 테스트, 2,3을 두고 1을 테스트 ... 이렇게 반복해서 찾아낸 성능들의 average같은 것들로 평가