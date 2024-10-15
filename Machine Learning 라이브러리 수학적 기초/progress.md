# 진행상황

## 09.24

#### 선형대수란?

연립일차방정식으로 미지수를 풀어내는 것
"Solving for unknowns within system of linear equations"

특징으로는

식을 그렸을 때 직선이며(선형)

직선끼리 만나지 않거나(해가 없음)
<br>
직선이 교차하거나(유일한 해가 있음)
<br>
직선이 일치하거나(해가 무한)
<br>
의 경우가 있다.

tensor나 합성곱 신경망이 될 수 있는 선형대수의 구조들을 맛보기로 보여줌

선형대수의 기원을 간략하게 알아봄

#### 다음 강의 예고

- tensor에 대해서 배울 예정

## 09.25

#### 3. 선형방정식 시스템 plot 그리기

**What Linear Algebra Is**
<br>
파이썬으로 간단한 선형 방정식 문제 풀어보기

[3-1파일](3-1.py)에서 실습

[실습결과](3-1result.png)

#### 다음강의 예고

- 간단한 연습문제를 종이와 펜으로 풀어볼 예정

## 09.27

#### 4. 선형대수 연습문제

종이와 펜을 사용해 간단한 선형 방정식 문제 풀어보기

1 \* (t + 30) = 4t 를 사용해 mark2가 만들어지고 10일 후에 mark2가 mark1의 전기 생산량을 따라잡는다는 결과가 나옴.

#### 5. 텐서

PyTorch와 TensorFlow를 사용하여 '텐서' 라는 개념을 알아봄

