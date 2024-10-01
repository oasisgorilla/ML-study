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

추가로 [10-1파일](10-1.py)에서 NumPy로 벡터를 만들어 연산하는 것과 파이썬으로 2차원배열을 만들어 연산하는 것의 차이를 알아봄

#### 11. 일반적인 텐서 표기법

이미지 데이터를 학습하는 경우를 예시로 4차원 텐서 표기법을 알아봄

#### 12. 대수 데이터 구조 연습문제

수학적으로 행렬의 전치나 특정 원소를 나타내는 등의 표기법을 테스트함

#### 13. 부분 소개

지금까지 진행한 부분과 앞으로 진행할 6가지 부분에 대해서 개관을 설명해줌
