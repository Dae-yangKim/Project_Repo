## 감염병 대응 빅데이터 아이디어 공모전 데이터 분석 및 모델링

### 목차

- [데이터 분석 방법론](#data_analysis)
- [분석](#analysis)
- [군집분석](#clustering)
---

## <a id='data_analysis'><b>데이터 분석 방법론</b></a>
해당 아이디어 공모전의 경우 , 감염병이라는 큰 틀 안에서 주제를 정하여 데이터 분석을 진행해야 하기 때문에
현재 문제가 되고 있는 현황 , 도메인 지식등을 미리 조사하면서 먼저 주제를 정하고 , 데이터를 모은 후에 데이터를 이해하는 과정이 필요했기에 , 방법론으로는
CRISP-DM 방식으로 채택을 함.<br>
<a href="https://ibb.co/XLhRrP8"><img src="https://i.ibb.co/tK7rT6X/CRISP-DM-Process-Diagram.png" alt="CRISP-DM-Process-Diagram" border="0" width="350" height="350"></a><br>
<strong>이미지 출처 : [https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining)</strong>

---

## <a id='analysis'><b>분석</b></a>
분석의 대략적인 프로세스는 아래와 같다<br>
<a href="https://ibb.co/DMFGP52"><img src="https://i.ibb.co/X5PyfSR/24.png" alt="24" border="0"></a>

---

## <a id='clustering'><b>군집분석</b></a>
해당 프로젝트에서 정한 주제는 데이터를 통해서 독거노인의 감염병 치료 취약 지역을 알아내는 것이기 때문에 , 데이터의 유사성에 따라서 군집 분석을 한다.<br>
<b>사용 알고리즘 : K-means</b>

<pre>
  전체적인 프로세스는
  1. 데이터를 통해서 적절한 K를 분석
  2. 군집을 K개 분석한다
</pre>

1. 데이터를 통해서 적절한 K를 분석<br>
두가지 방식을 채택했는데 , <br>
- 실루엣 분석
- 엘보우 메서드
실루엣 분석의 경우 , 1에 가까울 수록 군집이 잘 된 것이고 , 엘보우 메서드의 경우에는 그래프에서 급격하게 떨어지는 지점이 가장 적절한 지점이다.<br>

2. 군집을 K개 분석한다<br>
위의 분석에서 적절한 K를 선택한 후에 모델에 데이터를 넣는다.