텐서 : 벡터공간에서 선형관계를 나타낼 때 쓰는 특수한 자료구조
<br>
[학습일지링크](https://velog.io/@oasisgorilla/%EA%B3%B5%EB%B6%80%EC%9D%BC%EC%A7%80%ED%85%90%EC%84%9CTensor%EB%9E%80)

#### 6. 스칼라

PyTorch와 TensorFlow를 사용하여 '스칼라' 라는 개념을 알아봄
<br>
[학습일지링크](https://velog.io/@oasisgorilla/%EA%B3%B5%EB%B6%80%EC%9D%BC%EC%A7%80%ED%85%90%EC%84%9C%EC%97%90-%EB%8C%80%ED%95%B4-%EB%8D%94-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90%EC%8A%A4%EC%B9%BC%EB%9D%BC)

#### 7. 벡터와 벡터의 전치

PyTorch와 TensorFlow를 사용하여 '벡터' 라는 개념을 알아봄
벡터의 전치 : 백터의 열과 행을 바꾸는 것
<br>
[학습일지링크](https://velog.io/@oasisgorilla/%EA%B3%B5%EB%B6%80%EC%9D%BC%EC%A7%80%ED%85%90%EC%84%9C%EC%97%90-%EB%8C%80%ED%95%B4-%EB%8D%94%EB%8D%94%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90%EB%B2%A1%ED%84%B0)

## 09.30

#### 8. 노름벡터와 단위벡터

벡터의 크기를 표현하는 norm의 종류에 대해 알아보고, 각각 특징과 쓰임을 알아봄
<br>google colab을 사용하여 간단한 예제 실습
<br>
[학습일지링크](https://velog.io/@oasisgorilla/%EA%B3%B5%EB%B6%80%EC%9D%BC%EC%A7%80%ED%85%90%EC%84%9C%EC%97%90-%EB%8C%80%ED%95%B4-%EB%8D%94%EB%8D%94%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90%EB%B2%A1%ED%84%B0)

## 10.01

#### 9. 기저, 직교, 정규직교 벡터

특수한 벡터들을 추가적으로 알아보았음
<br>
[학습일지링크](https://velog.io/@oasisgorilla/%EA%B3%B5%EB%B6%80%EC%9D%BC%EC%A7%80%ED%85%90%EC%84%9C%EC%97%90-%EB%8C%80%ED%95%B4-%EB%8D%94%EB%8D%94%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90%EB%B2%A1%ED%84%B0)

#### 10. 행렬 텐서

행렬텐서에 대해 알아봄<br>
[학습일지링크](https://velog.io/@oasisgorilla/%EA%B3%B5%EB%B6%80%EC%9D%BC%EC%A7%80%ED%85%90%EC%84%9C%EC%97%90-%EB%8C%80%ED%95%B4-%EB%8D%94%EB%8D%94%EB%8D%94-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90%ED%96%89%EB%A0%AC)

추가로 [10-2파일](10-2.py)에서 NumPy로 벡터를 만들어 연산하는 것과 파이썬으로 2차원배열을 만들어 연산하는 것의 차이를 알아봄

[학습일지링크1](https://velog.io/@oasisgorilla/%EA%B3%B5%EB%B6%80%EC%9D%BC%EC%A7%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B0%EC%97%B4%EA%B3%BC-NumPy%EB%B0%B0%EC%97%B4%EC%9D%98-%EC%B0%A8%EC%9D%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B01),
[학습일지링크2](https://velog.io/@oasisgorilla/%EA%B3%B5%EB%B6%80%EC%9D%BC%EC%A7%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B0%EC%97%B4%EA%B3%BC-NumPy%EB%B0%B0%EC%97%B4%EC%9D%98-%EC%B0%A8%EC%9D%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0NumPy%EB%B0%B0%EC%97%B4-%EB%B6%84%EC%84%9D)

#### 11. 일반적인 텐서 표기법

이미지 데이터를 학습하는 경우를 예시로 4차원 텐서 표기법을 알아봄

#### 12. 대수 데이터 구조 연습문제

수학적으로 행렬의 전치나 특정 원소를 나타내는 등의 표기법을 테스트함

#### 13. 부분 소개

지금까지 진행한 부분과 앞으로 진행할 6가지 부분에 대해서 개관을 설명해줌

## 10.03

#### 15. 아다마르 곱을 포함한 기초 텐서 연산

TensorFlow나 PyTorch를 사용하여 기초적인 연산을 구글 코랩에서 실습

[학습일지 링크](https://velog.io/@oasisgorilla/%EA%B3%B5%EB%B6%80%EC%9D%BC%EC%A7%80%ED%85%90%EC%84%9C%EC%97%B0%EC%82%B0%EC%95%84%EB%8B%A4%EB%A7%88%EB%A5%B4-%EA%B3%B1-%EA%B8%B0%EC%B4%88%EC%97%B0%EC%82%B0)

지금까지 진행했던 실습 내용 정리

## 10.04 ~ 06
복습 및 velog 정리

## 10.07

#### 16. 텐서 리덕션

TensorFlow나 PyTorch를 사용하여 텐서 리덕션을 구글 코랩에서 실습

[학습일지 링크](https://velog.io/@oasisgorilla/%EA%B3%B5%EB%B6%80%EC%9D%BC%EC%A7%80%ED%85%90%EC%84%9C%EC%97%B0%EC%82%B0%EB%A6%AC%EB%8D%95%EC%85%98)

#### 17. 내적

TensorFlow나 PyTorch를 사용하여 내적을 구글 코랩에서 실습

[학습일지 링크](https://velog.io/@oasisgorilla/%EA%B3%B5%EB%B6%80%EC%9D%BC%EC%A7%80%ED%85%90%EC%84%9C%EC%97%B0%EC%82%B0%EB%82%B4%EC%A0%81)

#### 18. 텐서 계산 연습문제

#### 19. 대입을 통한 선형계 해법

#### 20. 소거법을 통한 선형계 해법

#### 21. 선형계 시각화
matplot 라이브러리를 사용한 선형계 시각화 예시를 보여줌

## 10.10

#### 22. 부분소개

#### 23. Frobenius의 일반적인 기준
8강에서 배웠던 L2 norm(유클리드 norm)의 확장 개념을 배워봄
[관련 학습일지 링크](https://velog.io/@oasisgorilla/%EA%B3%B5%EB%B6%80%EC%9D%BC%EC%A7%80%ED%85%90%EC%84%9C%EC%97%90-%EB%8C%80%ED%95%B4-%EB%8D%94%EB%8D%94%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90%EB%B2%A1%ED%84%B0)

[학습일지 링크](https://velog.io/@oasisgorilla/%EA%B3%B5%EB%B6%80%EC%9D%BC%EC%A7%80Frobenius-norm)

## 10.11

#### 24. 행렬곱
행렬곱을 이론적으로 배우고, 코랩에서 코드로 실습,<br>
행렬곱이 머신러닝에서 실제로 어떻게 쓰이는지를 집 가격 추론 예시를 통해 배워봄

[학습일지 링크](https://velog.io/@oasisgorilla/%EA%B3%B5%EB%B6%80%EC%9D%BC%EC%A7%80%ED%96%89%EB%A0%AC%EA%B3%B1-jphvw8qa)

## 10.12

#### 25. 대칭 및 단위 행렬
단위행렬 학습, 단위행렬 학습을 위한 대칭행렬 개념 학습 후 코랩에서 코드로 실습

[학습일지 링크](https://velog.io/@oasisgorilla/AI-%EC%88%98%ED%95%99%EC%A0%81-%EA%B8%B0%EC%B4%88%EC%97%AC%EB%9F%AC%EA%B0%80%EC%A7%80-%ED%96%89%EB%A0%AC)

## 10.13

#### 26. 행렬 곱 연습문제
종이와 펜을 갖고 행렬 곱 연습문제 풀어봄

## 10.15

#### 27. 역행렬
역행렬의 특성을 배우고, 어디에 사용되는지(선형회귀) 학습,<br>
코랩에서 코드로 가중치w 벡터를 구하는 실습

[학습일지 링크](https://velog.io/@oasisgorilla/AI-%EC%88%98%ED%95%99%EC%A0%81-%EA%B8%B0%EC%B4%88%EC%97%AC%EB%9F%AC%EA%B0%80%EC%A7%80-%ED%96%89%EB%A0%AC)

#### 28. 대각행렬
대각행렬의 특성을 학습함

[학습일지 링크](https://velog.io/@oasisgorilla/AI-%EC%88%98%ED%95%99%EC%A0%81-%EA%B8%B0%EC%B4%88%EC%97%AC%EB%9F%AC%EA%B0%80%EC%A7%80-%ED%96%89%EB%A0%AC)

#### 29. 직교행렬
이전에 배웠던 직교벡터, 기저벡터 개념을 확장하여<br>
직교행렬 개념을 학습하고, 그 쓰임을 알아봄

[학습일지 링크](https://velog.io/@oasisgorilla/AI-%EC%88%98%ED%95%99%EC%A0%81-%EA%B8%B0%EC%B4%88%EC%97%AC%EB%9F%AC%EA%B0%80%EC%A7%80-%ED%96%89%EB%A0%AC)

#### 30. 직교행렬 연습문제
단위행렬I와 어떠한 행렬K가 직교행렬인지 증명하는 과정을 수식으로 이해하고,<br>
코랩에서 실습